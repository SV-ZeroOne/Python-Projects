import sys
import datetime

print("##############################")
print("Hello World")
print("Welcome to my python program")
print("##############################")
currentDateTime = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
print(currentDateTime)
# Will git update this? 
# Yes it did just had to stage, commit and push
print("##############################")
print()
storyFormat = '''
Once upon a time, in an ancient jungle there lived an {animal} who at {food}.
The End
'''

def tellStory():
    userPicks = dict()
    addPick('animal', userPicks)
    addPick('food', userPicks)
    story = storyFormat.format(**userPicks)
    print(story)

def addPick(cue, dictionary):
    prompt = 'Enter an example for ' + cue + ': '
    response = input(prompt)
    dictionary[cue] = response

tellStory()
input('Press Enter to end the program.')