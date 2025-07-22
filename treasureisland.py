# 💖 Anjali's Cute Treasure Adventure Game 💖 NO CHEATING PLEASE kEEP IT FAIR

print("🌴 Welcome to Treasure Island! 🌴")
print("Your mission is to find the treasure... 💎 but only if you answer correctly!\n")


print("""
        🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊
        🌴     Start Point     🌴
                 !
           🪷 Rose Garden
                 !
          ☕ Cute Café
                 !
       📚 Secret Library
                 !
         🪙 TREASURE CAVE 
        🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊
""")


step_one = input("🐾 What is Anjali's favourite pet animal? (dog or cat): ").lower()
if step_one == "dog":
    print("✅ Right answer! i like dogs , its just family problem to keep cat as pet\n")

    # Step 2
    step_two = input("💖 Is Anjali cute? (yes or no): ").lower()
    if step_two == "yes":
        print("✨ Right again! You know her well!\n")

        # Step 3
        step_three = input("🎨 What is Anjali's favourite colour? (pink/golden/black): ").lower()
        if step_three == "pink":
            print("🔥 Burned by fire... Game Over.")
        elif step_three == "golden":
            print("🏆 YEY, YOU WIN! LOVE YOU ;) 💖✨")
        elif step_three == "black":
            print("🦁 Eaten by beasts... Game Over.")
        else:
            print("💀 Unknown path... Game Over.")
    else:
        print("🐟 Attacked by a trout... Game Over.")
else:
    print("🕳️ You fell into a hole... Game Over.")
