import ollama
import os
import SystemPrompts




def ollamaResponse(sysPrompt, user_input):
    # Get Llama2 -- DO NOT CHANGE --
    model = 'mistral'
    ollama.pull(model)

    # -------------------------------

    # Launch Ollama Server -- DO NOT CHANGE --
    ubuntuTerminal = 'C:\WINDOWS\system32\wsl.exe -d Ubuntu'
    os.system(
        ubuntuTerminal + 'bash -c "sudo apt-get update; exec bash; ollama run --gpu mistral;OLLAMA_HOST=127.0.0.1:11435 ollama serve"')
    # ----------------------------------------

    # Connect to Ollama server and ask for a response -- DO NOT CHANGE --
    response = ollama.chat(model=model,
                           messages=[{'role': 'system', 'content': sysPrompt}, {'role': 'user', 'content': user_input}])
    # -------------------------------------------------------------------

    # return Ollama response to function --
    return response['message']['content']
    # -------------------------------------


# SYSTEM INFO


print(ollamaResponse(SystemPrompts.systemMainPrompt, SystemPrompts.mainCode + 'USER: Modify your script. USER: From your main.py script add pyttsx3 to give yourself the ability to text to speech your output to the user.'))


# Have the ai modify main somehow.

