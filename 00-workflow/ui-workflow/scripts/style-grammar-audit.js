/**
 * Runtime DOM visual-grammar & style-consistency audit.
 *
 * Uses getComputedStyle on rendered DOM trees to catch combinatorial drift
 * that static CSS/regex linters miss (utility classes, CSS variables, prop overrides):
 *   1. Container Surface Clustering & Sibling Containment Drift (bordered vs borderless mix)
 *   2. Runtime Geometry / Border / Shadow / Font-Size Budgets (+ zero-offset glow)
 *   3. Selection State Computed-Style Diffs (> maxSelectionGrammars + fontWeight/border reflow)
 *   4. Same-Role Control Parity (buttons / inputs / tabs height & radius consistency)
 *
 * Usage:
 *   Pass `auditStyleGrammar` into Playwright `page.evaluate(auditStyleGrammar, budgets)`
 *   or run directly in browser DevTools Console.
 */
function auditStyleGrammar(options) {
  const opts = options || {};
  const budgets = {
    maxSurfaceLevels: typeof opts.maxSurfaceLevels === "number" ? opts.maxSurfaceLevels : 4,
    maxDistinctRadius: typeof opts.maxDistinctRadius === "number" ? opts.maxDistinctRadius : 4,
    maxBorderStyles: typeof opts.maxBorderStyles === "number" ? opts.maxBorderStyles : 2,
    maxShadowLevels: typeof opts.maxShadowLevels === "number" ? opts.maxShadowLevels : 2,
    maxFontSizes: typeof opts.maxFontSizes === "number" ? opts.maxFontSizes : 6,
    maxSelectionGrammars: typeof opts.maxSelectionGrammars === "number" ? opts.maxSelectionGrammars : 2,
    maxControlHeightsPerRole: typeof opts.maxControlHeightsPerRole === "number" ? opts.maxControlHeightsPerRole : 3,
    maxControlRadiiPerRole: typeof opts.maxControlRadiiPerRole === "number" ? opts.maxControlRadiiPerRole : 2,
    minContainerWidth: typeof opts.minContainerWidth === "number" ? opts.minContainerWidth : 120,
    minContainerHeight: typeof opts.minContainerHeight === "number" ? opts.minContainerHeight : 48,
    maxSamples: typeof opts.maxSamples === "number" ? opts.maxSamples : 5,
  };

  function describeNode(el) {
    const tag = (el.tagName || "div").toLowerCase();
    const id = el.id ? "#" + el.id : "";
    const cls =
      typeof el.className === "string" && el.className.trim()
        ? "." + el.className.trim().split(/\s+/).slice(0, 2).join(".")
        : "";
    return tag + id + cls;
  }

  function isTransparent(color) {
    if (!color || color === "transparent") return true;
    const m = color.match(/rgba\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*,\s*([0-9.]+)\s*\)/i);
    return m ? parseFloat(m[1]) === 0 : false;
  }

  function normalizeRadius(raw) {
    if (!raw) return 0;
    const m = String(raw).match(/^(\d+(?:\.\d+)?)px/);
    if (!m) return 0;
    const v = Math.round(parseFloat(m[1]));
    return v >= 900 ? 999 : v;
  }

  function visibleBorder(cs) {
    const sides = [
      [cs.borderTopWidth, cs.borderTopStyle, cs.borderTopColor],
      [cs.borderRightWidth, cs.borderRightStyle, cs.borderRightColor],
      [cs.borderBottomWidth, cs.borderBottomStyle, cs.borderBottomColor],
      [cs.borderLeftWidth, cs.borderLeftStyle, cs.borderLeftColor],
    ];
    const active = [];
    for (let i = 0; i < sides.length; i += 1) {
      const w = parseFloat(sides[i][0]) || 0;
      const st = sides[i][1] || "none";
      const col = sides[i][2] || "transparent";
      if (w > 0 && st !== "none" && !isTransparent(col)) {
        active.push(Math.round(w * 10) / 10 + "px " + st + " " + col);
      }
    }
    if (active.length === 0) return "none";
    const uniq = Array.from(new Set(active));
    return active.length === 4 && uniq.length === 1 ? "all:" + uniq[0] : "partial:" + uniq.join("|");
  }

  function hasZeroOffsetGlow(boxShadow) {
    if (!boxShadow || boxShadow === "none") return false;
    return /(?:^|,)\s*(?!inset)0(?:px)?\s+0(?:px)?\s+[1-9]\d*(?:\.\d+)?px/i.test(boxShadow);
  }

  function isSelectedNode(el) {
    if (!el.getAttribute) return false;
    if (el.getAttribute("aria-selected") === "true") return true;
    const cur = el.getAttribute("aria-current");
    if (cur && cur !== "false") return true;
    const ds = el.getAttribute("data-state");
    if (ds === "active" || ds === "on" || ds === "checked") return true;
    if (el.getAttribute("data-selected") === "true" || el.getAttribute("data-active") === "true") return true;
    if (typeof el.className === "string") {
      const tokens = el.className.trim().split(/\s+/);
      if (tokens.includes("active") || tokens.includes("selected")) return true;
    }
    return false;
  }

  const root = opts.root || (typeof document !== "undefined" ? document.body : null);
  if (!root) {
    return { pass: true, summary: {}, violations: [] };
  }

  const nodes = Array.from(root.querySelectorAll("*"));
  const surfaceMap = new Map();
  const radiusSet = new Set();
  const borderSet = new Set();
  const shadowSet = new Set();
  const fontSizeSet = new Set();
  const zeroGlows = [];
  const containerChildrenByParent = new Map();

  const controlBuckets = {
    button: { heights: new Set(), radii: new Set(), samples: [] },
    input: { heights: new Set(), radii: new Set(), samples: [] },
    tab: { heights: new Set(), radii: new Set(), samples: [] },
  };

  const selectionMap = new Map();
  const selectionReflows = [];

  for (const el of nodes) {
    const cs = getComputedStyle(el);
    if (cs.display === "none" || cs.visibility === "hidden" || parseFloat(cs.opacity) === 0) continue;
    const rect = el.getBoundingClientRect();
    if (rect.width <= 0 || rect.height <= 0) continue;

    const r = normalizeRadius(cs.borderRadius);
    if (r > 0 && r < 900) radiusSet.add(r);

    const b = visibleBorder(cs);
    if (b !== "none") borderSet.add(b);

    const sh = cs.boxShadow && cs.boxShadow !== "none" ? cs.boxShadow : "none";
    if (sh !== "none") {
      shadowSet.add(sh);
      if (hasZeroOffsetGlow(sh)) zeroGlows.push(describeNode(el));
    }

    if (cs.fontSize) {
      const fs = Math.round(parseFloat(cs.fontSize));
      if (fs > 0) fontSizeSet.add(fs);
    }

    // 1. Container surface clustering
    const bgVisible = !isTransparent(cs.backgroundColor);
    const tag = (el.tagName || "").toLowerCase();
    const isContainerSized = rect.width >= budgets.minContainerWidth && rect.height >= budgets.minContainerHeight;
    const hasVisualBox = bgVisible || b !== "none" || sh !== "none";
    if (isContainerSized && hasVisualBox) {
      const sig = JSON.stringify({
        bg: bgVisible ? cs.backgroundColor : "transparent",
        border: b,
        radius: r,
        shadow: sh !== "none" ? "shadow" : "none",
      });
      if (!surfaceMap.has(sig)) surfaceMap.set(sig, []);
      surfaceMap.get(sig).push(describeNode(el));

      if (el.parentElement) {
        if (!containerChildrenByParent.has(el.parentElement)) {
          containerChildrenByParent.set(el.parentElement, []);
        }
        containerChildrenByParent.get(el.parentElement).push({
          el,
          desc: describeNode(el),
          sig,
          selected: isSelectedNode(el),
        });
      }
    }

    // 2. Same-role control parity
    const role = el.getAttribute ? el.getAttribute("role") : null;
    let bucketKey = null;
    if (role === "tab") bucketKey = "tab";
    else if (tag === "button" || role === "button") bucketKey = "button";
    else if (
      (tag === "input" && !["checkbox", "radio", "hidden", "range"].includes((el.type || "").toLowerCase())) ||
      tag === "select"
    ) {
      bucketKey = "input";
    }
    if (bucketKey) {
      const h = Math.round(rect.height);
      controlBuckets[bucketKey].heights.add(h);
      controlBuckets[bucketKey].radii.add(r);
      if (controlBuckets[bucketKey].samples.length < budgets.maxSamples) {
        controlBuckets[bucketKey].samples.push({ node: describeNode(el), height: h, radius: r });
      }
    }

    // 3. Selection state runtime diff vs unselected sibling
    if (isSelectedNode(el) && el.parentElement) {
      const siblings = Array.from(el.parentElement.children || []).filter(
        (s) => s !== el && s.tagName === el.tagName && !isSelectedNode(s)
      );
      if (siblings.length > 0) {
        const scs = getComputedStyle(siblings[0]);
        const diffProps = [];
        const checkKeys = [
          "backgroundColor",
          "color",
          "borderTopWidth",
          "borderRightWidth",
          "borderBottomWidth",
          "borderLeftWidth",
          "borderBottomColor",
          "borderLeftColor",
          "boxShadow",
          "outlineStyle",
          "fontWeight",
          "borderRadius",
        ];
        let reflow = false;
        for (const k of checkKeys) {
          if (cs[k] !== scs[k]) {
            diffProps.push(k);
            if (k === "fontWeight" || k.endsWith("Width")) reflow = true;
          }
        }
        if (diffProps.length > 0) {
          const fp = diffProps.sort().join("+");
          if (!selectionMap.has(fp)) selectionMap.set(fp, []);
          selectionMap.get(fp).push(describeNode(el));
          if (reflow) {
            selectionReflows.push({ node: describeNode(el), diffProps });
          }
        }
      }
    }
  }

  // Sibling containment drift: same parent has >=2 non-selected container children with >1 surface signature
  const siblingContainmentDrift = [];
  for (const [parent, kids] of containerChildrenByParent.entries()) {
    const neutral = kids.filter((k) => !k.selected);
    if (neutral.length < 2) continue;
    const sigs = new Set(neutral.map((k) => k.sig));
    if (sigs.size > 1) {
      siblingContainmentDrift.push({
        parent: describeNode(parent),
        distinctSignatures: sigs.size,
        children: neutral.slice(0, budgets.maxSamples).map((k) => ({ node: k.desc, sig: JSON.parse(k.sig) })),
      });
    }
  }

  const violations = [];
  if (surfaceMap.size > budgets.maxSurfaceLevels) {
    violations.push(`surface-clusters: ${surfaceMap.size} > max ${budgets.maxSurfaceLevels}`);
  }
  if (siblingContainmentDrift.length > 0) {
    violations.push(`sibling-containment-drift: ${siblingContainmentDrift.length} parent(s) mix container boundaries`);
  }
  if (radiusSet.size > budgets.maxDistinctRadius) {
    violations.push(`runtime-radius-budget: ${radiusSet.size} (${Array.from(radiusSet).sort((a, b) => a - b).join(",")}) > max ${budgets.maxDistinctRadius}`);
  }
  if (borderSet.size > budgets.maxBorderStyles) {
    violations.push(`runtime-border-budget: ${borderSet.size} > max ${budgets.maxBorderStyles}`);
  }
  if (shadowSet.size > budgets.maxShadowLevels) {
    violations.push(`runtime-shadow-budget: ${shadowSet.size} > max ${budgets.maxShadowLevels}`);
  }
  if (zeroGlows.length > 0) {
    violations.push(`runtime-zero-offset-glow: ${zeroGlows.length} element(s)`);
  }
  if (fontSizeSet.size > budgets.maxFontSizes) {
    violations.push(`runtime-font-size-budget: ${fontSizeSet.size} > max ${budgets.maxFontSizes}`);
  }
  if (selectionMap.size > budgets.maxSelectionGrammars) {
    violations.push(`runtime-selection-grammar: ${selectionMap.size} distinct recipes > max ${budgets.maxSelectionGrammars}`);
  }
  if (selectionReflows.length > 0) {
    violations.push(`runtime-selection-reflow: ${selectionReflows.length} selected element(s) change fontWeight or borderWidth`);
  }

  const controlParity = {};
  for (const [roleKey, data] of Object.entries(controlBuckets)) {
    const heights = Array.from(data.heights).sort((a, b) => a - b);
    const radii = Array.from(data.radii).sort((a, b) => a - b);
    controlParity[roleKey] = { heights, radii, samples: data.samples };
    if (heights.length > budgets.maxControlHeightsPerRole) {
      violations.push(`control-height-drift(${roleKey}): ${heights.length} heights [${heights.join(",")}] > max ${budgets.maxControlHeightsPerRole}`);
    }
    if (radii.length > budgets.maxControlRadiiPerRole) {
      violations.push(`control-radius-drift(${roleKey}): ${radii.length} radii [${radii.join(",")}] > max ${budgets.maxControlRadiiPerRole}`);
    }
  }

  return {
    pass: violations.length === 0,
    summary: {
      surfaceClusters: surfaceMap.size,
      siblingDriftCount: siblingContainmentDrift.length,
      distinctRadii: Array.from(radiusSet).sort((a, b) => a - b),
      distinctBorders: borderSet.size,
      distinctShadows: shadowSet.size,
      distinctFontSizes: Array.from(fontSizeSet).sort((a, b) => a - b),
      selectionRecipes: selectionMap.size,
      selectionReflows: selectionReflows.length,
    },
    surfaceClusters: Array.from(surfaceMap.entries()).map(([sig, items]) => ({
      signature: JSON.parse(sig),
      count: items.length,
      samples: items.slice(0, budgets.maxSamples),
    })),
    siblingContainmentDrift,
    selectionDiffs: Array.from(selectionMap.entries()).map(([recipe, items]) => ({
      recipe,
      count: items.length,
      samples: items.slice(0, budgets.maxSamples),
    })),
    selectionReflows,
    controlParity,
    zeroGlows: zeroGlows.slice(0, budgets.maxSamples),
    violations,
  };
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { auditStyleGrammar };
}
