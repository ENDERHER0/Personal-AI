Multiple open-source Ollama AI projects
Simple GUI
TTS-based chat system needs Prompt work
Video camera to text-based chat system
Everything is a work in progress.

This is a side project, I am using to learn about AI, file systems, and peripheral manipulation.

Made from my Ollama GUI:

Title: Interactive Conversation with an Artificial Intelligence (AI) Companion using Ollama

This script introduces you to an interactive conversation experience with a friendly AI companion.
This intelligent assistant is designed to understand the context of your conversations, respond appropriately,
and adapt to new topics. It uses advanced technology called artificial intelligence (AI), specifically OpenMined's Ollama model,
along with custom models for grammar correction, text-to-speech conversion, and topic modeling.

Importing Necessary Components:

ollama_response: This library allows us to access the advanced AI capabilities of OpenMined's Ollama model.
getTFS and sendTTS: Custom modules that enable speech recognition using Google Text-to-Speech (TTS) for input and output, respectively.
customModels: A custom module containing various models tailored to our specific conversation needs.
Setting Up the Conversation Environment:

We define several custom models, including friendModel, grammarModel, ttsModel, and topicModel.
These models help us understand user input (friendModel), correct any errors in speech or text (grammarModel),
convert text to spoken words using TTS (ttsModel), and adapt to new conversation topics (topicModel).
An empty list named chat_history is initialized for storing the entire conversation history.
The process_input Function: This function processes user input based on the command given.
For instance, if you say "quit," the program terminates.
If you request a new topic by saying "new topic" followed by your desired topic (e.g., "What can you tell me about space?"),
the current conversation is cleared and replaced with this new topic. In all other cases, your input will be added to chat_history.

The main Function: This function initiates the main loop of our interactive conversation experience.
It checks if there's an existing topic in the chat history; if not, it prompts you for a new topic and clears any previous conversations.
Then, it enters the primary conversation cycle where your input is taken, processed using Ollama models (friendModel and grammarModel),
generated into a response, and converted to spoken words using ttsModel.

Starting the Interactive Conversation: When you run this script, it automatically initiates the main() function,
which starts the conversation loop with your AI companion.
Your companion will engage in a friendly dialogue based on your input while adapting to new topics as needed.

I will try and keep this updated.
