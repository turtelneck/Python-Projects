
# creates a class
class Guy:
    # the following are class properties
    name = 'none'
    relationship_to_user = 'unknown'
    location = 'unknown'

# these two classes are created with the same properties as the first,
# but additional properties 'inches' and 'age' are added
class tallGuy(Guy):
    inches = 72
    age = 'unknown'

class friendlyGuy(Guy):
    mood: 'good'
    age = 'unknown'
