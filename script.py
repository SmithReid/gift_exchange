from random import randint

givers = {"Lena": None, 
        "Reid": "Ashlye",
        "Ashlye": "Reid", 
        "Max": "Karley", 
        "Karley": "Max", 
        "Claire": "Jared",
        "Jared": "Claire", 
        "Nick": "Emily", 
        "Emily": "Nick", 
        "Chris": None
        }

if __name__ == "__main__":
    final = {}
    receivers = givers.copy()
    list_givers = list(givers.keys())
    for giver in list_givers:
        receiver = list(receivers.keys())[randint(0, len(receivers.keys()) - 1)]
        while receiver == givers[giver] or receiver == giver: 
            receiver = list(receivers.keys())[randint(0, len(receivers.keys()) - 1)]
        final[giver] = receiver
        receivers.pop(receiver)

    print("final: " + final)

    print(len(set(final.keys())) == len(set(final.values())))