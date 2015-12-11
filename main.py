import cv2


def showVideoPart(filename, startFrame, endFrame):

    cap = cv2.VideoCapture("video/Man_in_background.avi")

    if endFrame <= startFrame:
        print "bledna liczba ramek"
    if endFrame > cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
        print "Na pewno to Video, nie ma tylu ramek"

    startFrame = 100
    endFrame = 200
    frameNumber = 0
    while cap.isOpened():
        frameNumber += 1
        ret, frame = cap.read()

        if startFrame < frameNumber < endFrame:
            cv2.imshow('window', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print "naliczylo ramek: ", frameNumber
    cap.release()
    cv2.destroyAllWindows()
