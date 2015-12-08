import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (int(cap.get(3)),int(cap.get(4))))

# easy get video to "cap" varqiable from 0 -> means local camera
while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        # read() zwraca 2 wartosci, jedna to true dla poprawnie odebranej ramki, druga to sama ramka w postaci macierzy
        print cap.get(4)
        # get wyswietla parametry na temat plik, jest ich 18(w dok/tut), 4 to dla przykladu "width" klatki
        out.write(frame)
        cv2.imshow('window', frame)
        #downie pierwszy czlon to po prosu nazwa okna, drugi to frame do wyswietlenia

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# When everything done, release the capture
out.release()
cap.release()
cv2.destroyAllWindows()