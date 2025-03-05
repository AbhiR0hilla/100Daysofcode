from game_data import data,art,vs
import random

# def display(diff):

print(art)
accb=random.choice(data)

score=0
resume=True
while resume:
    acca=accb
    accb=random.choice(data) #assigned the data dict value
    counta = acca["follower_count"]
    countb = accb["follower_count"]
    def format_data(account):
        acca_name=account["name"]
        acca_desc=account["description"]
        acca_co=account["country"]
        return f"{acca_name},a {acca_desc} from {acca_co}"
    def calculate(choice,counta,countb):    #calulates who higher follower and returns boolean
        if counta>countb:
            return choice=="a"
        else:
            return choice=="b"
    print(f"Compare {format_data(acca)}.")
    print(vs)
    print(f"Against {format_data(accb)}.")

    choice=input("who has more followers A or B: ").lower()
    print("\n"*20)
    print(art)

    iscorrect=calculate(choice,counta,countb)
    if iscorrect:
        print("you're right")
        score+=1
        print(f"current score : {score}")
    else:
        print(f"you're wrong, final score is: {score}")
        resume=False



