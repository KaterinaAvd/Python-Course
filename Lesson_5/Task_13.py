# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

def exp_num(a, b):     
    if b == 0:         
        return 1  
    return a * exp_num(a, b-1)

print(exp_num(int(input()), int(input())))