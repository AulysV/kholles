import random

A = "Alice"
B = "Bob"

# A = str(input("Qui est le premier combattant ? ")
# A = str(input("Qui est le second combattant ? ")

points_A = int(input(f"Points de {A}: "))
points_B = int(input(f"Points de {B} : "))

def kipass(x, y):
    if x > y:
        print(f"{B} passe en kholle.")
    elif y > x:
        print(f"{A} passe en khôlle.")
    else:
        # Si les points sont égaux, random :
        print(f"{random.choice([A, B])} passe en khôlle.")

kipass(points_A, points_B)