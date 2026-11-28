/**
 * Runtime shadow-clipping audit for rendered DOM trees.
 *
 * Detects visible elements whose outer `box-shadow` extends past a clipping
 * ancestor (`overflow: hidden|clip|auto|scroll`, `clip-path`, or `contain: paint`).
 *
 * Usage:
 *   Pass `auditShadowClipping` into Playwright `page.evaluate(auditShadowClipping)`
 *   or run directly in browser DevTools Console.
 */
function auditShadowClipping(options) {
  const opts = options || {};
  const tolerance = typeof opts.tolerance === "number" ? opts.tolerance : 1;
  const maxItems = typeof opts.maxItems === "number" ? opts.maxItems : 40;
  const clipOverflow = new Set(["hidden", "clip", "auto", "scroll"]);

  function splitLayers(raw) {
    const layers = [];
    let buf = "";
    let depth = 0;
    for (let i = 0; i < raw.length; i += 1) {
      const ch = raw[i];
      if (ch === "(") depth += 1;
      else if (ch === ")") depth = Math.max(0, depth - 1);
      if (ch === "," && depth === 0) {
        layers.push(buf.trim());
        buf = "";
      } else {
        buf += ch;
      }
    }
    if (buf.trim()) layers.push(buf.trim());
    return layers;
  }

  function computeShadowExtent(boxShadow) {
    if (!boxShadow || boxShadow === "none") return null;
    const extent = { top: 0, right: 0, bottom: 0, left: 0 };
    let hasOuter = false;
    for (const layer of splitLayers(boxShadow)) {
      if (/\binset\b/i.test(layer)) continue;
      // Strip color functions like rgb(...)/rgba(...)/oklch(...) before reading px lengths
      const stripped = layer.replace(/[a-z]+\([^)]*\)/gi, " ");
      const nums = stripped.match(/-?\d+(?:\.\d+)?px/g);
      if (!nums || nums.length < 2) continue;
      const ox = parseFloat(nums[0]) || 0;
      const oy = parseFloat(nums[1]) || 0;
      const blur = parseFloat(nums[2]) || 0;
      const spread = parseFloat(nums[3]) || 0;
      const reach = blur + spread;
      if (reach <= 0 && ox === 0 && oy === 0) continue;
      hasOuter = true;
      extent.right = Math.max(extent.right, Math.max(0, ox + reach));
      extent.left = Math.max(extent.left, Math.max(0, -ox + reach));
      extent.bottom = Math.max(extent.bottom, Math.max(0, oy + reach));
      extent.top = Math.max(extent.top, Math.max(0, -oy + reach));
    }
    return hasOuter ? extent : null;
  }

  function describeNode(el) {
    const tag = el.tagName.toLowerCase();
    const id = el.id ? "#" + el.id : "";
    const cls =
      typeof el.className === "string" && el.className.trim()
        ? "." + el.className.trim().split(/\s+/).slice(0, 2).join(".")
        : "";
    return tag + id + cls;
  }

  const root = opts.root || document.body;
  if (!root) return { totalChecked: 0, clippedCount: 0, items: [] };

  const nodes = root.querySelectorAll("*");
  const items = [];
  let totalChecked = 0;

  for (const el of nodes) {
    const cs = getComputedStyle(el);
    if (cs.display === "none" || cs.visibility === "hidden" || parseFloat(cs.opacity) === 0) {
      continue;
    }
    const ext = computeShadowExtent(cs.boxShadow);
    if (!ext) continue;
    const rect = el.getBoundingClientRect();
    if (rect.width <= 0 || rect.height <= 0) continue;
    totalChecked += 1;

    let anc = el.parentElement;
    while (anc && anc !== document.documentElement) {
      const acs = getComputedStyle(anc);
      const clipsX = clipOverflow.has(acs.overflowX) || clipOverflow.has(acs.overflow);
      const clipsY = clipOverflow.has(acs.overflowY) || clipOverflow.has(acs.overflow);
      const clipsAll =
        (acs.clipPath && acs.clipPath !== "none") ||
        (acs.contain && acs.contain.includes("paint"));

      if (clipsX || clipsY || clipsAll) {
        const ar = anc.getBoundingClientRect();
        const cuts = {};
        if (clipsX || clipsAll) {
          const leftCut = ar.left - (rect.left - ext.left);
          const rightCut = rect.right + ext.right - ar.right;
          if (leftCut > tolerance) cuts.left = Math.round(leftCut);
          if (rightCut > tolerance) cuts.right = Math.round(rightCut);
        }
        if (clipsY || clipsAll) {
          const topCut = ar.top - (rect.top - ext.top);
          const bottomCut = rect.bottom + ext.bottom - ar.bottom;
          if (topCut > tolerance) cuts.top = Math.round(topCut);
          if (bottomCut > tolerance) cuts.bottom = Math.round(bottomCut);
        }
        if (Object.keys(cuts).length > 0) {
          if (items.length < maxItems) {
            items.push({
              element: describeNode(el),
              clippedBy: describeNode(anc),
              cuts,
              shadowExtent: ext,
            });
          }
          break;
        }
      }
      anc = anc.parentElement;
    }
  }

  return { totalChecked, clippedCount: items.length, items };
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { auditShadowClipping };
}
