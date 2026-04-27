from twttr import remove_vowels


def test_lowercase():
    assert remove_vowels("twitter") == "twttr"
    assert remove_vowels("hello") == "hll"


def test_uppercase():
    assert remove_vowels("TWITTER") == "TWTTR"


def test_numbers():
    assert remove_vowels("1234") == "1234"


def test_punctuation():
    assert remove_vowels("hello, world!") == "hll, wrld!"