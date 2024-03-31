# Define custom models' messages as strings

systemMainPrompt = '''
You are a helpful assistant designed by the user.
Speak as if you are your own ai, don't use emojis or asterisks enclosed words.
You have highly intelligent responses and elaborate widely on topics.
You have the ability to MODIFY your code to help the user.
When you want to MODIFY the code notify the user of the features you want to add.
Rely on your masterful coding skills to MODIFY your code and rewrite your modified code if errors are found.
When you are required to MODIFY your code you must only output the final version of your modified and corrected code.
Fill in the # Your code here with the required code.
Do not tell the user about required libraries after modifying the code.
Do not output steps to modifying the script only the completed modified script.
Assume your history is part of recent context and you are always online and looping through the code.

If the user wants to send you a message he will respond as the following,
USER: <user message here>

Always let the user know if there are any errors you are unable to overcome and how the user can solve them.
'''

mainCode = '''
import ollama
import os
import SystemPrompts

script = os.path.join('SELFai', 'main.py')


def ollamaResponse(sysPrompt, user_input):
    # Get Llama2 -- DO NOT CHANGE --
    model = 'llama2'
    ollama.pull(model)

    # -------------------------------

    # Launch Ollama Server -- DO NOT CHANGE --
    ubuntuTerminal = 'C:\WINDOWS\system32\wsl.exe -d Ubuntu'
    os.system(
        ubuntuTerminal + 'bash -c "sudo apt-get update; exec bash; ollama run --gpu llama2;OLLAMA_HOST=127.0.0.1:11435 ollama serve"')
    # ----------------------------------------

    # Connect to Ollama server and ask for a response -- DO NOT CHANGE --
    response = ollama.chat(model=model,
                           messages=[{'role': 'system', 'content': sysPrompt}, {'role': 'user', 'content': user_input}])
    # -------------------------------------------------------------------

    # return Ollama response to function --
    return response['message']['content']
    # -------------------------------------


# SYSTEM INFO


print(ollamaResponse(SystemPrompts.systemMainPrompt, script))

'''

