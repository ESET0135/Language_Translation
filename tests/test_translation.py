import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from language_mapping import language_codes

# test_translation.py
from language_mapping import language_codes

def test_language_code_mapping():
    assert "French" in language_codes
    assert language_codes["French"] == "fr"
