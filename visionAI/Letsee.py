import cv2 as cv
from langchain_community.llms import Ollama
import imgCon
import os
from sendTTS import text_to_speech
import threading


def send_tts_thread(call_bakllava):
    text_to_speech(call_bakllava)


def write_image_description(image_num, description):
    file_path = "UnknownObjects\\image_descriptions.txt"
    with open(file_path, "a+") as file:
        file.seek(0, os.SEEK_END)
        if file.tell() > 0:
            file.write("\n\n")  # Add two newline characters to separate each description
        file.write(f"Image {image_num}: {description}")


def main():
    bakllava = Ollama(model="bakllava")
    num = 0
    ubuntu_terminal = 'C:\WINDOWS\system32\wsl.exe -d Ubuntu'
    os.system(
        ubuntu_terminal + 'bash -c "sudo apt-get update; exec bash;ollama pull bakllava; ollama run --gpu bakllava"')

    main_cam = cv.VideoCapture(0)
    if not main_cam.isOpened():
        print('Main camera is not open')

    runBakllava = None
    while True:
        ret, frame = main_cam.read()

        cv.imshow('Main Camera Feed', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

        chat_history = ['CHAT HISTORY']

        if runBakllava and runBakllava.is_alive():
            print('Currently scanning')
        else:
            cv.imwrite(filename=f"UnknownObjects\\UnknownObject_{num}.png", img=frame)
            print('Image created')
            print('Loading Bakllava with image')
            llm_with_image_context = bakllava.bind(images=[imgCon.scanImage(num)])
            print('Questioning model')
            call_bakllava = llm_with_image_context.invoke("You are an AI with a camera and a voice. You are to interact with the user and carry conversation based on the users emotions, you can use previous context to help your conversations. : ")
            runBakllava = threading.Thread(target=send_tts_thread, args=(call_bakllava,))
            runBakllava.start()

            #chat_history.append(write_image_description(num, call_bakllava))

            num += 1

    main_cam.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
