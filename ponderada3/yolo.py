from ultralytics import YOLO
import cv2

#ativa a webcam, tive problemas para ativar usando o terminal do vscode ou do ubuntu, so consegui usando cmd
web_cam = cv2.VideoCapture(0)
model = YOLO("best.pt")

while True:
    _, frame = web_cam.read()
    # usa o modelo
    result = model.predict(frame, conf=0.6)

    cv2.imshow("results", result[0].plot())
    # se apertar q, para
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# para a câmera    
web_cam.release()

cv2.destroyAllWindows()