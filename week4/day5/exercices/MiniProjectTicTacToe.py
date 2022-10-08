def affichage(t):
    print(f"""
    Welcome to TIC TAC TOE
    
    TIC TAC TOE
    *****************
    *   {t['0'][0]} | {t['0'][1]} | {t['0'][2]}   *
    *  ---|---|---  *
    *   {t['1'][0]} | {t['1'][1]} | {t['1'][2]}   *
    *  ---|---|---  *
    *   {t['2'][0]} | {t['2'][1]} | {t['2'][2]}   *
    *****************
    """)


def enregistr_joueur(joueur):
    print(f"\tjouerer {joueur}'s turn...\n")
    row = input('\tEnter row: ')
    column = input('\tEnter column: ')
    while True :
        if int(row) > 3 or int(row) < 1 < 1:
            print("\tline incorrect")
        elif int(column) > 3 or int(column) < 1:
            print("\tcolumn incorrect")
        else:
            break
        row = input('\tEnter row: ')
        column = input('\tEnter column: ')
    row = str(int(row) -1)#-1 parceque le tableau commence à 0
    column = str(int(column) -1)
    return row, column



def jouer(joueur, t):
    while True:
        index = enregistr_joueur(joueur)
        ind = int(index[1])
        if t[index[0]][ind] == ' ': # il nous faut vérifer si la case est occupé ou pas
            t[index[0]][ind] = joueur
            return t
        else:
            print('\tCase occupée')    


def gagner(t):
    z = [0]
    x = [0]
    for i in range(0, 2):
        z.append(0)
        x.append(0)
    for j in range(0, 3):
        for i in range(0, 3):
            z[i] = 0
            x[i] = 0
        for i in range(0, 3):
            if t[str(i)][i].lower() == 'x':
                x[0] += 1
            if t[str(j)][i].lower() == 'x':
                x[1] += 1
            if t[str(i)][j].lower() == 'x':
                x[2] += 1
            if t[str(i)][i] == '0':
                z[0] += 1
            if t[str(j)][i] == '0':
                z[1] += 1
            if t[str(i)][j] == '0':
                z[2] += 1
        if 3 in z:
            return "\tjouerer 0's the winner"
        if 3 in x:
            return "\tjouerer X's the winner"
    return False




def principal():
    t = {
        '0': [],
        '1': [],
        '2': []
    }
    for x in t:
        for i in range(0, 3):
            t[x].append(' ')

    # Nous commençons par le jour X
    joueur = '0'
    while True:
        if joueur == '0':
            joueur = 'X'
        else:
            joueur = '0'
        affichage(t)
        t = jouer(joueur, t)
        win = gagner(t)
        affichage(t)
        if win:
            print(win)
            return True


principal()