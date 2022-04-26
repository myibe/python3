# exercice-12-classes.py

# exo 12.1
# Créez une classe nommée `User` qui possède les attributs suivants :
# - firstname: valeur par défaut ''
# - lastname: valeur par défaut ''
# - email: valeur par défaut ''
# - newsletter: valeur par défaut False
# et la méthode suivante :
# - __init__() : le constructeur
# Pas la peine de créer de getters et de setters

# réponse 12.1

from itertools import product
from unicodedata import name


class User:

    def __init__(self, firstName: str, lastName: str, email: str, newsletter=False):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.newsletter = newsletter

# exo 12.2
# Créez 4 instances de la classe `User` et affectez les valeurs suivantes à ses attributs :
# - user1
#   - firstname: Joe
#   - lastname: Dalton
#   - email: joe.dalton@example.com
#   - newsletter: true
# - user2
#   - firstname: William
#   - lastname: Dalton
#   - email: william.dalton@example.com
#   - newsletter: false
# - user3
#   - firstname: Jack
#   - lastname: Dalton
#   - email: jack.dalton@example.com
#   - newsletter: false
# - user3
#   - firstname: Avrel
#   - lastname: Dalton
#   - email: avrel.dalton@example.com
#   - newsletter: true

# réponse 12.2


user1 = User("Joe" , "Dalton", "joe.dalton@example.com", True)
user2 = User("William", "Dalton", "william.dalton@example.com", False)
user3 = User("Jack", "Dalson", "jack.dalton@example.com", False)
user4 = User("Avrel", "Dalson", "avrel.dalton@example.com", True)

# exo 12.3
# Ajoutez chacune des instances de la classe `User` à une liste nommée `users`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom complet et l'email de chaque utilisateur s'il est abonné à la newsletter (c-à-d si newsletter == True)

# réponse 12.3
users = [user1, user2, user3, user4]


for user in users:
    if user.newsletter == True:
        print(user.firstName, user.lastName, user.email)

# exo 12.4
# Créez une classe nommée `ProductLorem` qui possède les attributs suivants :
# - _name: valeur par défaut ''
# - _price: valeur par défaut 0.0
# et les méthodes suivantes :
# - __init__() : le constructeur
# - get_name() : renvoit le nom du produit
# - set_name() : détermine le nom du produit
# - get_price() : renvoit le prix du produit
# - set_price() : détermine le prix du produit

# réponse 12.4

class ProductLorem:

    def __init__(self, name: str, price=0):
        self.name = name
        self.price = price


# getter 
    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

# setter

    def set_price(self, x): 
        self._price = x 

    def set_name(self, y): 
        self._age = y 


# exo 12.5
# Créez 3 instances de la classe `ProductLorem` et affectez les valeurs suivantes à ses attributs en utilisant les setters :
# - product1
#   - name: Foo
#   - price: 31,41
# - product2
#   - name: Bar
#   - price: 27,18
# - product3
#   - name: Baz
#   - price: 16,18

# réponse 12.5

product1 = ProductLorem("Foo", 31.41)
product2 = ProductLorem("Bar", 27.18)
product3 = ProductLorem("Baz",16.18)

# exo 12.6
# Ajoutez chacune des instances de la classe `ProductLorem` à une liste nommée `products`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom et le prix de chaque produit
# Calculez la somme du prix des produits et affichez-en un arrondi à 2 chiffres après la virgule, après la boucle `for`

# réponse 12.6


products = [product1, product2, product3]
total = 0
for product in products:
    total += product.get_price()
    print(product)

print(round(total, 2))




# products = [product1, product2, product3]
# myNewList = [str(name) for name in products]
# sum1 = sum(myNewList)
# sum2 = sum(number for number in myNewList)
# print(f"Sum of list -> {sum1}")
# print(f"Sum of list -> {sum2}")


# exo 12.7
# Créez une classe nommée `ProductIpsum` qui possède les attributs suivants :
# - _name: valeur str transmise par le constructeur
# - _price: valeur float par défaut 0.0
# - _tax: valeur float par défaut 0.0
# et les méthodes suivantes :
# - __init__(name, price, tax) : le constructeur
# - get_name() : renvoit le nom du produit
# - set_name() : détermine le nom du produit
# - get_price() : renvoit le prix du produit
# - set_price() : détermine le prix du produit
# - get_tax() : renvoit la taxe en pourcentage
# - set_tax() :  détermine la taxe en pourcentage (pour une taxe de 20 %, le paramètre doit être 20.0)
# - get_tax_fee() : cette méthode calcule le montant de la taxe et le renvoit ; par exmeple pour un produit de 100 € et une taxe de 20 %, le résultat est 20.0
# - get_tax_included_price() : cette méthode calcule le prix taxe incluse et le renvoit ; par exemple pour un produit de 100 € et une taxe de 20 %, le résultat est 120.0
# réponse 12.7
class ProductIpsum:
    def __init__(self, name: str, price: float = 0.0, tax: float = 0.0):
        self._name = name
        self._price = price
        self._tax = tax

    def __str__(self):
        return f"{self._name} {self._price} {self._tax}"

    def get_name(self):
        return self._name

    def set_name(self, name: str):
        self._name = name

    def get_price(self):
        return self._price

    def set_price(self, price: float):
        self._price = price

    def get_tax(self):
        return self._tax

    def set_tax(self, tax: float): 
        self._tax = tax 

    def get_tax_fee(self):
        return self._price * (self._tax / 100)

    def get_tax_included_price(self):
        return self.get_tax_fee() + self._price
# exo 12.8
# Créez 3 instances de la classe `ProductIpsum` et affectez les valeurs suivantes à ses attributs en utilisant le constructeur :
# - product1
#   - name: Dolor
#   - price: 31,41
#   - tax: 20.0
# - product2
#   - name: Sit
#   - price: 27,18
#   - tax: 10.0
# - product3
#   - name: Amet
#   - price: 16,18
#   - tax: 5.5

# réponse 12.8
product1 = ProductIpsum("Dolor", 31.41, 20.0)
product2 = ProductIpsum("Sit", 27.18, 10.0)
product3 = ProductIpsum("Amet", 16.18, 5.5)
# exo 12.9
# Ajoutez chacune des instances de la classe `ProductIpsum` à une liste nommée `products`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom, le prix (sans la taxe), la taxe et le prix taxe incluse de chaque produit
# Calculez :
# - la somme du prix des produits sans les taxes
# - la somme du montant des taxes
# - la somme du prix des produits taxes incluses
# Et affichez-en des arrondis à 2 chiffres après la virgule, après la boucle `for`

# réponse 12.9

products = [product1, product2, product3]
sum_price_sans_tax = 0
sum_tax = 0
sum_price_taxInclus = 0
for product in products:
    print(product.get_name(),product.get_price())
    print(product.get_tax())
    print(product.get_tax_included_price())
    sum_price_sans_tax += product.get_price()
    sum_tax += product.get_tax_fee()
    sum_price_taxInclus += product.get_tax_included_price()

print(round(sum_price_sans_tax, 2))
print(round(sum_tax, 2))
print(round(sum_price_taxInclus, 2))

