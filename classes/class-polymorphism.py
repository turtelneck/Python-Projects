
# the parent class that subsequent classes are based on.
class Test:
    type = 'Short-answer'
    timer = False
    # a method attached to objects created by instantiations of this class.
    # It prompts users to enter their name, then prints a message.
    def begin(self):
        answer = input('What is your name? \n> ')
        print("\ncorrect answer, you're amazing\n")

# this class uses the properties of `Test` while adding two new properties
# and redefining the .begin() method
class IQ_Test(Test):
    difficulty = 'Extreme'
    deal_breaker = True
    # user is prompted to input text. An unreasonably specific answer gives
    # them one message, and anything else gets them another.
    def begin(self):
        answer = input('What is your favorite song?\n> ')
        if answer == 'Never Gonna Give You Up':
            print('\nyou are a super genius\n')
        else:
            print("\nyou got the answer wrong, but you're still smart\n")

# this class also adds two properties and redefines the .begin() method
class Opinion_Test(Test):
    difficulty = "N/A, it's just your opinion"
    completion_reward =  "We gain a reward by finding out your opinion,\nbut we have nothing to offer in return."
    #user is asked to input text, the result affecting the resultant message
    def begin(self):
        answer = input('What is 2 + 6?\n> ')
        if answer == '8':
            print('\ninteresting opinion you got there, bud\n')
        else:
            print('\ninteresting opinion you got there... pal\n')


first = Test()
first.begin()
second = IQ_Test()
second.begin()
third = Opinion_Test()
third.begin()
