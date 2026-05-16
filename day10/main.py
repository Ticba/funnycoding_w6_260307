hearts = 5
scene = "start"

scenes = {
    "start":{
        "look": "forest",    # "cmd": next state(scene)
        "look": "forest",
    },
    "forest":{
        "look": "forest",
    }
}

print("=== The Lost Crown ===")
print("You are searching for a lost crown hidden in an ancient kingdom.")
print("Type commands to move through the story.")
print("You start with 5 hearts.")
print("If you type something wrong, you lose 1 heart.")

while hearts > 0:
    print("\n--------------------")
    print("Hearts:", "♥ " * hearts)

    if scene == "start":
        print("\nYou wake up beside an old stone road.")
        print("The sky is dark, and the wind is cold.")
        print("A dark forest stands in front of you.")
        print("You feel like something is calling you from far away.")
        print("Maybe you should look around, run forward, or sleep here.")

        cmd = input("What will you do? ").lower()

        if cmd == "look":
            print("\nYou look around and notice footprints leading into the forest.")
            scene = scenes["start"]["look"]
        elif cmd == "run":
            print("\nYou run into the forest without looking back.")
            scene = "forest"
        elif cmd == "sleep":
            print("\nYou fall asleep beside the road.")
            scene = "bad ending"
        else:
            hearts -= 1
            print("\nThat command does not work.")
            print("Hint: Type look, run, or sleep.")

    elif scene == "forest":
        print("\nYou enter the forest.")
        print("Tall trees block the sunlight.")
        print("You hear something moving in the bushes.")
        print("A dark cave lies to the north.")
        print("A rocky hill nearby looks possible to climb.")
        print("You can also go back to the stone road.")

        cmd = input("What will you do? ").lower()

        if cmd == "north":
            print("\nYou walk north toward the dark cave.")
            scene = "cave"
        elif cmd == "climb":
            print("\nYou climb the rocky hill toward the old castle.")
            scene = "castle"
        elif cmd == "back":
            print("\nYou return to the old stone road.")
            scene = "start"
        else:
            hearts -= 1
            print("\nThat command does not work.")
            print("Hint: Type north, climb, or back.")