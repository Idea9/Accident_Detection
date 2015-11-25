import numpy as np
import cv2

cap = cv2.VideoCapture("http://149.156.199.210:8080/mjpg/video.mjpg")

# easy get video to "cap" variable from 0 -> means local camera
while cap.isOpened():
    ret, frame = cap.read()
    # read() zwraca 2 wartosci, jedna to true dla poprawnie odebranej ramki, druga to sama ramka w postaci macierzy
    print cap.get(4)
    # get wyswietla parametry na temat plik, jest ich 18(w dok/tut), 4 to dla przykladu "width" klatki
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('window', gray)
    #downie pierwszy czlon to po prosu nazwa okna, drugi to frame do wyswietlenia

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()