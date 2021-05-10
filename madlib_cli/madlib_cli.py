import re
import os

def welcome():
    welcomeMsg= """Welcome to MadLib Command Line (MADLIB-CLI)!
    Ready for some fun?  Enter the words! :)
    """
    print(welcomeMsg)

def read_template(path):
    if os.path.isfile(path):
        with open(path,'r') as file_template:
            file_template = file_template.read()
        return file_template
     
    else:
        raise FileNotFoundError()



def parse_template(template):
    pattern = r"{(.*?)}"
    # pattern = r"\s*{.*}\s*"
    empty_string = re.sub(pattern, "{}", template)
    language_parts = re.findall(pattern, template)
    return empty_string, language_parts


def get_user_input(language_parts):
    return [input(f"Enter a {part}: ") for part in language_parts]

def merge(empty_string, inputs):
    madlib = empty_string.format(*inputs)
    print(madlib)
    return madlib

def write_madlib(path, madlib):
    with open(path,'w') as filled:
        filled.write(madlib)


if __name__ == '__main__':
    path = 'assets/make_me_a_video_game_template.txt'
    template = read_template(path)
    empty_string, language_parts = parse_template(template)
    print(empty_string,"\n",language_parts)
    inputs = get_user_input(language_parts)
    madlib = merge(empty_string, inputs)
    write_madlib('assets/madlib.txt', madlib)











 




