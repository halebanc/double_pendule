from fonctions import *
import sys

argument=sys.argv
if(len(argument)!=10 and argument[1]!="help"):
    print("Vous n'avez pas rentrez le bon nombre d'argument \nEssayez help pour avoir de l'aide.")
    exit(1)

if(argument[1]=="help"):
    retour="Bienvenue dans le message d'aide du  programme double_pendule.py\n\
La commande comprend 9 arguments:\n\
1: pendule / pendule-eul , on utilise soit la methode de RK4 pour pendule soit la methode de Euleur pour pendule-eul\n\
2:l1, taille de la première tige en metre\n\
3:l2, taille de la deuxième tige en metres\n\
4:m1, masse du premier poidsen kg\n\
5:m2, masse du second poids en kg\n\
6:position de de départ de l'angle alpha en radian \n\
7:position de départ de l'angle beta en radian \n\
8:vitesse de départ de l'angle alpha en rdaian par seconde\n\
9:vitesse de départ de l'angle beta en radian par seconde\n\
\n\
Exemple:\n\
python3 doouble_pendule.py pendule 1 1 1 1 3.14 0 0 0"
    print(retour)
    exit(0)


arg1=str(argument[1])
l1=float(argument[2])
l2=float(argument[3])
m1=float(argument[4])
m2=float(argument[5])
alpha0=float(argument[6])
beta0=float(argument[7])
valpha0=float(argument[8])
vbeta0=float(argument[9])
if(arg1=="pendule"):
    animation_double_pendule((l1+l2)*1.5, 0.01,[alpha0, beta0, valpha0, vbeta0],l1, l2, m1, m2, rk=True)
elif(arg1=="pendule-eul"):
    animation_double_pendule((l1+l2)*1.5, 0.01,[alpha0, beta0, valpha0, vbeta0],l1, l2, m1, m2, eul=True)
else:
    print("Vous n'avez pas rentrez un argument valide\nEssayez help pour avoir de l'aide.")
    exit(1)
#affiche les angles au cours du temps en bleu 
#animation_double_pendule(3, 0.0005,[pi/2, pi/2, 0, 0],1, 1, 1, 1, graphe=True, t_graphe=300000, save=True)
