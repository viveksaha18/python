# Break
for i  in range(10):
    if(i == 3):
        break
    print(i)

# Continue
for i in range(10):
    if(i == 2 ):
        continue
    print(i)    

# Pass -> No Effect
for i in range (5):
    if(i == 2):
        pass
    print(i)