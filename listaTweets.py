import time

import tweepy

class Usuarios:
    def __init__(self):
            self.screen_name = str()
            self.listaDeSeguidores = list()
            self.listaDeTweets = list()
            self.citacoes = 0



def contains(u,usuarios):
        for i in usuarios:
            if i.screen_name == u:
                return  1

        return 0


def limit_handled(id,n):
        while True:
            try:
               return  api.retweets(id=id, count=n)
            except tweepy.RateLimitError:
                time.sleep(1 * 60)


# passa o Consumer Key e o Consumer Secret
auth = tweepy.OAuthHandler('fAcWDUi0sQIRK5jJApYnis5ZL', 'wqDbAyQhLqlpvdJcDT0VfnaGW2Q1kyb14fAHSdYJmLxmB7K01M')

# passa o "Access Token" e o "Access Token Secret"
auth.set_access_token('3090425878-OroIfqEkU3WNs7C0oU8oHuQ95i4AfAMp34lRzq5','Y1EvT0rPn2qbUnNBhccu6vs4UN6bTUdx2ajwqFCw3UQm9')

# cria um objeto api
api = tweepy.API(auth)
api.user_timeline(id="twitter")
tweepy.Cursor(api.user_timeline, id="twitter")

#faz a busca por um tma q
resultados =  tweepy.Cursor(api.search,q = "#ReformaDaPrevidência", result_type = "popular").items(150)


listaU = []
k = 0
listaT = []

for i in resultados: #pega todos usuarios e tweets
    listaU.append(i.user.screen_name)
    listaT.append(i)

usuarios = [Usuarios() for i in range(len(listaU))]

print("Pegou os usuarios e tweets")

for i in range(len(listaU)): #tira usuarios repetidos da minha lista
    c = contains(listaU[i],usuarios)
    if c == 0:
        usuarios[k].screen_name = listaU[i]
        k = k +1;

print("Tirou usuarios repetidos")

for i in listaT: #adiciona os tweets aos seus usuarios
    for j in range(k):
        if i.user.screen_name == usuarios[j].screen_name:
            usuarios[j].listaDeTweets.append(i)
            usuarios[j].citacoes = usuarios[j].citacoes + len(limit_handled(i.id,50))
            break

print("Adicionou os tweets aos seus usuarios")


with open("influentes.txt", 'w') as f: #1 - nome do usuario 2 - quantidade de retweets[se for 0 não foi retwwetado]
    for i in usuarios:
        if i.screen_name != "":
            c = str(i.citacoes)
            f.write("".join(i.screen_name + " " + c + "\n"))


print("Acabouuuuuu")