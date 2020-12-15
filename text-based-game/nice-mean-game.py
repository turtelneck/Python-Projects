#
# Python:   3.9.0
#
# Author:   Rhodri


def start(nice=0,mean=0,name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
        check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game
    """
    # meaning, if we do not already have this user's name,
    # then they are a new player and hwe need to get their name
    if name != "":
        print("\nCool cool.")
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n> ").lower()
        if pick == "n":
            print("\nThestranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger begins to plot your death.")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()
    

def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name):
    if nice > 2:
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    print("\nLooks like you were nice. \nWhich is good, I guess. \nPat yourself on the back or something.")
    again(nice,mean,name)

def lose(nice,mean,name):
    print("\nWow, you're a real jerk, aren't you? \nWell, in the end everyone you were mean to \ncame together to plot your death. \nSo you'll have a lot of time to think \nabout the consequences of your actions \nwhile you haunt them or something.")
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n) \n> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nCan't blame you. I mean, this ain't exactly Mario Odyssey. \n\nSee ya!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO'\n> ")
            
def reset(nice,mean,name):
    nice = 0
    mean = 0
    start(nice,mean,name)












if __name__ == "__main__":
    start()
