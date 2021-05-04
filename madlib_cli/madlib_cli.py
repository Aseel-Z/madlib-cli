def intro():
    welcomeMsg= """Welcome to MadLib Command Line (MADLIB-CLI)!
    Ready for some fun?  Guess the words! :)
    """
    print(welcomeMsg)

intro()

def read_template():
    template = open('assets/a_spring_day_template.txt','r')
    contents = template.read()
    line_contents=template.readlines()
    template.close()
    print(contents)
    print(line_contents)

    for line in line_contents:



def getUserInputs():
    	
Adjective = input("How would you describe a spring day?: ")
Noun1 = input("Enter an adjective: ")
Place1 = input("Enter an adjective: ")
Noun2 = input("Enter an adjective: ")
Name = input("Enter an adjective: ")
Place2 = input("Enter an adjective: ")
Thing = input("Enter an adjective: ")
Activity = input("Enter an adjective: ")

Today, was an {Adjective} spring day. The {Noun1} was blue and clear.
I went to a {Place1} near the {Noun2} with {Name}.
Then, I went to the {Place2} to do my {Thing} {Activity}.


 

 
# # # Ask the user to input a noun
# # noun = input("Enter a noun: ")
 
# # # Replace the blank with the user's input
# # madlib = madlib.replace("blank", noun)
 
# # # Print out the Mad Lib including the user's response
# # print(madlib)

	
# ​string = "This is a string"
 
# string = string.replace("is", "was")
 
# print(string)




