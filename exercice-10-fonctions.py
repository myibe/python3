# exercice-10-fonctions.py

# exo 10.1
# Créer une fonction nommée `my_sum()` qui :
# - prend deux paramètres
# - additionne ces deux paramètres
# - renvoit le résultat
# Appelez la fonction et affichez le résultat

# réponse 10.1

def my_sum(a, b):
    return a + b

a = 2
b = 1
resultat = my_sum(a, b)
print(resultat)

# exo 10.2
# Créer une fonction nommée `my_diff()` qui :
# - prend deux paramètres de type `int`
# - soustrait `b` de `a`
# - renvoit le résultat de type `int`
# Notez bien le type hinting dans la déclaration de la fonction
# Appelez la fonction et affichez le résultat

# réponse 10.2

def my_diff(a: int, b: int):
    print(b-a)

my_diff(1,2)


# exo 10.3
# Créer une fonction nommée `oui_non()` qui :
# - prend un paramètre booléen
# - renvoit `oui` si le booléen est égal à True
# - renvoit `non` si le booléen est égal à False
# Appelez la fonction avec la valeur True et affichez le résultat
# Appelez la fonction avec la valeur False et affichez le résultat

# réponse 10.3

def oui_non(is_bool:bool):
    if is_bool:
        print(True)
    else:
        print(False)
        
oui_non(True)
oui_non(False)

# exo 10.4
# Créer une fonction nommée `is_greater()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoit True si `a` est plus grand que `b`
# - renvoit False dans les autres cas
# Appelez la fonction et affichez le résultat

# réponse 10.4

def is_greater(a:float, b:float):
    if a>b: 
        return True
    else:
        return False

print(is_greater(27.5, 24.2))

# exo 10.5
# Créer une fonction nommée `compare()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoit 1 si `a` est plus grand que `b`
# - renvoit -1 si `a` est plus petit que `b`
# - renvoit 0 si `a` et `b` sont égaux
# Appelez la fonction et affichez le résultat

# réponse 10.5

def compare(a:float, b:float):
    if a > b:
        print(1)
    elif b >a:
        print(-1)
    else:
        print(0)

compare(5,2)
compare(3,7)
compare(6,6)

# exo 10.6
# La formule suivante permet de convertir des mètres en miles :
#
#       miles = meters / 1609.344
#
# La formule suivante permet de faire l'inverse :
#
#       meters = miles * 1609.344
#
# Créez une fonction nommée :
#
# - meters_to_miles() permettant de convertir des mètres en miles
# - miles_to_meters() permettant de convertir des miles en mètres
#
# Ensuite convertissez les valeurs :
#
# - 1 Km en miles
# - 10 miles en mètres
#
# Appelez les fonctions et affichez les résultats

# réponse 10.6
def meters_to_miles(miles:float):
    print(miles/1609.344)

meters_to_miles(5)

def miles_to_meters(meters:float):
    print(meters*1609.344)

miles_to_meters(8)


# exo 10.7
# Créer une fonction nommée `compute_tax()` qui :
# - prend un paramètre nommé `price` de type `float`
# - prend un paramètre nommé `tax_type` de type `int`
# - ajoute une taxe de 2,1 % à `price` si `tax_type` est égal à `1`
# - ajoute une taxe de 5,5 % à `price` si `tax_type` est égal à `2`
# - ajoute une taxe de 10 % à `price` si `tax_type` est égal à `3`
# - ajoute une taxe de 20 % à `price` si `tax_type` est égal à `4`
# - renvoit le prix initial si `tax_type` n'est pas reconnu
# Appelez la fonction et affichez le résultat avec un montant de 100 € pour chaque type de taxe
#
# Référence : [Quels sont les taux de TVA en vigueur en France et dans l'Union européenne ? | economie.gouv.fr](https://www.economie.gouv.fr/cedef/taux-tva-france-et-union-europeenne)

# réponse 10.7

def compute_tax(price : float , tax_type: int):
    if tax_type == 1:
        price = price +(price*0.021)
        return price
    elif tax_type == 2:
        price = price + (price*0.055)
        return price
    elif tax_type == 3 :
        price = price + (price*0.1)
        return price
    elif tax_type == 4 :
        price = price + (price*0.2)
        return price
    else:
        return price


print(compute_tax(100,1))
print(compute_tax(100,2))
print(compute_tax(100,3))
print(compute_tax(100,4))