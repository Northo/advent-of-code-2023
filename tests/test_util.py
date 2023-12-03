from advent_of_code.util import get_input_text, Session
from dotenv import dotenv_values

def test_session():
    Session()

def test_get_input_text():
    # NB expects .env file to exitst
    input_text = get_input_text(1)
    assert isinstance(input_text, str)
    print(input_text)
    print(Session())
