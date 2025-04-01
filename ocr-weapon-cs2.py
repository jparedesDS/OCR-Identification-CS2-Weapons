import cv2
import numpy as np
import pytesseract
import mss
import time

# Lista de palabras clave
keywords = ["AK-47", "M4A1-S", "M4A1", "AWP", "FAMAS", "Galil", "Desert Eagle", "USP-S", "Glock-18"]


def process_frame(frame):
    """Preprocesa la imagen para mejorar la detección de texto."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)
    resized = cv2.resize(enhanced, (0, 0), fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    return resized


def detect_text(frame):
    """Aplica OCR a la imagen y devuelve las palabras clave detectadas."""
    text = pytesseract.image_to_string(frame, config="--psm 6")
    detected_keywords = [word for word in keywords if word in text]
    return text, detected_keywords


# Configuración de captura de pantalla
with mss.mss() as sct:
    monitor = sct.monitors[1]  # Captura pantalla principal

    while True:
        screenshot = sct.grab(monitor)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        # Definir ROI (parte inferior derecha)
        h, w, _ = frame.shape
        roi = frame[int(h * 0.75):h, int(w * 0.91):w]

        # Procesar la imagen y aplicar OCR
        processed_frame = process_frame(roi)
        text, detected_keywords = detect_text(processed_frame)

        # Mostrar resultados en pantalla
        cv2.imshow("ROI", processed_frame)
        print("Texto detectado:", text)
        print("Palabras clave detectadas:", detected_keywords)

        if cv2.waitKey(1) & 0xFF == ord('z'):
            break

    cv2.destroyAllWindows()
