result = 123 +4.14
print(result)


# division entière
result = 1 // 3
print(result)


#modulo - c'est le reste de la divison c'est à dire 10/3 = 3+3+3+1 le modulo est donc 1
# on peut aussi s'en servir pour voir si un nombre est pair ou impair ex, si le resultat est 0 le nombre est pair
#si le resultat est 1e nombre est impair
result = 10 % 3
print(result)

# le modulo sert aussi à vérifier la divisibilité d'un nombre
result = 7685923 % 7
print(result)
# ici, le resultat obtenu est 0 donc 7685923 est divisible par 7

# puissances sur python on utilise **
#dans certains languages c'est ^ ou pow()
result= 3 ** 2
print(result)

# operateur booléen  & "and" 
result = True and True #True
result = False and True #False
result = True and False #False
result = False and False #False