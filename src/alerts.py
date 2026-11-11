"""Cross-platform best-effort alert sound."""
import sys
import threading

class SoundAlert:
    def __init__(self, cooldown_seconds=1.5):
        self.cooldown_seconds = cooldown_seconds
        self._last_played = 0.0
        self._lock = threading.Lock()

    def play(self):
        import time
        with self._lock:
            now = time.monotonic()
            if now - self._last_played < self.cooldown_seconds:
                return
            self._last_played = now
        threading.Thread(target=self._beep, daemon=True).start()

    @staticmethod
    def _beep():
        try:
            if sys.platform.startswith("win"):
                import winsound
                winsound.Beep(1100, 650)
                winsound.Beep(900, 650)
            else:
                # Tkinter's bell is triggered by the UI loop in app.py as a fallback.
                print("\\a", end="", flush=True)
        except Exception:
            print("\\a", end="", flush=True)
