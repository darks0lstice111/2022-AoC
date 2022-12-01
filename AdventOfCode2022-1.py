cals = 0
elves = []
with open('day1Input.txt') as f:
    inps = f.readlines()
    
for inp in inps:
    if inp != "\n":
        cals += int(inp)
    else:
        elves.append(cals)
        cals = 0
        
print("Elf with highest calorie inventory is Elf " + str(elves.index(max(elves))+1) + " with calorie count: " + str(max(elves)))
elves.sort()
print(elves[-1] + elves[-2] + elves[-3])