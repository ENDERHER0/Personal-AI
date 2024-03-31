import tkinter as tk
import threading
import ollama


# Initialize Ollama model
def init_ollama():
    threading.Thread(target=ollama.pull, args=('llama2',)).start()


# Set up user input and response frames as per your requirements using Tkinter widgets like Entry, Label etc.
def handle_user_input(event=None):
    question = entry1.get()
    entry1.delete(0, tk.END)  # Clear the entry field

    response = ollama.chat(model='llama2', messages=[{'role': 'user', 'content': question}])

    # Clear the old response
    response_text.config(state=tk.NORMAL)
    response_text.delete(1.0, tk.END)

    # Add the new response
    response_text.insert(tk.END, "You: {}\n".format(question))
    response_text.insert(tk.END, "Ollama: {}\n\n".format(response["message"]["content"]))
    response_text.config(state=tk.DISABLED)

    # Scroll back to the top
    response_text.see("1.0")


root = tk.Tk()
root.title("PYOLGPT")
root.iconbitmap("llamopy.ico")
frame1 = tk.Frame(master=root)  # User input frame
frame2 = tk.Frame(master=root)  # Response frame

entry1 = tk.Entry(frame1, width=50)  # User input entry widget
button1 = tk.Button(frame1, text="Submit", command=handle_user_input)
scrollbar = tk.Scrollbar(frame2)
response_text = tk.Text(frame2, wrap=tk.WORD, yscrollcommand=scrollbar.set)

scrollbar.config(command=response_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
response_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

frame1.grid(row=0, column=0, padx=(5, 0), pady=(5, 0))
frame2.grid(row=1, column=0, padx=(5, 0), pady=(5, 0))
entry1.grid(row=0, column=0, padx=(5, 5), sticky="w")
button1.grid(row=0, column=1, sticky="e")

response_text.config(width=60, height=20, state=tk.DISABLED)  # Disable text widget initially
root.geometry("500x400")
root.bind("<Return>", lambda event: (handle_user_input()))
root.mainloop()


init_ollama()  # Start the Ollama script in a separate thread or process if needed.
