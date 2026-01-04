print("Welcome to the Treasure Island Game!\n")
print("Welcome, explorer.\nYou stand before an ancient temple said to remember every mistake.\nChoose wisely. Your decisions shape what comes next.\n")

injured_arms = False    
injured_lungs = False

# --stage 1--

print("Two symbols glow on the ground in front of you.\nOne shines with Light.\nThe other absorbs everything like a Void.\n")
stage1 = input("[Choose: Light or Void]\n").lower()
if stage1 == "void":
    print("\nGood choice.\nThe ground remains stable beneath your feet.\nYou step forward and walk deeper into the temple.")
else:
    stage1 == "light"
    print("\nWrong choice.\nThe symbol flashes violently.\nThe floor collapses beneath you.\n")
    
    print("You land hard inside a dark chamber.\nThe floor is breaking apart.\nYou must act quickly.")
    print("\nTwo ways appear:\nA hanging rope swaying above\nA narrow stone ledge along the wall\n")
    escape1 = input("[Choose: Rope or Ledge]\n").lower()
    if escape1 == "rope":
        print("\nYou grab the rope just in time.\nThe floor collapses below you.\nYou climb up and escape the chamber.\n")
        print("You survived… but your arms are injured.\nYou continue forward, weakened but alive.")
        injured_arms = True   
    else:
        escape1 == "ledge"
        print("\nWrong choice.\nYou step onto the ledge.\nThe stone crumbles under your feet.\nYou lose balance and fall into darkness.\n")
        print("You are dead.\nGame Over.")
        exit()

# --stage 2--

print("\nYou enter a long hall.\nAt the end, two doors stand silently:\nA Wide door with heavy marks\nA Narrow door with smooth edges\n")
stage2 = input("[Choose: Wide or Narrow]\n").lower()
if stage2 == "narrow":
    print("\nCorrect.\nThe door opens smoothly without resistance.\nYou move deeper into the temple.")
else:
    stage2 == "wide"
    print("\nWrong choice.\nThe moment you open the door,\na strange smell fills the air.\nThe door slams shut behind you.")   

    print("Green gas spreads rapidly across the room.\nYour chest tightens.\nYou must escape now.\n")
    print("Two actions possible:\nCrawl close to the floor\nRun fast to the exit")
    escape2 = input("[Choose: Crawl or Run]\n").lower()
    if escape2 == "crawl":
        print("\nSmart move.\nThe air near the floor is clearer.\nYou slowly reach the exit and escape.\n")
        print("You survive… but your lungs are damaged.\nBreathing is now harder.")
        injured_lungs = True   
    else:
        escape2 == "run"
        print("\nWrong choice\nYou try to outrun the gas.\nYou inhale deeply.\nYour vision fades.\n")
        print("You are dead.\nGame Over.")
        exit()

# --stage 3--

print("A deep pit blocks your path.\nA broken bridge hangs loosely across it.\n")
print("Options:\nJump across\nRepair the bridge\n")

stage3 = input("[Choose: Jump or Repair]\n").lower()
if stage3 == "jump":
    if injured_arms or injured_lungs:
        print("\nYou try to jump, but your injured body fails.\nYour strength gives out mid-air.\n")
        print("You fall into the pit.\nYou are dead.\n")
        print("Game Over.")
        exit()
    else:
        stage3 == "repair"
        print("\nYou take a deep breath and jump.\nYou land safely on the other side.\n")
        print("Well done.")
else:
    stage3 == "repair"
    print("You carefully repair the bridge piece by piece.\nIt takes time, but it holds.")
    print("You cross safely to the other side.\n")

# --final stage--
    
print("You reach the heart of the temple.\nA massive vault stands before you.\n")
print("Three seals glow:\nFire\nStone\nTime")

final_stage = input("[Choose: Fire, Stone, or Time]\n").lower()
if not injured_arms and not injured_lungs and final_stage == "time":
    print("\nThe seal reacts to your presence.\nThe vault opens.\nTreasure is yours.\n")
    print("Congratulations! You have completed the Treasure Island Game successfully!\n")
elif injured_arms or injured_lungs and final_stage == "stone":
    print("\nThe seal acknowledges your struggles.\nThe vault opens.\nTreasure is yours.\n")
    print("Congratulations! You have completed the Treasure Island Game successfully!\n")
else:
    print("\nWrong choice.\nThe seal remains closed.\nThe temple begins to shake violently.\nYou must flee!\nYou run out just in time as the temple collapses behind you.\n")
    print("You survived, but the treasure remains hidden.\n.")
    print("Game Over.")
             

   