# Agent State Directory

This directory contains persistent state files for workflow agents to maintain work progress across context compressions and session boundaries.

## Purpose

State files record **current facts, frozen decisions, progress, evidence, pending items, and next actions** — not conversation history.

## State Files

- **`product.md`** - Product Designer's work state (product core, confirmed rules, pending questions)
- **`architecture.md`** - Chief Architect's work state (requirement decisions, roadmap, current stage)
- **`blueprint.md`** - Construction Blueprint's planning state (task graph, verified facts, planning gaps)
- **`construction.md`** - Construction Agent's work progress (completed tasks, test results, next steps)
- **`verification.md`** - Stage Verifier's verification state (frozen finding set, resolution status)

## Usage

Each agent:
1. **Reads** its state file at the start of every session
2. **Updates** the state file immediately after confirming key decisions or completing work units
3. **Appends** a timestamp to the Session Log when starting a new session
4. **Refreshes** the state file before context compression or session handoff

## State File Structure

Each state file contains:
- **Current State** section (top) - continuously updated current facts
- **Session Log** section (bottom) - append-only chronological session markers

## Principles

- State files express "current truth", not accumulated chat logs
- When new decisions replace old ones, update the old records
- Only write user-confirmed conclusions, not agent suggestions
- State files enable accurate recovery after context compression
