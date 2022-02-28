from copy import deepcopy
import numpy as np 
import matplotlib.pyplot as plt
from math import sin, cos, sqrt, pi

def euler(fonction, q, t, dt, args):
    """
    Cette fonction renvoie l'approximation de la méthode d'euler à t+dt appliqué à la fonction

    fonction est un fonction avec q et t en parametre et une multitude d'argument 
    q est un tableau de boolean 
    t et dt sont des booleans
    """
    dq=fonction(q, t, args)
    q_0=deepcopy(q)
    for i in range(0, len(q)):
        q[i]=q_0[i]+(dq[i]*dt)

def rk4(fonction, q, t, dt, args):
    """
    Cette fonction renvoie l'approximation de la méthode d'Runge Kata à t+dt appliqué à la fonction

    fonction est un fonction avec q et t en parametre et une multitude d'argument 
    q est un tableau de boolean 
    t et dt sont des booleans
    """
    taille=len(q)
    p1=fonction(q, t, args)

    q2=deepcopy(q)
    for a in range (0, taille):
        q2[a]+=p1[a]*(dt/2)
    p2=fonction(q2,t+(dt/2), args)

    q3=deepcopy(q)
    for b in range(0, taille):
        q2[b]+=p2[b]*(dt/2)
    p3=fonction(q3, t+(dt/2), args)

    q4=deepcopy(q)
    for c in range (0, taille):
        q4[c]+=p3[c]*dt
    p4=fonction(q4, t+dt, args)

    q_0=deepcopy(q)
    for i in range(0, taille):
        q[i]=q_0[i]+(dt/6)*(p1[i]+(2*p2[i])+(2*p3[i])+p4[i])


def equa_pendule(q, t, args):
    retour=[None]*2
    retour[0]=q[1]
    retour[1]=-(args[0]**2)*sin(q[0])
    return retour

def equa_double_pendule(q, t, args):
    g=args[0]
    l1=args[1]
    l2=args[2]
    m1=args[3]
    m2=args[4]
    retour=[None]*4
    retour[0]=q[2]
    retour[1]=q[3]
    retour[2]=(1/(l1*(m1+m2*(sin(q[0]-q[1])**2))))*(m2*(cos(q[0]-q[1])*g*sin(q[1])-l1*(q[2]**2)*sin(q[0]-q[1])*cos(q[0]-q[1])-l2*(q[3]**2)*sin(q[0]-q[1]))-(m1+m2)*g*sin(q[0]))
    retour[3]=((m1+m2)/(l2*(m1+m2*(sin(q[0]-q[1])**2)))) * (((m2/(m1+m2))*(l2*(q[3]**2)*sin(q[0]-q[1])*cos(q[0]-q[1])))+ (g*sin(q[0])*cos(q[0]-q[1]))-(g*sin(q[1]))+(l1*(q[2]**2)*sin(q[0]-q[1])))
    #retour[2]=(-1/((m1+m2)*l1))*((m2*l2*retour[3]*cos(q[0]-q[1]))+(m2*l2*(q[3]**2)*sin(q[0]-q[1]))+((m1+m2)*g*sin(q[0])))
    return retour

def animation_pendule(largeur,dt, q_0, l, eul=True, rk=False, gravite=9.8, graphe=False, t_graphe=100000):
    if graphe:
        eul=True
        rk=True
    else:
        min = -largeur
        max = largeur
        fig, ax = plt.subplots()
        ax.axis([min,max,min,max])
        ax.set_aspect("equal")
    if eul:
        if not graphe:
            ligne1, = ax.plot([0, sin(q_0[0])*l],[0 ,-cos(q_0[0])*l ], "b")
        else:
            tab_q_e=[q_0[0]]

        q_e=deepcopy(q_0)
    if rk:
        if not graphe:
            ligne2, = ax.plot([0, sin(q_0[0])*l],[0 ,-cos(q_0[0])*l ], "r")
        else:
            tab_q_r=[q_0[0]]
        q_r=deepcopy(q_0)
    if graphe:
        compte=0
        tab_t=[0.]
    t=dt
    while(True):
        if eul:
            euler(equa_pendule, q_e, t, dt, [sqrt(gravite/l)] )
            if not graphe:
                ligne1.set_data([0, sin(q_e[0])*l],[0 ,-cos(q_e[0])*l ])
        if rk:
            rk4(equa_pendule, q_r, t, dt, [sqrt(gravite/l)])
            if not graphe:
                ligne2.set_data([0, sin(q_r[0])*l],[0 ,-cos(q_r[0])*l ])
        if not graphe:
            plt.pause(dt)
        else:
            tab_t.append(t)
            tab_q_e.append(q_e[0])
            tab_q_r.append(q_r[0])
            if compte>=t_graphe:
                break
            compte+=1

        t+=dt

    if graphe:
        x=np.array(tab_t)
        y1=np.array(tab_q_r)
        y2=np.array(tab_q_e)
        plt.plot(x,y1, "r")
        plt.plot(x,y2, "b")
    plt.show()


def animation_double_pendule(largeur_tab,dt, q_0, l1,l2, m1, m2,  eul=False, rk=False, gravite=9.8, graphe=False, t_graphe=1000000, energie=False, save=False):
    #Animation du double pendile à partir des differentes fonctions 
    #grahe sert à produire un graphe des angles alpha et phi
    #
    if not (eul or rk):
        eul=True
    if graphe:
        eul=True
        rk=True
    else:
        min = -largeur_tab
        max = largeur_tab
        fig, ax = plt.subplots()
        ax.axis([min,max,min,max])
        ax.set_aspect("equal")
    if energie:
        energie_tab=[]
    x1_0=l1*sin(q_0[0])
    y1_0=-l1*cos(q_0[0])
    x2_0=l1*sin(q_0[0])+sin(q_0[1])*l2
    y2_0=-l1*cos(q_0[0])-cos(q_0[1])*l2
    if energie:
        T=(m1/2)*((l1**2)*(q_0[2]**2))+(m2/2)*((l1**2)*(q_0[2]**2)+(l2**2)*(q_0[3]**2)+(2*l1*l2*q_0[2]*q_0[3]*cos(q_0[0]-q_0[1])))
        U=m1*gravite*l1*cos(q_0[0])-m2*gravite*(l1*cos(q_0[0])+l2*cos(q_0[1]))
        E=T+U 
        print("depart:"+str(E))
    if eul:
        if not graphe:
            ligne_e1, = ax.plot([0, x1_0],[0, y1_0], "b")
            ligne_e2, = ax.plot([x1_0,x2_0 ],[y1_0 , y2_0], "b")
        else:
            tab_q_e1=[q_0[0]]
            tab_q_e2=[q_0[1]]

        q_e=deepcopy(q_0)
    if rk:
        if not graphe:
            ligne_r1, = ax.plot([0, x1_0],[0, y1_0], "r")
            ligne_r2, = ax.plot([x1_0,x2_0 ],[y1_0 , y2_0], "r")
        else:
            tab_q_r1=[q_0[0]]
            tab_q_r2=[q_0[0]]
        q_r=deepcopy(q_0)
    if graphe or energie:
        compte=0
        tab_t=[0.]
    t=dt
    while(True):
        if eul:
            euler(equa_double_pendule, q_e, t, dt, [gravite, l1, l2, m1, m2] )
            if not graphe:
                x1=l1*sin(q_e[0])
                y1=-l1*cos(q_e[0])
                x2=l1*sin(q_e[0])+l2*sin(q_e[1])
                y2=-l1*cos(q_e[0])-cos(q_e[1])*l2
                ligne_e1.set_data([0, x1], [0, y1])
                ligne_e2.set_data([x1, x2], [y1, y2])
            if energie and (compte%100000==0):
                H=(m1+m2)*(((l1*q_e[2])**2)/2)+(m2/2)*((l2*q_e[3])**2)+m2*l1*l2*q_e[2]*q_e[3]*cos(q_e[0]-q_e[1])-(m1+m2)*gravite*l1*cos(q_e[0])-m2*gravite*l2*cos(q_e[1])
                print("eul:"+str(H), flush=True)
        if rk:
            rk4(equa_double_pendule, q_r, t, dt, [gravite, l1, l2, m1, m2])
            if not graphe:
                x1=l1*sin(q_r[0])
                y1=-l1*cos(q_r[0])
                x2=l1*sin(q_r[0])+sin(q_r[1])*l2
                y2=-l1*cos(q_r[0])-cos(q_r[1])*l2
                ligne_r1.set_data([0, x1], [0, y1])
                ligne_r2.set_data([x1, x2], [y1, y2])
            if energie and (compte%100==0):
                    H=(m1+m2)*(((l1*q_r[2])**2)/2)+(m2/2)*((l2*q_r[3])**2)+m2*l1*l2*q_r[2]*q_r[3]*cos(q_r[0]-q_r[1])-(m1+m2)*gravite*l1*cos(q_r[0])-m2*gravite*l2*cos(q_r[1])
                    print("rk:"+str(H), flush=True)
        if not graphe:
            plt.pause(dt)
        else:
            tab_t.append(t)
            tab_q_e1.append(q_e[0])
            tab_q_e2.append(q_e[1])

            tab_q_r1.append(q_r[0])
            tab_q_r2.append(q_r[1])
            if compte>=t_graphe:
                break
            compte+=1
            if(compte%1000==0):
                print(".", end="", flush=True)
            if(compte%10000==0):
                print("-", end="",  flush=True)
        if energie and not graphe:
            compte+=1


        t+=dt

    if graphe:
        x=np.array(tab_t)
        y1=np.array(tab_q_r1)
        y2=np.array(tab_q_e1)
        y3=np.array(tab_q_r2)
        y4=np.array(tab_q_e2)
        plt.plot(x,y1, "r")
        plt.plot(x,y2, "b")
        plt.plot(x,y3, "m")
        plt.plot(x,y4, "c")
        plt.xlabel("temps")
        plt.ylabel("angles,  methode de Euleur en cyan et mauve\n methode rk4 en rouge et bleu")
    if save:
        plt.savefig("fig1.png", dpi=500)
    plt.show()


