

class Test:
    type = 'Short-answer'
    timer = False

    def begin(self):
        answer = input('What is your name?')
        print("correct answer, you're amazing")


class IQ_Test(Test):
    difficulty = 'Extreme'
    deal_breaker = True

    def begin(self):
        answer = input('What is your favorite song?\n> ')
        if answer == 'Never Gonna Give You Up':
            print('\nyou are a super genius')
        else:
            print("\nyou got the answer wrong, but you're probably pretty smart all the same")


class Opinion_Test(Test):
    difficulty = "N/A, it's just your opinion, man"
    completion_reward =  "By finding out your opinion, we gain a reward.\nBut you won't get anything"

    def begin(self):
        answer = input('What is 2 + 6?\n> ')
        if answer == 8:
            print('\ninteresting opinion you got there, bud')
        else:
            print('\ninteresting opinion you got there... pal')
