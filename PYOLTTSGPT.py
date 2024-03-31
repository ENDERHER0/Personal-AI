import ollama_response
import getTFS
import sendTTS
import customModels


# Define custom models
friendModel = customModels.friendModel
grammarModel = customModels.grammarModel
ttsModel = customModels.ttsModel
topicModel = customModels.topicModel  # New topic model

# Initialize chat history
chat_history = []


def process_input(command, user_input):
    global chat_history

    if command == "quit":
        sendTTS.text_to_speech("Goodbye!")
        exit()
    elif command == "new topic":
        sendTTS.text_to_speech("What would you like to talk about?")
        new_topic = getTFS.recognize_speech()
        chat_history.clear()  # Clear the chat history
        chat_history.append(new_topic)  # Add the new topic to the chat history
    else:
        # Add user input to chat history
        chat_history.append(user_input)


def main():
    global chat_history

    # Start the conversation loop
    while True:
        # User input
        if len(chat_history) == 0:
            sendTTS.text_to_speech("What would you like to know?")
            user_input = getTFS.recognize_speech()
            topic = ""  # Assign an empty string if no topic is obtained
        else:
            # Get the topic from the AI
            user_input_string = ' '.join(chat_history)
            topic = ollama_response.ollamaResponse(topicModel, user_input_string)

            # Ask the user for the next question
            sendTTS.text_to_speech("What would you like to know next?")
            user_input = getTFS.recognize_speech()

        # Check if the user input is a command
        if user_input.lower() in {"quit", "new topic"}:
            process_input(user_input.lower(), user_input)
        else:
            # Add user input to chat history
            chat_history.append(user_input)

        # Add topic to chat history
        chat_history.append(topic)

        # Join all user inputs into a single string
        user_input_string = ' '.join(chat_history)

        # Call the ollamaResponse function with your custom models and user input as arguments
        grammar_fixed = ollama_response.ollamaResponse(grammarModel, user_input_string)

        # Call the ollamaResponse function with your custom models and user input as arguments
        response = ollama_response.ollamaResponse(friendModel, grammar_fixed)

        tts_output = ollama_response.ollamaResponse(ttsModel, response)

        print(f"Ollama (Friend Model): \n{tts_output}")  # Make TTS model talk
        sendTTS.text_to_speech(f'{tts_output}')

        # Add user input to chat history
        chat_history.append(user_input)


if __name__ == "__main__":
    main()
