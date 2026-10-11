# Verification gates

Run these yourself. An agent's report tells you where to look, not what is true.

## Per delivery (each unit an agent reports)

1. **Diff:** read every change (`git diff <base>`), and revert any change that was not requested.
2. **Checks:** run the team's checks plus the integrated checks yourself. They must be green, leave no tracked file modified, and include a negative case.
3. **Visual:** open the captures at full size, then 2x crops of the dense regions: hands and fingers, contact with the ground, edges and seams, text, water or material joints. Look for clipping, floating parts, gaps, stretched textures, z-fighting.
4. **Motion:** record a short clip (5-15 s) of the real behaviour and review it with a video-capable model, using a neutral prompt that does not name the defect you suspect. Extract frames at the reported timestamps and look at them before acting. After a fix, make a new clip.
5. **Performance:** measure on the target device whatever can cost frame time (fps, worst frame, draw calls, memory). A desktop or phone-sized capture is not device performance.

## Before any build reaches the user's device

1. Build from a clean, committed state, with a version name that identifies the commit.
2. **Desktop pass:** launch every entry point (menu item, scene, lab) with the real renderer. Record that it reached its first frame, the error count, and a capture.
3. **Device pass:** install, prove the installed version, then launch every entry point from a fresh app start. Record for each one:
   - that the process is alive;
   - the error count in the logs;
   - the focused window;
   - a capture.

   Prefer a built-in smoke mode, where the app opens each entry itself and logs OK or FAIL, over tapping screen coordinates. If you must tap, measure the positions on a full-resolution screenshot of each menu state.
4. Walk each newly delivered feature by its real UI path, the way the user will.
5. Attach the results table (entry, desktop, device, notes) to your message to the user. Never announce something you have not opened yourself.

## Red flags that mean "not done"

- The feature works only in a sandbox, not in the main product.
- It was proven only by a headless test, a scripted scenario or a single camera angle.
- The device pass was skipped "because the desktop checks are green". Exports drop files and classes that desktop runs still find.
- The same defect has come back after a fix: look for the method or tool gap behind it.
