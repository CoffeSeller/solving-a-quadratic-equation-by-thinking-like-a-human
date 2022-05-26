print("\n We are going to solve an equation like this: \"x² + bx + c = 0\" Create equation by entering b and c values.\n")
b = int(input("please enter b: "))
c = int(input("please enter c: "))
print("\nEquation that you just created: x² +", b, "x +", c, "= 0")

multipliers_c = []
#finding multipliers of c
if c > 0:
    for i in range(1, c + 1):
       if c % i == 0:             
           multipliers_c.append(i) 

elif c < 0:
    for i in range(c,0): 
            if c % i == 0:              
                multipliers_c.append(i)  

else: #if c=0
    print("\nRoots of equation: x₁ = 0", ",  x₂ = ", -b, "\n") #if c=0 equation is: x² + bx = 0 and its same as x.(x+b)=0 so one root is zero and other root is -b
    exit()


#From here on there is something about setting negative and positive multipliers for negative values of c, which is hard to explain.
multipliers_c_with_opposite_signs = [-x for x in multipliers_c] 

c_1 = multipliers_c[:len(multipliers_c)//2]
c_2 = multipliers_c[len(multipliers_c)//2:]

c_3 = multipliers_c_with_opposite_signs[:len(multipliers_c)//2]
c_4 = multipliers_c_with_opposite_signs[len(multipliers_c)//2:]


c_5 = c_1 + c_4
c_6 = c_3 + c_2


last_multiplier = len(multipliers_c) - 1 

for i in range(0, len(multipliers_c) // 2):
    if c > 0:
        if multipliers_c[i] + multipliers_c[last_multiplier - i] == b : #we take a multiplier from start  and a multiplier from the end then we check if sum of these is equal to b 
            root1 = multipliers_c[i] * -1                                #multiply with -1 because :(ex: x+5=0: x≠5, x=-5)
            root2 = multipliers_c[last_multiplier - i] * -1          
            break                                                         

        elif multipliers_c_with_opposite_signs[i] + multipliers_c_with_opposite_signs[last_multiplier - i] == b :
            root1 = multipliers_c_with_opposite_signs[i] * -1                                          
            root2 = multipliers_c_with_opposite_signs[last_multiplier - i] * -1          
            break                                                         

        else:                                                          
            continue
    
    elif c < 0: 
        if c_5[i] + c_5[last_multiplier - i] == b : 
            root1 = c_5[i] * -1                       
            root2 = c_5[last_multiplier - i] * -1
            break
        
        elif c_6[i] + c_6[last_multiplier - i] == b :
            root1 = c_6[i] * -1
            root2 = c_6[last_multiplier - i] * -1
            break

        else:
            continue
    

if('root1' and 'root2' in locals()):
    print("\nRoots of equation are: x₁ = ", root1, ",  x₂ = ", root2, "\n")
    
else:
    print("\nThere is no roots in integers.")
