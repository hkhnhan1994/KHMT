import tkinter as tk
from tkinter import ttk
import openai
import uuid

# OpenAI API parameters
openai.api_key = "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"
model_name = "text-davinci-003"

# Default parameter values
TROUBLE_DEFAULT = "printer problem"
BRAND_MODEL_DEFAULT = "ABC Printer"
CONNECTION_TYPE_DEFAULT = "over LAN"
OS_DEFAULT = "Windows 10"
SOFTWARE_INSTALLED_DEFAULT = "Printer Software v1.0"
RECENT_CHANGES_DEFAULT = "No recent changes"
INKTONER_STATUS_DEFAULT = "sufficient ink/toner"
ATTEMPTED_DEFAULT = "tried restarting the printer"
WISH_DEFAULT = "printing issue"
TEMPERATURE = 0.7
MAX_TOKENS = 50
DEFAULT_USER = 1234
# Dictionary to store user session IDs and conversations
user_sessions = {}


def start_conversation(user_id=DEFAULT_USER):
    # Generate a unique session ID for the user
    session_id = str(uuid.uuid4())

    # Store the session ID in the user_sessions dictionary
    user_sessions[user_id] = session_id

    # Return the session ID to the user
    return session_id


def get_session_id(user_id):
    # Retrieve the session ID for the user from the user_sessions dictionary
    session_id = user_sessions.get(user_id)

    return session_id


def send_message(user_id, message):
    # Retrieve the session ID for the user
    session_id = user_sessions.get(user_id)

    # Retrieve the conversation history from user_sessions
    conversation = user_sessions.get(session_id, [])

    # Set the initial parameter values in the conversation if it's a new conversation
    if not conversation:
        conversation = [
            {"role": "system", "content": "You are a helpful assistant that provides technical support for printer and scanner problems."},
            {"role": "user", "content": ""},
            {"role": "user", "content": ""},
            {"role": "user", "content": ""},
            {"role": "user", "content": ""},
            {"role": "user", "content": ""},
            {"role": "user", "content": ""},
            {"role": "user", "content": ""},
            {"role": "user", "content": ""},
            {"role": "user", "content": ""},
        ]

        # Set the initial parameter values in the conversation
        conversation[1]["content"] = f"I'm having trouble with {param_entries['Trouble:'].get()}."
        conversation[2]["content"] = f"Printer or Scanner Model: {param_entries['Printer or Scanner Model:'].get()}."
        conversation[3]["content"] = f"Connection Type: {param_entries['Connection Type:'].get()}."
        conversation[4]["content"] = f"Operating System: {param_entries['Operating System:'].get()}."
        conversation[5]["content"] = f"Software installed: {param_entries['Software Installed:'].get()}"
        conversation[6]["content"] = f"Recent Changes or Updates: {param_entries['Recent Changes or Updates:'].get()}"
        conversation[7]["content"] = f"Paper and Ink/Toner Status: {param_entries['Paper and Ink/Toner Status:'].get()}"
        conversation[8]["content"] = f"Steps Taken So Far: {param_entries['Steps Taken So Far:'].get()}"
        conversation[9]["content"] = f"help me troubleshoot and resolve this {param_entries['Wish:'].get()} issue"


    # Append the user's message to the conversation list
    conversation.append({"role": "user", "content": message})
    log_text.insert(tk.END, f"Initial conversation: {conversation}\n")
    # print(f"Initial conversation: {conversation}")
    # Call the OpenAI API to generate a response
    response = openai.Completion.create(
        engine=model_name,
        prompt="conversation",
        top_p=0.9,#  Values closer to 1.0 generate more focused output
        frequency_penalty=0.8,# Higher values (e.g., 2.0) discourage the model from repeating the same tokens.
        presence_penalty=0.6, # Higher values (e.g., 0.6) encourage the model to stay closer to the input context.
        stop=None, # A sequence of tokens at which the model will stop generating further output
        temperature=float(param_entries['Temperature:'].get()),
        max_tokens=int(param_entries['Max Tokens:'].get()),
        n=1,
    )

    # Retrieve and return the assistant's reply
    reply = response.choices[0].message['content']

    # Store the updated conversation history for the user
    user_sessions[session_id] = conversation

    return reply


# GUI setup
root = tk.Tk()
root.title("AI Chatbot")

# Set the window resizable
root.resizable(True, True)
root.pack_propagate(0)

# Create the parameter input frame
param_frame = ttk.LabelFrame(root, text="Parameters")
param_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create the user ID input
user_id_label = ttk.Label(param_frame, text="User ID:")
user_id_label.pack()
user_id_input = ttk.Entry(param_frame)
user_id_input.insert(tk.END, DEFAULT_USER)
user_id_input.pack()

# Create the adjustable parameters
parameters = [
    ("Trouble:", TROUBLE_DEFAULT),
    ("Printer or Scanner Model:", BRAND_MODEL_DEFAULT),
    ("Connection Type:", CONNECTION_TYPE_DEFAULT),
    ("Operating System:", OS_DEFAULT),
    ("Software Installed:", SOFTWARE_INSTALLED_DEFAULT),
    ("Recent Changes or Updates:", RECENT_CHANGES_DEFAULT),
    ("Paper and Ink/Toner Status:", INKTONER_STATUS_DEFAULT),
    ("Steps Taken So Far:", ATTEMPTED_DEFAULT),
    ("Temperature:", TEMPERATURE),
    ("Wish:", WISH_DEFAULT),
    ("Max Tokens:", MAX_TOKENS),
    ("Temperature:", TEMPERATURE),
]

param_entries = {}
for i, (param_name, default_value) in enumerate(parameters):
    label = ttk.Label(param_frame, text=param_name)
    label.pack()
    entry = ttk.Entry(param_frame)
    entry.insert(tk.END, default_value)
    entry.pack()
    param_entries[param_name] = entry

# Create the log box
log_frame = ttk.LabelFrame(root, text="Log")
log_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

log_text = tk.Text(log_frame, height=10, width=50)
log_text.pack(fill=tk.BOTH, expand=True)

# Create the assistant reply and user message frame
message_frame = ttk.LabelFrame(root, text="Assistant Reply and User Message")
message_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create the assistant reply box
output_label = ttk.Label(message_frame, text="Assistant Reply:")
output_label.pack()
output_text = tk.Text(message_frame, height=10, width=50)
output_text.pack(fill=tk.BOTH, expand=True)

# Create the user message box
user_message_label = ttk.Label(message_frame, text="User Message:")
user_message_label.pack()
user_message_input = tk.Text(message_frame, height=10, width=50)
user_message_input.pack(fill=tk.BOTH, expand=True)


# Rest of the code...



def start_conversation_gui():
    # Retrieve the user ID from the input field
    user_id = user_id_input.get()

    # Start the conversation and get the session ID
    session_id = start_conversation(user_id)

    # Display the session ID in the log box
    log_text.insert(tk.END, f"Conversation started for User ID: {user_id} (Session ID: {session_id})\n")

start_button = ttk.Button(root, text="Start Conversation", command=start_conversation_gui)
start_button.pack(pady=10)

def send_message_gui():
    # Retrieve the user ID from the input field
    user_id = user_id_input.get()

    # Retrieve the user's message from the input box
    user_message = user_message_input.get("1.0", tk.END).strip()

    # Send the message and get the assistant's reply
    assistant_reply = send_message(user_id, user_message)

    # Display the assistant's reply in the output box
    output_text.insert(tk.END, assistant_reply + "\n")

    # Clear the user message input box
    user_message_input.delete("1.0", tk.END)

# Function to resize the window to fit the content
def resize_window():
    root.update()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
send_button = ttk.Button(root, text="Send", command=send_message_gui)
send_button.pack()

# Call the resize_window function after the GUI is idle
root.after(0, resize_window)
root.mainloop()
