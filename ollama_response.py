import ollama
import os


def ollamaResponse(modeltype, user_input):
    # Get Llama2
    model = 'llama2'
    ollama.pull(model)

    ubuntuTerminal = 'C:\WINDOWS\system32\wsl.exe -d Ubuntu'
    os.system(ubuntuTerminal + 'bash -c "sudo apt-get update; exec bash; ollama run --gpu llama2;OLLAMA_HOST=127.0.0.1:11435 ollama serve"')

    response = ollama.chat(model=model, messages=[{'role': 'system', 'content': modeltype}, {'role': 'user', 'content': user_input}])

    return response['message']['content']


#print(ollama_response(user_prompt, friendlyModel()))
