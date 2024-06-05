import json
import os
import time
import requests
from matrix_client.client import MatrixClient
from matrix_client.api import MatrixRequestError
import ollama
from dotenv import load_dotenv

load_dotenv()

ollama_host = os.getenv("OLLAMA_HOST")
ollama_client = ollama.Client(host=ollama_host)

CONVERSATION_HISTORY_DIR = 'conversation_history/'

def load_conversation_history(room_id):
    file_path = f"{CONVERSATION_HISTORY_DIR}{room_id}_conversation_history.json"
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_conversation_history(room_id, history):
    file_path = f"{CONVERSATION_HISTORY_DIR}{room_id}_conversation_history.json"
    with open(file_path, 'w') as file:
        json.dump(history, file)

def handle(event):
    room_id = event['room_id']
    sender = event['sender']
    user_input = event['content']['body']

    if sender != client.user_id:
        history = load_conversation_history(room_id)

        history.append({'role': 'user', 'content': user_input})

        try:
            response = ollama_client.chat(model=os.getenv("OLAMA_MODEL_NAME"), messages=history)
            bot_response = response['message']['content']
        except Exception as e:
            bot_response = f"Error: {e}"

        client.api.send_message(room_id, bot_response)

        history.append({'role': 'assistant', 'content': bot_response})

        save_conversation_history(room_id, history)

def get_access_token():
    return os.getenv("ACCESS_TOKEN")

def get_homeserver_url():
    return os.getenv("HOMESERVER_URL")

client = MatrixClient(get_homeserver_url(), token=get_access_token())

def on_message(event):
    if event['type'] == "m.room.message":
        handle(event)

client.add_listener(on_message)

client.start_listener_thread()

if not os.path.exists(CONVERSATION_HISTORY_DIR):
    os.makedirs(CONVERSATION_HISTORY_DIR)

while True:
    time.sleep(10)  # sleep to prevent high CPU usage
