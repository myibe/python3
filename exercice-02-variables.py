# exercice-02-variables.py

# exo 2.1
# Affectez :
# - le nombre 42 à une variable
# - le nombre d'or 1,61 à une variable
# - votre nom et prénom à une variable
# - la valeur booléenne vrai si nous sommes le matin, sinon la valeur booléenne faux, à une variable
# - la valeur null `None` à une variable
# Affichez ces variables

# réponse 2.1
nombre = 42
print(42)

nombre_or = 1.61
print(nombre_or)

name = "Myriam Ibe"
print(name)

is_morning = True
print(is_morning)

is_notmorning = False
print(is_notmorning)


has_accepted = None
print(has_accepted)

# code 2.1
# la fonction `round()` permet d'arrondir un float en un integer
# 0,1 est arrondi à la valeur inférieur
print(round(0.1))
# 0,9 est arrondi à la valeur supérieur
print(round(0.9))
# la fonction `round()` permet aussi d'arrondir en précisant le nombre de chiffres après la virgule
# arrondir à un nombre décimal à 4 chiffres après la virgule
print(round(1 / 3, 4))

# exo 2.2
# Stockez le valeurs suivantes dans une variable et transtypez-les :
# - integer 2 en un float
# - float 1,62 en un integer
# - float 1,62 en un float arrondi à zéro chiffre après la virgule, puis en un integer
# - float 1,62 en un float arrondi à un chiffre après la virgule
# À chaque fois stockez le résultat dans une variable et affichez le résultat.

# réponse 2.2

#rep 1
nombre2 = 2
print(nombre2)
nombre2 = float(nombre2)
print(nombre2)

#rep 2
nombre3 = 1.62
print(nombre3)
nombre3 = int(nombre3)
print(nombre3)

#rep 3
nombre4 = 1.62
nombre4 = round(nombre4, 0)
print(nombre4)

nombre4 = int(nombre4)
print(nombre4)

#rep 4
nombre5 = 1.62
nombre5 = round(nombre5, 1)
print(nombre5)




