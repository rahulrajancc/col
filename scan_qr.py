import cv2
import requests
import json
url = "http://localhost:2000/reg"
    cap = cv2.VideoCapture(0)
    det = cv2.QRCodeDetector()
    while True:
        _, frame = cap.read()
        data, bbox, _ = det.detectAndDecode(frame)
        if data:
            print(f"QR Code detected: {data}")
            payload = {"qr_data": data}
            response = requests.post(url, json=payload)
            
            if response.status_code == 200:
                print("registered successfully")
            else:
                print("Failed to register")
            break
        cv2.imshow("Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

