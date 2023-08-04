from helloworld.app import greeting


def test_greeting_returns_name_if_name_is_given():
    assert "test_name" in greeting("test_name")


def test_greeting_returns_generic_msg_if_name_not_given():
    assert greeting() == "Hello, stranger"


def test_greeting_returns_secret_response_on_23():
    assert greeting("23") == "Illuminaty"
