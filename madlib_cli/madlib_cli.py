import errno
import os
import re

def intro():
    welcomeMsg= """Welcome to MadLib Command Line (MADLIB-CLI)!
    Ready for some fun?  Guess the words! :)
    """
    print(welcomeMsg)

intro


#Create and test a read_template function that takes in a path to text file and returns a stripped string of the file’s contents
# read_template should raise a FileNotFoundError if path is invalid.

def read_template(path):
    if os.path.isfile():
        template = open(path,'r')
        contents = template.read()
        stripped = contents.strip()
        template.close()
        return stripped
    else:
        raise FileNotFoundError()




#Create and test a parse_template function that takes in a template string and 
# returns a string with language parts removed and a separate list of those language parts.

def parse_template(template):
    empty_string = re.sub(r"\s*{.*}\s*", template)
    language_parts = re.findall(r"\s*{.*}\s*", " ", template)
    return string, language_parts




def getUserInputs():
    Adjective = input("How would you describe a spring day? ")
    Noun1 = input("Enter something that is located up the land?")
    Place1 = input("A place where poeple eat and meet? ")
    Noun2 = input("a wide blue thing?")
    Name = input("a person's name? a female maybe?")
    Place2 = input("a place where people buy stuff? ")
    Thing = input("Something we can't suvive without? ")
    Activity = input(" the act of buying? ")
    return {Adjective, Noun1, Place1, Noun2, Name, Place2, Thing, Activity}

#  Create and test a merge function that takes in a “bare” template and a list of user entered language parts, 
# and returns a string with the language parts inserted into the template
# def merge(empty_template, inputs):
#     for i in inputs:
#         empty_template.format(,inputs[i])
#     return empty_template



# def read_template():
#     template = open('assets/a_spring_day_template.txt','r')
#     contents = template.read()
#     line_contents=template.readlines()
#     for line in 
#     template.close()

#     # print(contents)
#     # print(line_contents)
#     inputs = getUserInputs()
#     print(inputs)
#     for element in inputs:
#         print(element)
#         contents = contents.replace("{element}", element)
#     print(contents)
#     template.close()



 




