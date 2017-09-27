# -*- coding: UTF-8 -*-

import emoji
import csv
import string
import re

def get_sentiment_emoji_dict(csv_path):
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        emoji = next(reader, None)
        emojis = {}
        while emoji:
            code = emoji.pop('Unicode').encode()
            emojis[code] = emoji
            emoji = next(reader, None)
        return emojis

def extractEmojis(text):
    listaEmociones = (''.join(c for c in text if (unicode(c,'utf-8') in emoji.UNICODE_EMOJI)))
    return listaEmociones

def findEmotion(tweet):
    print(tweet)
    # Finds all regular expresions with the proper regex
    arrRegex = [a.encode('utf-8') for a in re.findall(u'[^\w\s,]',tweet.decode('utf-8'))]
    # Extrae los emojis del tweet
    emojiArr = extractEmojis(arrRegex)
    # Imprime el arreglo de emojis
    print("Emojis: " + emojiArr)
    # Separa el tweet solo considerando los espacios
    tweetArr = tweet.split()
    # Quita signos de puntuación del tweet
    table = string.maketrans("","")
    tweet =  tweet.translate(table, string.punctuation).replace("¡"," ").replace("¿"," ")
    # Crea un arreglo separado por el delimitador \\
    tweetArr = unicode(tweet, 'utf-8').encode('unicode_escape').split('\\')
    # Crea un arreglo con cada palabra y emoji
    arrPalabras=[]
    for t in tweetArr:
        for element in t.split():
            arrPalabras.append('\\'+element)
    #print(arrPalabras)
    # Crea el diccionario de sentimientos
    sentiments = get_sentiment_emoji_dict('emojis.csv')

    # Arreglo de las emociones del emoji
    # Alegria,Colera,Miedo,Tristeza,Amor,Sorpresa,Verguenza,Aversion
    arrEmociones = [0,0,0,0,0,0,0,0]

    # Diccionario con las polaridades según la posición del arrEmociones
    dictPolar = {0:'Positivo',1:'Negativo',2:'Negativo',3:'Negativo',
                  4:'Positivo',5:'Negativo',6:'Neutro',7:'Positivo'}

    # Incrementa la emoción en el arreglo de emociones por Emoji
    # Esto lo hace si el emoji encontrado está en nuestro diccionario
    for palabra in arrPalabras:
        if (palabra in sentiments):
            emojiDict = sentiments[palabra]
            arrEmociones[0]+=int(emojiDict['Alegria'])
            arrEmociones[1]+=int(emojiDict['Colera'])
            arrEmociones[2]+=int(emojiDict['Miedo'])
            arrEmociones[3]+=int(emojiDict['Tristeza'])
            arrEmociones[4]+=int(emojiDict['Amor'])
            arrEmociones[5]+=int(emojiDict['Sorpresa'])
            arrEmociones[6]+=int(emojiDict['Verguenza'])
            arrEmociones[7]+=int(emojiDict['Aversion'])

    # Devuelve la ponderación tomando la máxima emoción encontrada
    # Si hay más de una emoción máxima, toma la primera, porque max(arrEmociones)
    print("Ponderación: " + dictPolar[arrEmociones.index(max(arrEmociones))])

    # Diccionario con las emociones  según la posición del arrEmociones
    dictEmociones = {0:'Alegría',1:'Cólera',2:'Miedo',3:'Tristeza',
                  4:'Amor',5:'Sorpresa',6:'Vergüenza',7:'Aversión'}

    # Devuelve la emoción generalizada tomando la máxima emoción encontrada
    print("Emoción: " + dictEmociones[arrEmociones.index(max(arrEmociones))] + "\n\n")


def main():
    # Reads the Comma Separated Value and creates a list with the first 500
    tweets = open('yuyacst_tweets.csv', 'r')
    tweetList = tweets.readlines()
    for tweet in tweetList[:10]:
        findEmotion(tweet)
if __name__ == '__main__':
    main()

# Fuentes consultadas:
# https://stackoverflow.com/questions/43146528/how-to-extract-all-the-emojis-from-text
# https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
