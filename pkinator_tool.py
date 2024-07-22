import keyboard
import random

class KeyEventHandler:
    def __init__(self):
        print("Please enter the petition:", end=' ', flush=True)
        self.divination = [
            "You may not fully believe in the process just yet. Trust will come with time.",
            "There seems to be some hesitation. Give it a bit more thought and see what unfolds.",
            "Your trust is still building. Keep an open mind and stay patient.",
            "It’s okay to be skeptical. Trust will grow as you continue this journey.",
            "There’s a sense of doubt lingering. Reflect on your feelings and see if they shift.",
            "Skepticism is natural. Continue to explore and the answers will become clearer.",
            "You might question the guidance now, but clarity will emerge with patience.",
            "Doubt can cloud judgment. Stay open and see how things evolve over time.",
            "Trust is a process. Keep engaging and you might find the answers you seek.",
            "Caution is wise. Allow the process to unfold and see how your perspective changes."]

        
        self.mask = ["L", "e", "o", " ", "p", "l", "e", "a", "s", "e", " ", "a", "n", "s", "w", "e", "r", " ", "t", "h", "e", " ", "f", "o", "l", "l", "o", "w", "i", "n", "g", " ", "q", "u", "e", "s", "t", "i", "o", "n"]
        self.answer = ""
        self.i = 0  # Initialize the counter
        self.mask_mode = False  # State variable to track if mask mode is active

        # Register the function to be called on each key press
        keyboard.on_press(self.on_key_event)
        
  #  def custom_behavior(self):
   #     #print("This is the function where you can write custom behavior")
    #    x = input("Enter your input: ")
     #   print(random.choice(self.divination))

    def on_key_event(self, event):
        if event.name == '.':
            if self.mask_mode:
                self.mask_mode = False  # Deactivate mask mode
                # print("Mask mode deactivated.")
            else:
                self.mask_mode = True
                self.i = 0  # Reset counter for mask mode
                self.answer = ""
                # print("Mask mode activated.")
            return  # Exit the function to avoid processing '.' as a regular key

        if self.mask_mode:
            if self.i < len(self.mask):
                if event.name == 'backspace':
                    if self.answer:
                        self.answer = self.answer[:-1]  # Remove the last character from the answer string
                elif event.name in {'space', 'enter', 'tab', 'esc', 'shift', 'ctrl', 'alt'}:
                    special_keys = {
                        'space': ' ',
                        'enter': '\n',
                        'tab': '\t',
                        'esc': '',
                        'shift': '',
                        'ctrl': '',
                        'alt': ''
                    }
                    char = special_keys.get(event.name, '')
                    self.answer += char
                else:
                    char = event.name
                    self.answer += char
                
                # Print the current character from the mask and update the counter
                if self.i < len(self.mask):
                    print(self.mask[self.i], end='', flush=True)
                    self.i += 1  # Increment the counter
                else:
                    print()  # Print a new line if the mask is exhausted
            else:
                print()  # Print a new line if the mask is exhausted
        else:
            input()
            print("Leo says!!:",random.choice(self.divination))  # For non-mask mode

    def run(self):
        keyboard.wait('enter')
        

# Ensure that the script runs only when it is executed directly
if __name__ == "__main__":
    input("Please write your question:") 
    handler = KeyEventHandler()
    handler.run()
    print("")
    if handler.mask_mode:
        print("Leo says !! :",handler.answer)


