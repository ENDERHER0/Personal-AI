import ollama
import numpy
import os
import cv2 as cv
from subprocess import run

ubuntuTerminal = 'C:\WINDOWS\system32\wsl.exe -d Ubuntu'
os.system(ubuntuTerminal + 'bash -c "sudo apt-get update; exec bash;ollama pull bakllava')
visionModel = str('bakllava')
imagePrompt = str('What is this?')

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv.imshow('frame', frame)
    num = 0

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here

    if cv.waitKey(1) == ord('c'):
        print("Scanning")

        # Not Saving Images

        if (cv.imwrite(filename="visionAI/UnknownObjects/UnknownObject_" + str(num) + '.png', img=frame)):
            print('Image Created')
            cap.release()
            cv.destroyAllWindows()
        else:
            print('Try again.')
            break

        image = "visionAI/UnknownObjects/UnknownObject_" + str(num) + '.png'
        os.system(
            ubuntuTerminal + 'bash -c "sudo apt-get update; exec bash; ollama run --gpu bakllava; ' + imagePrompt + "; " + image + '"')

        output = os.popen(ubuntuTerminal).readlines()
        print(output)
        num += 1

    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
