import random

def game():
    new_score=random.randint(1,100)
    return new_score;


score= game();
with open("hi-score.txt","r") as f:
    highscore=int(f.read())

if(score > highscore):
    with open("hi-score.txt","w") as f:
        f.write(str(score))
        print("the new score is: ",score);

