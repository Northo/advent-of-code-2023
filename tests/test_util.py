from advent_of_code.util import Session, get_input_text


def test_session():
    Session()


def test_get_input_text():
    # NB expects .env file to exitst
    input_text = get_input_text(1)
    assert isinstance(input_text, str)
    print(input_text)
    print(Session())
