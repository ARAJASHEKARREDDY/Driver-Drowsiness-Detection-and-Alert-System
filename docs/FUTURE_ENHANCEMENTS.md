# Future Enhancements & Roadmap

The following items are proposed future work. They are not included in the current reference implementation unless explicitly stated in the README.

## Detection Improvements
- Add yawn detection and mouth aspect ratio analysis.
- Explore head-pose estimation and prolonged gaze-away detection.
- Add per-user calibration rather than relying on a fixed EAR threshold.
- Evaluate different lighting, camera placements, glasses, and face orientations.
- Investigate temporal models using responsibly collected and consented datasets.

## User Experience
- Add a graphical settings panel for threshold, frame count, and camera selection.
- Add selectable alert tones and configurable cooldowns.
- Add clear camera-permission and troubleshooting guidance.
- Improve on-screen overlays and accessibility.

## Engineering
- Add structured logging and diagnostic reports.
- Expand unit and integration tests.
- Add packaging for supported operating systems.
- Add CI checks for linting and tests.
- Document reproducible evaluation metrics and limitations.

## Responsible Deployment
Any real-world deployment would require rigorous validation, privacy and security review, human-factors testing, fail-safe design, and relevant regulatory/safety approvals. A webcam prototype alone is not suitable for safety-critical use.
