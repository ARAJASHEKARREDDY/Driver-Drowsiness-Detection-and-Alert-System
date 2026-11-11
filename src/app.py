"""DriverSafe: webcam-based drowsiness demo using MediaPipe Face Mesh."""
import argparse
import os
import cv2
import mediapipe as mp
from detector import average_eye_ear
from alerts import SoundAlert

def parse_args():
    parser = argparse.ArgumentParser(description="Webcam-based driver drowsiness detection demo")
    parser.add_argument("--camera", type=int, default=int(os.getenv("CAMERA_INDEX", "0")), help="Webcam device index")
    parser.add_argument("--threshold", type=float, default=float(os.getenv("EAR_THRESHOLD", "0.21")), help="EAR threshold; tune for your camera")
    parser.add_argument("--frames", type=int, default=int(os.getenv("CONSECUTIVE_FRAMES", "18")), help="Consecutive low-EAR frames before alert")
    parser.add_argument("--no-mirror", action="store_true", help="Do not mirror the webcam preview")
    return parser.parse_args()

def main():
    args = parse_args()
    if args.frames < 1:
        raise SystemExit("--frames must be at least 1")
    cap = cv2.VideoCapture(args.camera)
    if not cap.isOpened():
        raise SystemExit(f"Could not open camera index {args.camera}. Check permissions or try --camera 1.")

    face_mesh = mp.solutions.face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )
    sound = SoundAlert()
    closed_frames = 0
    status = "NO FACE"
    color = (0, 200, 255)
    print("DriverSafe running. Press Q in the video window to quit.")

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                print("Unable to read a frame from the webcam.")
                break
            if not args.no_mirror:
                frame = cv2.flip(frame, 1)
            height, width = frame.shape[:2]
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = face_mesh.process(rgb)

            if result.multi_face_landmarks:
                face = result.multi_face_landmarks[0]
                ear = average_eye_ear(face.landmark, width, height)
                if ear < args.threshold:
                    closed_frames += 1
                else:
                    closed_frames = 0

                if closed_frames >= args.frames:
                    status, color = "DROWSINESS ALERT", (0, 0, 255)
                    sound.play()
                else:
                    status, color = "ALERT / AWAKE", (0, 180, 0)

                cv2.putText(frame, f"EAR: {ear:.3f}", (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
            else:
                closed_frames = 0
                status, color = "NO FACE DETECTED", (0, 200, 255)

            cv2.rectangle(frame, (10, 55), (width-10, 105), color, -1)
            cv2.putText(frame, status, (22, 88), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
            cv2.putText(frame, "Q: quit | Demo only - do not use as a safety device", (15, height-18),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.48, (255,255,255), 1)
            cv2.imshow("DriverSafe - Drowsiness Detection", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        face_mesh.close()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
