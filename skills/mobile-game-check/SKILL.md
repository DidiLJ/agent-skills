---
name: mobile-game-check
description: Final mobile-first checklist for any Godot game or lab unit (reference device: a mid-range Android phone in landscape). Run it before declaring a unit done, before handing a build to a reviewer or the user, and before reporting "it works". Covers touch AND mouse/keyboard input, web export, Android build, phone-sized display and performance budgets, with evidence.
---

# Mobile-first game check

A unit is not done until every section below has evidence. "The check prints OK" is not evidence for touch, display or speed. Report the table at the end, one line per item, with the evidence path or the reason it was skipped.

## 1. Input works on every device
- Every gameplay input goes through Godot input actions. No hard-coded key or button in gameplay code.
- **Events created in code must listen to all devices.** `InputEventMouseButton.new()` (and key/joypad events) default to one device and silently ignore the touch-emulated mouse (device -1). Set `event.device = -1` on every event you register. Audit command, run from the project folder (any hit without `device = -1` nearby is a bug):
  `grep -rn "InputEvent[A-Za-z]*\.new()" scripts --include=*.gd | grep -v "check_\|capture_"`
  (Bug seen twice, in two different prototypes: buttons worked, the scene ignored fingers.)
- The headless check drives **real touch events**: `InputEventScreenTouch` / `InputEventScreenDrag` through `Input.parse_input_event` (single tap, hold-and-drag, two-finger gesture that must NOT trigger the tool). Also one mouse path and one keyboard path. The touch test must fail on the code before the fix.
- HUD buttons and scene taps both tested. A `Control` must not swallow scene touches (`mouse_filter`).
- The on-screen hint matches the last device used (touch wording vs key names read from the action, never typed by hand).

## 2. Web export (WebGL2, the most constrained target)
- Export only to a scratch folder such as `build/web-check/` (never the folder of the shared or release web build). Open it in the Browser pane on your own tab, play the changed feature, read the console: zero errors.
- Known Web traps: audio buses must be declared in `default_bus_layout.tres` (a bus created at runtime is silent), no bus effects on Sample playback, glyphs missing from the font (arrows, check marks), `DisplayServer` calls not implemented on Web, `user://` saves must survive a reload.

## 3. Phone display (example: a mid-range Android phone in landscape, 2400x1080, about 1079x485 logical)
- Real-renderer captures at phone resolution of every view and state you changed (and the smallest target, 900x410 logical), opened at full resolution by you. Check the four edges, safe area, clipped or overlapping text, readability on a small screen.
- Touch targets at least 48 dp with 8 dp spacing, text at least 13 dp, selected state of a tool visible, one line telling a first-time player what to do now.
- Captures must be produced after your last edit; an older capture proves nothing. A contact sheet is an index, not evidence.

## 4. Performance (measured, never assumed)
- Measure with a real renderer (windowed off-screen) the average and the **worst frame** of the changed feature, including its start (first use), not only steady state. Print the numbers.
- No `load()`, scene instantiation, material duplication or first-time shader use during play: preload or load threaded, and warm shaders during a loading or preparation phase.
- Targets on the reference phone: 60 fps average, frame p95 at most 20 ms, no frame above 50 ms during normal actions, physics tick p95 at most 4 ms. Name the debug/release build used.
- Report draw calls and active physics bodies when the feature adds visuals or bodies. Any regression against the previous measurement blocks the unit.
- Android: export only to a scratch folder such as `build/android-check/`, then install it and measure on a real phone. If you cannot do that yourself, say explicitly that phone numbers are not yours.

## 5. Physics: nothing ever floats
- Every object that can lose its support (building piece, furniture, barricade, prop, debris, body, limb) falls under gravity. Prove it for **each asset type** you add or touch: break or remove its supports (all of them, then one side only) in a check, wait for a quiet simulation (counters, not a fixed delay), and assert zero bodies resting above the ground without a body below them (`floating=0`).
- New destructible assets go through the project's shared module path, so support and gravity come by construction; no asset-specific patch.
- Look at it too: one real-renderer capture after breaking the supports. A capture taken mid-fall proves nothing; capture after the scene is quiet. (Seen once: a table top stayed in the air after its legs broke; a mid-flight screenshot missed it, the user saw it.)

## 6. Honesty
- Read the full logs, not only the OK token: `SCRIPT ERROR`, `ERROR`, `Assertion failed`, `leaked`, `still in use`. A check that cannot fail is not a check: show it fails before the fix.
- Flaky check = defect. Drive time by physics frames, not wall time.
- List what is not verified (phone feel, thermal, web on a real GPU) in plain words. Never call it "fluid" or "done on mobile" without a phone measurement.

## Report

| Item | Result | Evidence |
|---|---|---|
| Input: actions, device -1 audit, touch test fails-before/passes-after | | |
| Web export: console clean, feature played | | |
| Display: captures per view/state at phone size, opened | | |
| Performance: avg, worst frame, first use, budgets | | |
| Physics: supports broken per asset type, floating=0, capture after quiet | | |
| Logs read, flakiness, unverified list | | |
