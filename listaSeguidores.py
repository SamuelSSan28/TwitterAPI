import time

import tweepy

class Usuarios:
    def __init__(self):
            self.screen_name = str()
            self.listaDeSeguidores = list()



def seguidor(api,id,id2):
        while True:
            try:
               print("------------/---------/-----------")
               return  api.show_friendship(source_screen_name =id,target_screen_name =id2)
            except tweepy.RateLimitError:
                print("++++++++++++++++++")
                print("Esperandoooooooo")
                print("++++++++++++++++++")
                time.sleep(15*60)


# passa o Consumer Key e o Consumer Secret
auth = tweepy.OAuthHandler('fAcWDUi0sQIRK5jJApYnis5ZL', 'wqDbAyQhLqlpvdJcDT0VfnaGW2Q1kyb14fAHSdYJmLxmB7K01M')

# passa o "Access Token" e o "Access Token Secret"
auth.set_access_token('3090425878-OroIfqEkU3WNs7C0oU8oHuQ95i4AfAMp34lRzq5','Y1EvT0rPn2qbUnNBhccu6vs4UN6bTUdx2ajwqFCw3UQm9')

# cria um objeto api
api = tweepy.API(auth)
api.user_timeline(id="twitter")
tweepy.Cursor(api.user_timeline, id="twitter")

listaInfluentes = []
listaRecentes = []


with open("influentes.txt") as file:
    for line in file:
        l = line.split()
        listaInfluentes.append(l[0])

with open("recentes.txt") as file:
    for line in file:
        l = line.split()
        if listaInfluentes.count(l[0]) == 0:
            listaRecentes.append(l[0])


influentes = [Usuarios() for i in range(len(listaInfluentes))]
recentes = [Usuarios() for i in range(len(listaRecentes))]

for i in range(len(listaRecentes)): #tira usuarios repetidos da minha lista
        recentes[i].screen_name = listaRecentes[i]

for i in range(len(listaInfluentes)): #tira usuarios repetidos da minha lista
        influentes[i].screen_name = listaInfluentes[i]

for i in influentes:
    for r in recentes:
        status = seguidor(api, i.screen_name, r.screen_name)
        if (status[0].followed_by  == True):
            i.listaDeSeguidores.append(r.screen_name)
            print("{} é seguido por {}".format(i.screen_name, r.screen_name))
        else:
            print("{} não é seguido por {}".format(i.screen_name, r.screen_name))
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


with open("seguidorees.txt", 'w') as f: #1  - usuarios quem ele segue[se for 0 não segue ninguem]
    for i in influentes:
        f.write(i.screen_name)
        if (len(i.listaDeSeguidores) > 0):
            for j in i.listaDeSeguidores:
                s = str(j)
                f.write("".join(s + ","))
            f.write("\n")
        else:
            f.write(" 0\n")
