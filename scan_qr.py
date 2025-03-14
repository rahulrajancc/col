import cv2
import requests
import json

API_URL = "http://localhost:5000/register"

def scan_qr():
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    while True:
        _, frame = cap.read()
        data, bbox, _ = detector.detectAndDecode(frame)

        if data:
            print(f"QR Code detected: {data}")
            payload = {"qr_data": data}
            response = requests.post(API_URL, json=payload)
            
            if response.status_code == 200:
                print("QR code registered successfully!")
            else:
                print("Failed to register QR code.")

            break

        cv2.imshow("QR Code Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_qr()
