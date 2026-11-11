# Project Overview

## Problem Statement
Driver fatigue and drowsiness can reduce attention and reaction time. This project demonstrates a camera-based approach to monitoring eye closure and issuing an audible prompt in a controlled environment.

## Objective
Build a modular Python prototype that captures webcam frames, detects eye landmarks, estimates eye openness using Eye Aspect Ratio (EAR), and displays/plays a warning after sustained low EAR.

## Scope
This is a proof-of-concept for education and experimentation. It is not validated for road use and does not make medical or safety-critical decisions.

## Skills Demonstrated
- Python programming and modular code organization
- Computer vision with OpenCV
- Facial landmark processing with MediaPipe
- Geometric feature extraction (Eye Aspect Ratio)
- Real-time video processing
- Threshold-based event detection
- Basic testing, dependency management, Git, and technical documentation

## Core Modules
- `src/app.py`: webcam loop, face landmark processing, display, and alert trigger
- `src/detector.py`: eye landmark selection and EAR calculation
- `src/alerts.py`: best-effort sound alert with cooldown
