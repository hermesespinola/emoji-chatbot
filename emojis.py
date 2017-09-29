# -*- coding: UTF-8 -*-

import emoji
import csv
import string
import re
import json
from unidecode import unidecode
from nltk import SnowballStemmer
from nltk import corpus

stemmer = SnowballStemmer('spanish')

# stopwords = corpus.stopwords.words('spanish')
stopwords = ["0","1","2","3","4","5","6","7","8","9","_","a","actualmente","adelante","ademas","además","adrede","afirmó","agregó","ahi","ahora","ahí","al","algo","alguna","algunas","alguno","algunos","algún","alli","allí","alrededor","ambos","ampliamos","antano","antaño","ante","anterior","antes","apenas","aproximadamente","aquel","aquella","aquellas","aquello","aquellos","aqui","aquél","aquélla","aquéllas","aquéllos","aquí","arriba","arribaabajo","asegura","aseguró","asi","así","atras","aun","aunque","ayer","añadió","aún","b","bajo","breve","c","cada","casi","cerca","cierta","ciertas","cierto","ciertos","cinco","comentó","como","con","conmigo","conocer","conseguimos","conseguir","considera","consideró","consigo","consigue","consiguen","consigues","contigo","contra","cosas","creo","cual","cuales","cualquier","cuando","cuanta","cuantas","cuanto","cuantos","cuatro","cuenta","cuál","cuáles","cuándo","cuánta","cuántas","cuánto","cuántos","cómo","d","da","dado","dan","dar","de","debajo","debe","deben","debido","decir","dejó","del","delante","demás","dentro","deprisa","desde","despacio","despues","después","detras","detrás","dia","dias","dice","dicen","dicho","dieron","diferente","diferentes","dijeron","dijo","dio","donde","dos","durante","día","días","dónde","e","ejemplo","el","ella","ellas","ello","ellos","embargo","empleais","emplean","emplear","empleas","empleo","en","encima","encuentra","enfrente","enseguida","entonces","entre","era","erais","eramos","eran","eras","eres","es","esa","esas","ese","eso","esos","esta","estaba","estabais","estaban","estabas","estad","estada","estadas","estado","estados","estais","estamos","estan","estando","estar","estaremos","estará","estarán","estarás","estaré","estaréis","estaría","estaríais","estaríamos","estarían","estarías","estas","este","estemos","esto","estos","estoy","estuve","estuviera","estuvierais","estuvieran","estuvieras","estuvieron","estuviese","estuvieseis","estuviesen","estuvieses","estuvimos","estuviste","estuvisteis","estuviéramos","estuviésemos","estuvo","está","estábamos","estáis","están","estaba","estás","esté","estéis","estén","estés","ex","excepto","existe","existen","explicó","expresó","f","fin","final","fue","fuera","fuerais","fueran","fueras","fueron","fuese","fueseis","fuesen","fueses","fui","fuimos","fuiste","fuisteis","fuéramos","fuésemos","g","general","grandes","gt","gueno","h","ha","haber","habia","habida","habidas","habido","habidos","habiendo","habla","hablan","habremos","habrá","habrán","habrás","habré","habréis","habría","habríais","habríamos","habrían","habrías","habéis","había","habíais","habíamos","habían","habías","hace","haceis","hacemos","hacen","hacer","hacerlo","haces","hacia","haciendo","hago","han","has","hasta","hay","haya","hayamos","hayan","hayas","hayáis","he","hecho","hemos","hicieron","hizo","horas","hoy","hube","hubiera","hubierais","hubieran","hubieras","hubieron","hubiese","hubieseis","hubiesen","hubieses","hubimos","hubiste","hubisteis","hubiéramos","hubiésemos","hubo","i","igual","incluso","indicó","informo","informó","intenta","intentais","intentamos","intentan","intentar","intentas","intento","ir","j","junto","k","l","la","lado","largo","las","le","lejos","les","llegó","lleva","llego","llevar","lo","los", "lt3","luego","lugar","m","manera","manifestó","mayor","me","mediante","medio","mencionó","menudo","mi","mia","mias","mientras","mio","mios","mis","misma","mismas","mismo","mismos","modo","momento","mí","mía","mías","mío","míos","n","nadie","nos","nosotras","nosotros","nuestra","nuestras","nuestro","nuestros","nueva","nuevas","nuevo","nuevos","nunca","o","ocho","os","otra","otras","otro","otros","p","pais","para","parece","parte","partir","pasada","pasado","paìs","peor","pero","pesar","poca","pocas","poco","pocos","podeis","podemos","poder","podria","podriais","podriamos","podrian","podrias","podrá","podrán","podría","podrían","poner","por","por qué","porque","posible","primer","primera","primero","primeros","principalmente","pronto","propia","propias","propio","propios","proximo","próximo","próximos","pudo","pueda","puede","pueden","puedo","pues","q","qeu","que","quedó","quien","quienes","quiza","quizas","quizá","quizás","quién","quiénes","qué","r","raras","realizado","realizar","realizó","repente","respecto", "rt", "s","sabe","sabeis","sabemos","saben","saber","sabes","sal","salvo","se","sea","seamos","sean","seas","segun","segunda","segundo","según","seis","ser","sera","seremos","será","serán","serás","seré","seréis","sería","seríais","seríamos","serían","serías","seáis","señaló","sido","siempre","siendo","siete","sigue","siguiente","sino","sobre","sois","sola","solamente","solas","solo","solos","somos","son","soy","soyos","su","supuesto","sus","suya","suyas","suyo","suyos","sé","sólo","t","tal","tambien","también","tanto","tarde","te","temprano","tendremos","tendrá","tendrán","tendrás","tendré","tendréis","tendría","tendríais","tendríamos","tendrían","tendrías","tened","teneis","tenemos","tener","tenga","tengamos","tengan","tengas","tengo","tengáis","tenida","tenidas","tenido","tenidos","teniendo","tenéis","tenía","teníais","teníamos","tenían","tenías","tercera","ti","tiempo","tiene","tienen","tienes","toda","todas","todavia","todavía","todo","todos","total","trabaja","trabajais","trabajamos","trabajan","trabajar","trabajas","trabajo","tras","trata","través","tres","tu","tus","tuve","tuviera","tuvierais","tuvieran","tuvieras","tuvieron","tuviese","tuvieseis","tuviesen","tuvieses","tuvimos","tuviste","tuvisteis","tuviéramos","tuviésemos","tuvo","tuya","tuyas","tuyo","tuyos","tú","u","ultimo","un","una","unas","uno","unos","usa","usais","usamos","usan","usar","usas","uso","usted","ustedes","v","va","vais","valor","vamos","van","varias","varios","vaya","veces","ver","verdad","verdadera","verdadero","vez","vosotras","vosotros","voy","vuestra","vuestras","vuestro","vuestros","w","x","y","ya","yo","z","él","éramos","ésa","ésas","ése","ésos","ésta","éstas","éste","éstos","última","últimas","último","últimos"]

def removeStopwords(tweet):
    return ' '.join(word for word in tweet.split() if word not in stopwords)

def cleanseTweet(tweet):
    tweet = ' '.join(word if word[0]!='#' else re.sub(r"\B([A-Z])", r" \1", word) for word in tweet.split())
    tweetNoUrlMentionHash = re.sub(r"(?:@\S*|#|http(?=.*://)\S*)", "", tweet)
    table = string.maketrans("","")
    tweetSinMarks = tweetNoUrlMentionHash.translate(table, string.punctuation).replace("¡","").replace("¿","").replace("RT ","").replace("...","").replace("lt3","") #Quita signos y url y mencion
    tweetUni = unicode(tweetSinMarks,"utf-8") #Convierte a unicode
    tweetSinAcento = unidecode(tweetUni).lower() #Quita acentos y emojis
    tweetSinHash =tweetSinAcento.replace("[?]","") #Quita los emojis o símbolos fantasma
    tweetSinEspacios = re.sub(' +',' ',tweetSinHash).strip(" ")
    tweetSinPuntos = re.sub('\.{3}', '', tweetSinEspacios)
    tweetSinStopWords = removeStopwords(tweetSinPuntos)
    return tweetSinStopWords

def get_sentiment_emoji_dict(csv_path):
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        emoji = next(reader, None)
        emojis = {}
        while emoji:
            code = emoji.pop('Unicode').encode()
            emojis[code.lower()] = emoji
            emoji = next(reader, None)
        return emojis

def extractEmojis(text):
    listaEmociones = [c for c in text if (unicode(c,'utf-8') in emoji.UNICODE_EMOJI)]
    return listaEmociones

def separateTweetEmojis(tweet):
    # Finds all regular expresions with the proper regex
    arrRegex = [a.encode('utf-8') for a in re.findall(u'[^\w\s,]',tweet.decode('utf-8'))]
    return extractEmojis(arrRegex), cleanseTweet(tweet)

default_sentiment = {
    'Alegria': 0,
    'Colera': 0,
    'Miedo': 0,
    'Tristeza': 0,
    'Amor': 0,
    'Sorpresa': 0,
    'Verguenza': 0,
    'Aversion': 0
}

def emojisSentiment(emojis, sentiments):
    arr_sent=[]
    for e in emojis:
        e_repr = repr(unicode(e, 'utf-8'))[2:-1].lower()
        sent = sentiments.get(e_repr, default_sentiment)
        arr_sent.append(sent)

    arrEmociones = [0] * 8
    dictPolar = {0:'Positivo',1:'Negativo',2:'Negativo',3:'Negativo',
                  4:'Positivo',5:'Positivo',6:'Neutro',7:'Negativo'}
    for sent in arr_sent:
        arrEmociones[0]+=int(sent['Alegria'])
        arrEmociones[1]+=int(sent['Colera'])
        arrEmociones[2]+=int(sent['Miedo'])
        arrEmociones[3]+=int(sent['Tristeza'])
        arrEmociones[4]+=int(sent['Amor'])
        arrEmociones[5]+=int(sent['Sorpresa'])
        arrEmociones[6]+=int(sent['Verguenza'])
        arrEmociones[7]+=int(sent['Aversion'])

    maxEmocion = arrEmociones.index(max(arrEmociones))
    if max(arrEmociones) != 0:
        # Devuelve la ponderación tomando la máxima emoción encontrada
        # Si hay más de una emoción máxima, toma la primera, porque max(arrEmociones)
        print("Polaridad Emoji: " + dictPolar[maxEmocion])

        # Diccionario con las emociones  según la posición del arrEmociones
        dictEmociones = {0:'Alegría',1:'Cólera',2:'Miedo',3:'Tristeza',
                      4:'Amor',5:'Sorpresa',6:'Vergüenza',7:'Aversión'}

        # Devuelve la intensidad del emoji, porcentualmente
        suma = 0
        for i in arrEmociones:
            suma+=i

        # Devuelve la emoción generalizada tomando la máxima emoción encontrada
        return dictEmociones[maxEmocion], float(arrEmociones[maxEmocion])/float(suma)*100
        #print(dictEmociones[maxEmocion])
    else:
        return "Neutro", 0

def cleanWord(tweet):
    # Separa el tweet solo considerando los espacios
    tweetArr = tweet.split()
    # Quita signos de puntuación del tweet
    table = string.maketrans("","")
    tweet =  tweet.translate(table, string.punctuation).replace("¡"," ").replace("¿"," ")
    tweet = re.sub(r'\d+', ' numero ', tweet)
    # Crea un arreglo separado por el delimitador \\
    tweetArr = unicode(tweet, 'utf-8').encode('unicode_escape').split('\\')
    # Crea un arreglo con cada palabra y emoji
    arrPalabras=[]
    for t in tweetArr:
        for element in t.split():
            arrPalabras.append(stemmer.stem(element))
    return arrPalabras

    # Ahora analizamos la emoción por cada palabra del tweet normalizado
    # Arreglo de polaridades acumuladas por tweet
    # Positivo, Negativo, Neutro
    arrPolaridadGeneral = [0,0,0]
    arrCleanTweet = clntweet.split()
    for word in arrCleanTweet:
        if word in polarity:
            polaridad = polarity[word]
            if polaridad == 'positivo':
                arrPolaridadGeneral[0]+=1
            elif polaridad == 'negativo':
                arrPolaridadGeneral[1]+=1
            elif polaridad == 'neutro':
                arrPolaridadGeneral[2]+=1

    if max(arrPolaridadGeneral) != 0:
        # Devuelve la máxima polaridad
        maxPolaridad = arrPolaridadGeneral.index(max(arrPolaridadGeneral))
        if maxPolaridad == 0:
            print("Polaridad Texto: Positivo")
        elif maxPolaridad == 1:
            print("Polaridad Texto: Negativo")
        elif maxPolaridad == 2:
            print("Polaridad Texto: Neutro")

        # Devuelve la intensidad del texto, porcentualmente
        suma = 0
        for i in arrPolaridadGeneral:
            suma+=i
        print("Intensidad Texto: %.2f"%(float(arrPolaridadGeneral[maxPolaridad])/float(suma)*100)+"%")
    else:
        print("Polaridad Texto: Neutro")
        print("Intensidad Texto: 0%")


    #print(arrPolaridadGeneral)
    for c in dictPolar:
        if dictPolar[c] == 'Positivo':
            arrPolaridadGeneral[0]+=arrEmociones[c]
        elif dictPolar[c] == 'Negativo':
            arrPolaridadGeneral[1]+=arrEmociones[c]
        else:
            arrPolaridadGeneral[2]+=arrEmociones[c]

    if max(arrPolaridadGeneral) != 0:
        # Devuelve la máxima polaridad
        maxPolaridad = arrPolaridadGeneral.index(max(arrPolaridadGeneral))
        if maxPolaridad == 0:
            print("Polaridad emojis: Positivo")
        elif maxPolaridad == 1:
            print("Polaridad emojis: Negativo")
        elif maxPolaridad == 2:
            print("Polaridad emojis: Neutro")
    else:
        print("Polaridad Tweet: Neutro")
        print("Intensidad Tweet: 0%")


def main():
    sentiments = get_sentiment_emoji_dict('emojis.csv')
    tweets = open('yuyacst_tweets.csv', 'r')

    tweetsArr = tweets.readlines()
    for tweet in tweetsArr:
        findEmotion(tweet, sentiments)

    clean_emojis.close()
    clean_tweets.close()

if __name__ == '__main__':
    main()

# Fuentes consultadas:
# https://stackoverflow.com/questions/43146528/how-to-extract-all-the-emojis-from-text
# https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
