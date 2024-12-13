import random
import tkinter as tk
from tkinter import simpledialog
import time

def rolling_animation():
    """Simulate a dice rolling animation."""
    animation_label.config(text="Rolling", font=("Arial", 30))
    root.update()
    for _ in range(3):
        time.sleep(0.5)
        animation_label.config(text="Rolling." + '.' * (_ + 1), font=("Arial", 30))
        root.update()

def assign_die_sides():
    """Assign unique numbers 1-25 to each die."""
    return random.sample(range(1, 26), 12)  # Unique numbers for 12 sides

def display_rolls(dice_sides, rolls):
    """Display the roll results in the GUI."""
    result_text = "Results:\n"
    for i, roll in enumerate(rolls, start=1):
        result_text += f"Die {i} rolled: {roll}\n"
    
    result_label.config(text=result_text, font=("Arial", 24))
    total = sum(rolls)
    total_label.config(text=f"Total roll value: {total}", font=("Arial", 30))

def ask_num_dice():
    """Ask the user how many dice they want to roll."""
    return simpledialog.askinteger("Dice Roller", "How many dice would you like to roll? (Choose between 1-3):", minvalue=1, maxvalue=3)

def start_over():
    """Reset everything to start over."""
    global start_button, quit_button
    result_label.config(text="")
    total_label.config(text="")
    animation_label.config(text="Welcome to the Dice Roller!", font=("Arial", 30))
    start_button.pack_forget()
    quit_button.pack_forget()
    ask_number_of_dice()

def quit_program():
    """Quit the program."""
    root.quit()

def main():
    global root, animation_label, result_label, total_label, num_dice, start_button, quit_button, dice_sides
    
    root = tk.Tk()
    root.title("Dice Roller")

    # Center the window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 800
    window_height = 600
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    
    # Enlarged welcome message
    animation_label = tk.Label(root, text="Welcome to the Dice Roller!", font=("Arial", 30))
    animation_label.pack(pady=20)
    
    # Wait for a while to show welcome message, then clear it
    root.after(2000, lambda: animation_label.config(text=""))
    
    # Ask how many dice to roll
    root.after(2500, ask_number_of_dice)

    # Create the result and total labels, initially hidden
    result_label = tk.Label(root, font=("Arial", 24))
    result_label.pack(pady=20)

    total_label = tk.Label(root, font=("Arial", 30))
    total_label.pack(pady=10)

    root.mainloop()

def ask_number_of_dice():
    global num_dice, dice_sides
    num_dice = ask_num_dice()
    
    if num_dice:
        dice_sides = [assign_die_sides() for _ in range(num_dice)]
        
        # Display the dice sides
        sides_text = "Assigned die sides:\n"
        for i, sides in enumerate(dice_sides, start=1):
            sides_text += f"Die {i}: {sides}\n"
        result_label.config(text=sides_text, font=("Arial", 20))

        # After showing the assigned sides, show the Roll Dice button
        roll_button = tk.Button(root, text="Roll Dice", command=lambda: start_roll(dice_sides), font=("Arial", 20))
        roll_button.pack(pady=20)

def start_roll(dice_sides):
    rolling_animation()

    rolls = [random.choice(sides) for sides in dice_sides]

    # Display the dice sides and results in the GUI
    display_rolls(dice_sides, rolls)

    # Hide the Roll Dice button and show the Start Over and Quit buttons
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button) and widget["text"] == "Roll Dice":
            widget.pack_forget()

    # Define Start Over and Quit buttons as global variables
    global start_button, quit_button
    start_button = tk.Button(root, text="Start Over", command=start_over, font=("Arial", 20))
    start_button.pack(pady=10)

    quit_button = tk.Button(root, text="Quit", command=quit_program, font=("Arial", 20))
    quit_button.pack(pady=10)

if __name__ == "__main__":
    main()
