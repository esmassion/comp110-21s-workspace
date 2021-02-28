"""Covert Operations Program."""

__author__ = "730189396"


from random import randint

player: str
points: int

ALIVE_EMOJI: str = "\U0001F624"
DEAD_EMOJI: str = "\U0001F480"


def main() -> None:
    """Your Spy Mission begins."""
    greet()
    global points
    points = 0
    agency: str = input("What is your agency IMF/MI6/CIA - ")
    while agency != "CIA":
        if agency == "IMF":
            print("Welcome Back Special Agent.")
            points += 3
            mission_impossible()
        else: 
            if agency == "MI6":
                points += 3
                print("M will brief you at HQ.")
                print(f"You have successfully completed the mission and earned {bond(points)} Special Agent Points.")
        agency = input("What is your agency IMF/MI6/CIA - ")
    if agency == "CIA":
        points += 1
        print("Jesus Christ it's Jason Bourne. You can have 1 additional pity Special Agent Point.")
    print(f"Congratulations Special Agent {player} you earned a total of {points} Special Agent Point(s).")


def greet() -> None:
    """Greeting the player."""
    global player
    player = input("What is your codename: ")
    print(f"I've heard a lot about you {player}.")


def mission_impossible() -> None:
    """Another impossible mission."""
    global points
    print("The target will be at the Sydney Opera house tonight.")
    entry: str = input("How do you want to sneak in: fake face/janitorial staff/hot date - ")
    if entry == "fake face":
        points += 3
        print("You will be impersonating Ambassador Culvahouse.")
    else:
        if entry == "janitorial staff":
            points += 2
            print("Here is your bucket and mop.")
        else:
            points += 1
            print("lame.")
    d_o_a: str = input("Will you bring in the target dead or alive: ")
    if d_o_a == "alive":
        points += 2
        print(f"Alright, let's see what intel we can get from them {ALIVE_EMOJI}.")
    else:
        points += 1
        print(f"Only if they try to run can you terminate the target {DEAD_EMOJI}.")
    escape: str = input("How do you want to get away? roof extraction/pull fire alarm: ")
    if escape == "roof extraction":
        points += 2
        print(f"{player}, you will have 3 minutes to get to the roof. Helicopter will be waiting")
    else:
        points += 1
        print("Don't forget to shout FIRE!!")
    print(f"This is your mission should you choose to accept it you will earn {points} Special Agent Points.")


def bond(x: int) -> int:
    """James Bond adventure."""
    oo_number: str = "00" + str(randint(1, 9))
    print(f"Welcome back {oo_number}. Glad to see you in one piece after Nairobi.")
    global points
    bond_points: int = points
    broken_hearts: int = int(input("How many hearts will you break during the mission: "))
    if broken_hearts >= 3:
        bond_points += 3
        print(f"Yup, that sounds like {player}")
    else:
        if broken_hearts == 2:
            bond_points += 2
            print(f"{player}, why can you never just pick 1 and settle down?")
        else:
            if broken_hearts == 1:
                bond_points += 1
                print(f"{player} is off their game.")
            else:
                bond_points += 0
                print(f"You okay {player}? That doesn't like you.")
    cars: int = int(input("How many multi-million dollar cars are you going to wreck: "))
    if cars >= 3:
        bond_points += 0
        print(f"That's past your limit, {oo_number}. The damages are coming out of your check.")
    else:
        bond_points += 2
        print("Yeah yeah alright. The keys are in your locker.")
    print("The asset is hidden in Buckingham Palace.")
    threat_level: int = int(input(f"{oo_number}, what is the asset's threat level 1-10: "))
    if threat_level > 7:
        bond_points += threat_level
        print(f"Take the shot {DEAD_EMOJI}.")
    else:
        bond_points += threat_level
        print(f"Bring the asset back to HQ for questioning {ALIVE_EMOJI}.")
    points = bond_points + points
    return points


if __name__ == "__main__":
    main()