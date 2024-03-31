import pyaudio
from vosk import Model, KaldiRecognizer

def select_microphone():
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        if "Microphone (NVIDIA Broadcast)" in device_info['name']:
            return i
    print("No microphone named 'Microphone (NVIDIA Broadcast)' found. Defaulting to device index 0.")
    return 0

def recognize_speech():
    selected_device_index = select_microphone()

    model = Model(r"C:\Users\brett\Desktop\PythonAI\Personal AI\vosk-model-small-en-us-0.15")
    recognizer = KaldiRecognizer(model, 16000)

    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192, input_device_index=selected_device_index)
    stream.start_stream()

    recognized_text = []

    try:
        print(f"Listening through microphone: {mic.get_device_info_by_index(selected_device_index)['name']}")
        is_speech_started = False
        while True:
            data = stream.read(4096)

            if recognizer.AcceptWaveform(data):
                text = recognizer.Result()
                recognized_text.append(text[14:-3])  # Extract recognized text from the result
                if not is_speech_started and recognized_text[-1].strip():  # Check if speech has started
                    print("Recognized text:", recognized_text)
                    is_speech_started = True
            elif is_speech_started:  # If speech has started and there's a pause in speech
                break
    except KeyboardInterrupt:
        pass
    finally:
        stream.stop_stream()
        stream.close()
        mic.terminate()

    return ' '.join(recognized_text)  # Concatenate recognized text into a single string and return it

if __name__ == "__main__":
    recognized_text = recognize_speech()
    print("Recognized text:", recognized_text)
