#Matias Fernandez
#2023-11-02

import random #je importe random pour que ca genere des nombres au hazard


def attempt():
    attempt = int(input("\nEntrez votre essai :"))
    
    if attempt == random_nb:
        print(f"\nBravo! Bonne réponse\nVous avez reussi en {tries} essai(s)")
        return True # dire que t'a reussi

    elif attempt > random_nb:
        print(f"\nMauvais choix, le nombre est plus petit que {attempt}.")
        

    elif attempt < random_nb:
        print(f"\nMauvaise réponse, le nombre est plus grand que {attempt}")

    return False # dire que tu na pas reussi
        


game = True 

while game:
    tries = 0 # nombre d'essais
    min = int(input("\nEntrez le premier numero pour que je choisisse un numero aleatoirement"))
    max = int(input("\nMaintenant, entrez le deuxieme numero (il doit etre plus grand que le precedant)"))
    # demande de choisir 2 numero
    
    random_nb = random.randint(min, max) #choisie un numero aleatoirement
    print(f"\nJ'ai choisi un nombre au hasard entre {min} et {max}\nA vous de le deviner...")

    while True:
        tries += 1 # ajouter +1 essai a chaque attempt
        if attempt():
            break
    
    retry = input("Voulez-vous faire une autre partie (o/n)?") 
    if retry.lower() != 'o': #.lower() convert une chaine en minuscule, si  = o, recommence, si =/= o, print meric et au revoir et finir le code
        break

print("Merci et au revoir...") 



    







