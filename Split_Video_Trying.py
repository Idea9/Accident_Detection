import numpy as np
import cv2

cap = cv2.VideoCapture("video/Pure1.avi")
# easy get video to "cap" variable from 0 -> means local camera

frameNumber = 25*60
i = 0
fileNumber = 0
absoluteFrame = 0
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter("test", fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
while cap.isOpened():
    if cap.cv.empty():
        ret, frame = cap.read()
        # read() zwraca 2 wartosci, jedna to true dla poprawnie odebranej ramki, druga to sama ramka w postaci macierzy

        # set moze ustawiac te parametry ktore sa w get(), zmiana kazdej klatki na inna to jednak nie najlepszy pomysl toche muli dziada
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # po prostu bierzesz kazdy frame, przekladasz mu kolory i zapisujesz do gray
        if i == 0:
            name = 'TestMaterial/Video' + str(fileNumber) + '.avi'
            out = cv2.VideoWriter(name, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

        out.write(frame)
        i += 1

        if i == frameNumber:
            out.release()
            fileNumber += 1
            i = 0

        absoluteFrame += 1
        print absoluteFrame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()