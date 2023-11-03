#Matias Fernandez
#2023-11-02

#identifier la variable point,
point = "***********"


while "*" in point:
    print(point)
    point = point.removeprefix("*") #quand il y a "*" dans le text, ca enleve un jusqu'a il y en n'a plus, cela est fait avec removeprefix, ce qui enleve le prefix "*", et la boucle recommence jusq'il y a 0 "*" qui rest