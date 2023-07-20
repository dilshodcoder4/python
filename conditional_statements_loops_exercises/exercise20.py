# 20. Write a Python program to print the alphabet pattern 'G'.
for x in range(0,7):
    if x==0:
        print("  gg")
    elif x==1 or  x==4 or x==5:   
        print("g    g")
    elif x==2:
        print("g")    
    elif x==3:
        print("g  ggg")
    elif x==6:
        print(" gggg ")
                