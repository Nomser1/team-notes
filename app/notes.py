import json
import os

DATA_FILE = "data/notes.json"

def load_notes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_notes(notes):
    with open(DATA_FILE, "w") as f:
        json.dump(notes, f, indent=2)

def add_note(title, content):
    notes = load_notes()
    notes.append({"title": title, "content": content})
    save_notes(notes)

def list_notes():
    notes = load_notes()
    return notes 
