import pyttsx3


def text_to_speech(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties, including the British English voice
    engine.setProperty('voice', 'english_rp')  # For a British English voice
    engine.setProperty('rate', 150)  # You can adjust the speed of speech here

    # Convert text to speech
    engine.say(text)

    # Wait for speech to finish
    engine.runAndWait()


# Test the function
if __name__ == "__main__":
    text_to_speech("Hello, I'm a little British.")
