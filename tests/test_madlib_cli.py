from madlib_cli import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_read_template():
    actual = read_template('assets/a_spring_day_template.txt')
    expected = '''
    Today, was an awesome spring day. The sky was blue and clear.
    I went to a cafe near the sea with Sarah.
    Then, I went to the supermarket to do my grocery shopping.
    '''
    assert actual==expected

def test_parse_template():
    actual = parse_template('It was a {Adjective} and {Adjective} {Noun}.')
    expected = "It was a   and    ."
    assert actual==expected 

def test_merge():
    actual = merge('It was a {} and {} {}.', ['rainy', 'windy', 'day'])
    expected = "It was a raing and stormy day."
    assert actual==expected 
