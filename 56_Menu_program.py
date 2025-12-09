# Indian Caffeine Menu Program

print("=== Welcome to Indian Caffeine House ===")

menu = {
    "Masala Chai": 20,
    "Ginger Tea": 15,
    "Filter Coffee": 30,
    "Elachi Tea": 20,
    "Badam Milk": 40,
    "Cold Coffee": 60,
    "Lemon Tea": 15,
    "Green Tea": 25
}

# Display Menu
print("\n--- MENU ---")
for item, price in menu.items():
    print(f"{item} : ₹{price}")

total = 0

while True:
    choice = input("\nEnter the drink name (or type 'done' to finish): ")

    if choice.lower() == "done":
        break

    if choice in menu:
        total += menu[choice]
        print(f"Added {choice}. Current Total: ₹{total}")
    else:
        print("Sorry! Item not found in menu.")

print("\nYour final bill is: ₹", total)
print("Thank you for visiting Indian Caffeine House!")
