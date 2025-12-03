4# Saisie des valeurs
A = float(input("Entrez la valeur de A : "))
B = float(input("Entrez la valeur de B : "))

# 1. Fonction sans valeur de retour : vérifier si A et B sont de même signe
def meme_signe(a, b):
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        print("A et B sont de même signe.")
    elif a == 0 or b == 0:
        print("Au moins une des valeurs est zéro.")
    else:
        print("A et B sont de signes différents.")

# 2. Fonction avec valeur de retour : minimum
def minimum(a, b):
    if a < b:
        return a
    else:
        return b

# 3. Fonction avec valeur de retour : maximum
def maximum(a, b):
    if a > b:
        return a
    else:
        return b


# Appel des fonctions
meme_signe(A, B)

min_val = minimum(A, B)
max_val = maximum(A, B)

print("Le minimum est :", min_val)
print("Le maximum est :", max_val)
