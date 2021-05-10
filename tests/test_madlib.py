import pytest
from madlib_cli import __version__
from madlib_cli.madlib_cli import read_template, parse_template, merge, write_madlib

# @pytest.mark.skip
def test_version():
    assert __version__ == '0.1.0'

# @pytest.mark.skip
def test_read_template_returns_stripped_string():
    actual = read_template("assets/dark_and_stormy_night_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected

# @pytest.mark.skip
def test_read_template_returns_stripped_string_2(get_path):
    actual = read_template(get_path)
    expected = """Make Me A Video Game!

I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!

What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find.
"""
    assert actual == expected

@pytest.fixture
def get_path():
    return "assets/make_me_a_video_game_template.txt"

# @pytest.mark.skip
def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ["Adjective", "Adjective", "Noun"]

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts

def test_parse_template_2():
    actual_stripped, actual_parts = parse_template("I the {Adjective} and{Adjective} {A First Name} have {Past Tense Verb}{A First Name}")
    expected_stripped = "I the {} and{} {} have {}{}"
    expected_parts = ['Adjective', 'Adjective', 'A First Name', 'Past Tense Verb', 'A First Name']

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts

# @pytest.fixture
# def get_template():
#     return {"template":"I the {Adjective} and{Adjective} {A First Name} have {Past Tense Verb}{A First Name}",
#     ,"parts": "['Adjective', 'Adjective', 'A First Name', 'Past Tense Verb', 'A First Name']", 
#     "stripped": "I the {} and{} {} have {}{}"}


# @pytest.mark.skip
def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected

# @pytest.mark.skip
def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)

def test_write_madlib():
    path = 'assets/madlib.txt'
    madlib = "It was a dark and stormy night."
    write_madlib(path,madlib)
    expected = madlib
    actual = read_template(path)
    assert expected == actual
