import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# easy get video to "cap" variable from 0 -> means local camera
while(True):
    ret, frame = cap.read()
    # read() zwraca 2 wartosci, jedna to true dla poprawnie odebranej ramki, druga to sama ramka w postaci macierzy

    print cap.get(4)
    # get wyswietla parametry na temat plik, jest ich 18(w dok/tut), 4 to dla przykladu "width" klatki

    cap.set(3, 480)
    cap.set(4, 360)
    # set moze ustawiac te parametry ktore sa w get(), zmiana kazdej klatki na inna to jednak nie najlepszy pomysl toche muli dziada

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # po prostu bierzesz kazdy frame, przekladasz mu kolory i zapisujesz do gray

    cv2.imshow('frame',gray)
    #downie pierwszy czlon to po prosu nazwa okna, drugi to frame do wyswietlenia

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()