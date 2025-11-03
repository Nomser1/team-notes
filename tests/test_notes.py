import os
import json
from app import notes

def test_add_and_list_notes(tmp_path):
    test_file = tmp_path / "notes.json"
    notes.DATA_FILE = str(test_file)

    notes.add_note("Test", "Contenido de prueba")
    result = notes.list_notes()

    assert len(result) == 1
    assert result[0]["title"] == "Test"
    assert result[0]["content"] == "Contenido de prueba"