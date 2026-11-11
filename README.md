# 🚗 Driver Drowsiness Detection and Alert System

### Real-Time Driver Monitoring Using Computer Vision and Deep Learning-Based Facial Landmark Detection

## 📌 Project Overview

The **Driver Drowsiness Detection and Alert System** is a real-time computer vision application developed using Python to identify signs of driver fatigue and drowsiness through webcam monitoring.

Driver fatigue is one of the major contributing factors to road accidents. This project aims to improve road safety by continuously monitoring the driver's eye movements and detecting prolonged eye closure.

The system uses **OpenCV** for real-time video frame processing and **MediaPipe Face Mesh** to identify facial landmarks around the eyes. By calculating the **Eye Aspect Ratio (EAR)**, the application determines whether the driver's eyes are open or closed. If the eye closure condition persists beyond a predefined number of consecutive frames, the system identifies potential drowsiness and triggers an audio alert to warn the driver.

The application provides continuous monitoring with visual status indicators and sound-based warnings.

## 🎯 Project Objectives

- Detect driver drowsiness in real time using webcam input.
- Identify facial landmarks and monitor eye movements.
- Calculate the Eye Aspect Ratio (EAR) to determine eye closure.
- Detect prolonged eye closure using a predefined threshold.
- Generate an audio alert when drowsiness is detected.
- Improve driver awareness and contribute to road safety.

## ✨ Key Features

- **Real-Time Webcam Monitoring:** Captures and processes live video frames.
- **Facial Landmark Detection:** Uses MediaPipe Face Mesh to identify facial and eye landmarks.
- **Eye Aspect Ratio Calculation:** Measures eye openness using facial landmark coordinates.
- **Drowsiness Detection:** Identifies prolonged eye closure using EAR and frame-count thresholds.
- **Audio Alert System:** Plays an audible warning when drowsiness is detected.
- **Visual Status Monitoring:** Displays normal and drowsiness warning indicators.
- **Continuous Detection:** Repeatedly monitors the driver's eye movements during application execution.

## ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenCV | Webcam access and image processing |
| MediaPipe | Facial landmark and eye detection |
| NumPy | Numerical and coordinate calculations |
| Pygame / Audio Library | Sound alert generation |

## 🔄 System Workflow

1. **Start Application:** Initialize the drowsiness detection system.
2. **Capture Webcam Frames:** Access the webcam and capture live video.
3. **Detect Face and Eye Landmarks:** Identify facial landmarks using MediaPipe Face Mesh.
4. **Calculate EAR:** Calculate the Eye Aspect Ratio from the detected eye coordinates.
5. **Evaluate Threshold:** Compare the EAR value against a predefined threshold for consecutive frames.
6. **Determine Driver Status:**
   - Normal: Eyes remain sufficiently open.
   - Drowsy: Eye closure persists beyond the configured frame threshold.
7. **Trigger Alert:** Display a warning and play an audio alert when drowsiness is detected.

## 🏗️ System Architecture

The application follows a modular computer vision pipeline:

**Webcam Input → OpenCV Frame Processing → MediaPipe Face Mesh → Eye Aspect Ratio Calculation → Threshold Evaluation → Visual Warning & Audio Alert**

## 📐 Eye Aspect Ratio (EAR)

The Eye Aspect Ratio is a mathematical measure used to estimate whether the eyes are open or closed.

It is calculated using the vertical and horizontal distances between specific eye landmarks.

EAR is calculated as:

EAR = (||P2-P6|| + ||P3-P5||) / (2 × ||P1-P4||)

Where:
- P1 and P4 represent horizontal eye landmarks.
- P2, P3, P5, and P6 represent vertical eye landmarks.

A lower EAR value generally indicates that the eyes are closing. When the EAR remains below the configured threshold for a predefined number of consecutive frames, the system triggers a drowsiness warning.

## 🌍 Real-World Applications

- Driver fatigue monitoring systems.
- Road safety and accident prevention solutions.
- Intelligent transportation systems.
- Automotive driver assistance applications.
- Computer vision-based human monitoring systems.

## 🚀 Expected Outcome

The system continuously monitors the driver's eyes through a webcam, identifies prolonged eye closure, and generates an audio warning to alert the driver.

It demonstrates how computer vision and facial landmark detection can be applied to develop practical driver safety solutions.

## 🔮 Future Enhancements

- Integrate yawning detection.
- Implement head-pose estimation.
- Add advanced machine learning-based fatigue classification.
- Develop a mobile application for driver monitoring.
- Integrate GPS-based emergency notification.
- Extend compatibility with embedded systems such as Raspberry Pi.

## ⚠️ Disclaimer

This project is developed for educational and demonstration purposes. It is a prototype and should not be considered a replacement for certified automotive safety systems or responsible driving practices.

## 👨‍💻 Project Category

**Domain:** Artificial Intelligence / Computer Vision  
**Project Type:** Real-Time Detection System  
**Input:** Live Webcam  
**Output:** Visual Warning and Audio Alert  
**Programming Language:** Python

<img width="1710" height="867" alt="system-architecture" src="https://github.com/user-attachments/assets/95e0da01-8dd7-4f5f-961f-a361bfc20e56" />
<img width="1726" height="867" alt="detection-workflow" src="https://github.com/user-attachments/assets/741cfbeb-53b7-41d0-9938-f071fe0d06f8" />
<img width="2299" height="1299" alt="LhyeGtoGBuRSVpq3cPiLzZkGevosFkpHy2kbhSk0bzU6zXq9RlmPpoLhqQ9Rke9TKfJK4NCybUYTrVSUfBTHfh_c7iBVQZ6tYRKItU_iEoSpXPrgvaodAiZCI68gq8cS8A0LBDteiQ9m2vDbImFJhP5_921kCo3isqCz_38tcGtUwbRS50FFtmsc04PLKQD_" src="https://github.com/user-attachments/assets/b0f99201-7b42-49c0-80d4-a1f1bd6855e2" />




