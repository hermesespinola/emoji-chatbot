#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re, string
from unidecode import unidecode

stopwords = ["0","1","2","3","4","5","6","7","8","9","_","a","actualmente","adelante","ademas","además","adrede","afirmó","agregó","ahi","ahora","ahí","al","algo","alguna","algunas","alguno","algunos","algún","alli","allí","alrededor","ambos","ampliamos","antano","antaño","ante","anterior","antes","apenas","aproximadamente","aquel","aquella","aquellas","aquello","aquellos","aqui","aquél","aquélla","aquéllas","aquéllos","aquí","arriba","arribaabajo","asegura","aseguró","asi","así","atras","aun","aunque","ayer","añadió","aún","b","bajo","breve","c","cada","casi","cerca","cierta","ciertas","cierto","ciertos","cinco","comentó","como","con","conmigo","conocer","conseguimos","conseguir","considera","consideró","consigo","consigue","consiguen","consigues","contigo","contra","cosas","creo","cual","cuales","cualquier","cuando","cuanta","cuantas","cuanto","cuantos","cuatro","cuenta","cuál","cuáles","cuándo","cuánta","cuántas","cuánto","cuántos","cómo","d","da","dado","dan","dar","de","debajo","debe","deben","debido","decir","dejó","del","delante","demás","dentro","deprisa","desde","despacio","despues","después","detras","detrás","dia","dias","dice","dicen","dicho","dieron","diferente","diferentes","dijeron","dijo","dio","donde","dos","durante","día","días","dónde","e","ejemplo","el","ella","ellas","ello","ellos","embargo","empleais","emplean","emplear","empleas","empleo","en","encima","encuentra","enfrente","enseguida","entonces","entre","era","erais","eramos","eran","eras","eres","es","esa","esas","ese","eso","esos","esta","estaba","estabais","estaban","estabas","estad","estada","estadas","estado","estados","estais","estamos","estan","estando","estar","estaremos","estará","estarán","estarás","estaré","estaréis","estaría","estaríais","estaríamos","estarían","estarías","estas","este","estemos","esto","estos","estoy","estuve","estuviera","estuvierais","estuvieran","estuvieras","estuvieron","estuviese","estuvieseis","estuviesen","estuvieses","estuvimos","estuviste","estuvisteis","estuviéramos","estuviésemos","estuvo","está","estábamos","estáis","están","estaba","estás","esté","estéis","estén","estés","ex","excepto","existe","existen","explicó","expresó","f","fin","final","fue","fuera","fuerais","fueran","fueras","fueron","fuese","fueseis","fuesen","fueses","fui","fuimos","fuiste","fuisteis","fuéramos","fuésemos","g","general","grandes","gt","gueno","h","ha","haber","habia","habida","habidas","habido","habidos","habiendo","habla","hablan","habremos","habrá","habrán","habrás","habré","habréis","habría","habríais","habríamos","habrían","habrías","habéis","había","habíais","habíamos","habían","habías","hace","haceis","hacemos","hacen","hacer","hacerlo","haces","hacia","haciendo","hago","han","has","hasta","hay","haya","hayamos","hayan","hayas","hayáis","he","hecho","hemos","hicieron","hizo","horas","hoy","hube","hubiera","hubierais","hubieran","hubieras","hubieron","hubiese","hubieseis","hubiesen","hubieses","hubimos","hubiste","hubisteis","hubiéramos","hubiésemos","hubo","i","igual","incluso","indicó","informo","informó","intenta","intentais","intentamos","intentan","intentar","intentas","intento","ir","j","junto","k","l","la","lado","largo","las","le","lejos","les","llegó","lleva","llego","llevar","lo","los","luego","lugar","m","manera","manifestó","mayor","me","mediante","medio","mencionó","menudo","mi","mia","mias","mientras","mio","mios","mis","misma","mismas","mismo","mismos","modo","momento","mí","mía","mías","mío","míos","n","nada","nadie","nos","nosotras","nosotros","nuestra","nuestras","nuestro","nuestros","nueva","nuevas","nuevo","nuevos","nunca","o","ocho","os","otra","otras","otro","otros","p","pais","para","parece","parte","partir","pasada","pasado","paìs","peor","pero","pesar","poca","pocas","poco","pocos","podeis","podemos","poder","podria","podriais","podriamos","podrian","podrias","podrá","podrán","podría","podrían","poner","por","por qué","porque","posible","primer","primera","primero","primeros","principalmente","pronto","propia","propias","propio","propios","proximo","próximo","próximos","pudo","pueda","puede","pueden","puedo","pues","q","qeu","que","quedó","quien","quienes","quiza","quizas","quizá","quizás","quién","quiénes","qué","r","raras","realizado","realizar","realizó","repente","respecto", "rt", "s","sabe","sabeis","sabemos","saben","saber","sabes","sal","salvo","se","sea","seamos","sean","seas","segun","segunda","segundo","según","seis","ser","sera","seremos","será","serán","serás","seré","seréis","sería","seríais","seríamos","serían","serías","seáis","señaló","sido","siempre","siendo","siete","sigue","siguiente","sino","sobre","sois","sola","solamente","solas","solo","solos","somos","son","soy","soyos","su","supuesto","sus","suya","suyas","suyo","suyos","sé","sólo","t","tal","tambien","también","tanto","tarde","te","temprano","tendremos","tendrá","tendrán","tendrás","tendré","tendréis","tendría","tendríais","tendríamos","tendrían","tendrías","tened","teneis","tenemos","tener","tenga","tengamos","tengan","tengas","tengo","tengáis","tenida","tenidas","tenido","tenidos","teniendo","tenéis","tenía","teníais","teníamos","tenían","tenías","tercera","ti","tiempo","tiene","tienen","tienes","toda","todas","todavia","todavía","todo","todos","total","trabaja","trabajais","trabajamos","trabajan","trabajar","trabajas","trabajo","tras","trata","través","tres","tu","tus","tuve","tuviera","tuvierais","tuvieran","tuvieras","tuvieron","tuviese","tuvieseis","tuviesen","tuvieses","tuvimos","tuviste","tuvisteis","tuviéramos","tuviésemos","tuvo","tuya","tuyas","tuyo","tuyos","tú","u","ultimo","un","una","unas","uno","unos","usa","usais","usamos","usan","usar","usas","uso","usted","ustedes","v","va","vais","valor","vamos","van","varias","varios","vaya","veces","ver","verdad","verdadera","verdadero","vez","vosotras","vosotros","voy","vuestra","vuestras","vuestro","vuestros","w","x","y","ya","yo","z","él","éramos","ésa","ésas","ése","ésos","ésta","éstas","éste","éstos","última","últimas","último","últimos"]


def word_histogram(iterable):
    hist = {}
    # dict_file = open('words.txt', 'r')
    #
    # words = { w.lower().strip(): 0 for w in dict_file }
    # dict_file.close()
    for line in iterable:
        line = iterable[0]
        for word in line.split(' '):
            # Clean word
            # word = ''.join(c for c in word if c.isalnum())
            word = word.lower().strip()
            # word = re.sub(r"(?:@\S*|#|http(?=.*://)\S*)", "", word)
            # tweetNoUrlMentionHash = re.sub(r"(?:@\S*|#|http(?=.*://)\S*)", "", word)
            # table = string.maketrans("","")
            # word = word.translate(table, string.punctuation).replace("¡","").replace("¿","").replace("RT ","").replace("...","") #Quita signos y url y mencion
            # word = unicode(word,"utf-8") #Convierte a unicode
            # word = unidecode(word).lower() #Quita acentos y emojis y pasa a minuscula
            # word = word_map[word] if word_map.has_key(word) else word
            # and words.has_key(word)
            # if word != '' and word not in stopwords:
            hist[word] = 1 if word not in hist else hist[word] + 1

    pairs = zip(hist.keys(), hist.values())
    return sorted(pairs, key=lambda pair: -pair[1])

def get_keys_sorted(iterable):
    hist = {}
    # dict_file = open('words.txt', 'r')
    #
    # words = { w.lower().strip(): 0 for w in dict_file }
    # dict_file.close()
    for line in iterable:
        print (line)
        line = iterable[0]
        for word in line.split(' '):
            if word != '' and word not in stopwords:
                hist[word] = 1 if word not in hist else hist[word] + 1

    pairs = zip(hist.iterkeys(), hist.itervalues())
    return map(lambda p: p[0], sorted(pairs, key=lambda pair: -pair[1]))

def get_column(file_path, col_name, expr = lambda x: x):
    f = open(file_path, 'r')
    # column names
    columns = f.readline().rstrip('\n').split('\t')
    idx = columns.index(col_name)
    iterable = [expr(line.rstrip('\n').split('\t')[idx]) for line in f]
    f.close()
    return iterable

def remove_outliers(linespace):
    s = sum(linespace)
    n = len(linespace)
    media = s / n
    std = 1 / (n - 1) * sum([(media - x) ^ 2 for x in linespace])
    # print (s, n, media, std)

if __name__ == '__main__':
    with open('yuyacst_tweets.csv') as f:
        for w in word_histogram(f):
            print(w)
    # likes = get_column('topcomments.tab', 'comment_like_count', lambda x: int(x))
    # pprint(likes)
    # remove_outliers(likes)
