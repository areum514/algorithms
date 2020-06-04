voted = {}


def check_vote(name):
    if voted.get(name):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them vote")


check_vote('areum')
check_vote('yeram')
check_vote('yechan')

check_vote('areum')

print(voted)
