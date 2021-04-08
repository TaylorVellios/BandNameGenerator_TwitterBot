# band name generator 2
from os import name
import random
import genre_lists as GL


#pull_noun() returns a tuple - [0] for random any/ [1] for shorter in length
def pull_noun():
    n = open('resources/noun_list.txt','r')
    f = [i.strip('\n') for i in n]
    shorter = [i for i in f if len(i)<5]
    noun = random.choice(f)
    short = random.choice(shorter)
    n.close()
    return noun.capitalize() , short.capitalize()

#pull_verb() returns a tuple - [0] for random any/ [1] for shorter in length
def pull_verb():
    n = open('resources/verb_list.txt','r')
    f = [i.strip('\n') for i in n]
    shorter = [i for i in f if len(i)<6]
    verb = random.choice(f)
    short_v = random.choice(shorter)
    n.close()
    return verb.capitalize(), short_v.capitalize()

#Adjectives - Returns a Capitalized Single Word
def pull_adj():
    n = open('resources/adjective_list.txt','r')
    f = [i.strip('\n') for i in n]
    shorter = [i for i in f if len(i)<=5]
    adjective = random.choice(f)
    short_adj = random.choice(shorter)
    n.close()
    return (adjective.capitalize(), short_adj.capitalize())

#Adverbs - Returns a Capitalized Single Word
def pull_adverb():
    n = open('resources/adverb_list.txt','r')
    f = [i.strip('\n') for i in n]
    adverb = random.choice(f)
    n.close()
    return adverb.capitalize()

#returning a list of articles, pull_art()[0] to be used before an adjective/pull_art()[1] before a verb - [2] before a noun -- outputs are NOT capitalized
def pull_art(adj,verb,short_verb,noun, short_noun):
    art0 = ''
    art1 = ''
    art2 = ''
    art3 = ''
    arts = ['a','the']
    plur = 'an'
    if adj[0] in 'AEIOUaeiou':
        art0 = plur
    else:
        art0 = random.choice(arts)

    if short_verb[0] in 'AEIOUaeiou':
        art1 = plur
    else:
        art1 = random.choice(arts)

    if noun.endswith('s'):
        art2 = 'the'
    elif noun[0] in 'AEIOU':
        art2 = plur
    else:
        art2 = 'a'

    if short_noun.endswith('s'):
        art3 = 'the'
    elif noun[0] in 'AEIOU':
        art3 = plur
    else:
        art3 = 'a'

    return art0, art1, art2, art3

#Prepositions - Returns a Capitalized Single Word
def pull_prep():
    n = open('resources/prep_list.txt','r')
    f = [i.strip('\n') for i in n]
    prep = random.choice(f)
    n.close()
    return prep.capitalize()


#First Names, returns a name object and several alliterative options
def make_solo_artist():
    name_list = open('resources/first_names.txt')
    n_list = open('resources/noun_list.txt')
    name = random.choice([i.strip('\n') for i in name_list])
    nouns = [i.strip('\n').capitalize() for i in n_list if len(i)<=7]
    filtered = [i for i in nouns if i.startswith(name[0])]
    name_list.close()
    n_list.close()
    return name, random.choice(filtered)

def make_indie_aesthetic():
    adj = pull_adj()[0].upper()
    noun = pull_noun()[0].upper()
    rm_adj = [i for i in adj if i not in 'AEIOU']
    rm_noun = [i for i in noun if i not in 'AEIOU']
    return (f"{''.join(rm_adj)} {''.join(rm_noun)}", f"{adj} {noun}" )

#make_baseball_team returns an entire f-string
def make_baseball_team():
    cities = [i.strip('\n') for i in open('resources/city_names.txt')]
    get_city = random.choice(cities)
    nouns = [i.strip('\n') for i in open('resources/noun_list.txt') if i[0].lower()==get_city[0].lower()]
    get_noun = random.choice(nouns)
    plur_n = make_plural_noun(get_noun)
    return f'The {get_city} {plur_n.capitalize()}'

#Function to force a noun to be plural
def make_plural_noun(noun):
    plural_n = ''
    if noun[-1]!='s':
        if noun.endswith('oy'):
            plural_n = noun + 'ees'
        elif noun[-1]=='y':
            plural_n = noun[:-1] +'ies'
        elif noun.endswith('ch') or noun.endswith('x'):
            plural_n = noun + 'es'
        else:
            plural_n = noun + 's'
    else:
        plural_n = noun
    return plural_n


#MAIN NAME BUILD FUNCTION - RETURNS A LIST OF TUPLES
def make_name_1():

    nouns = pull_noun()
    noun = nouns[0]
    short_noun = nouns[1]

    nouns_2 = pull_noun()
    noun2 = nouns_2[0]
    short_noun_2 = nouns_2[1]


    verbs = pull_verb()
    verb = verbs[0]
    short_verb = verbs[1]


    adjectives = pull_adj()
    ad = adjectives[0] 
    short_adj = adjectives[1]

    art = pull_art(ad,verb,short_verb,noun,short_noun)
    art_pre_adj = art[0]
    art_pre_verb = art[1]
    art_pre_noun = art[2]
    art_pre_short_noun = art[3]

    
    prep = pull_prep()
    adverb = pull_adverb()

    solo = make_solo_artist()

    current_v = ''                      #Controlling Tense With What pull_verb() outputs
    if not verb.endswith('ing'):
        if verb.endswith('e') or verb.endswith('ie'):
            current_v = verb[:-1] + 'ing'
        elif verb[-2] != verb[-1] and verb[-2] in 'aeiouAEIOU' and verb[-3] in 'aeiouAEIOU':
            current_v = verb + 'ing'
        elif verb[-2:] not in ['st','ct','nd','ng','rt','rd','lt','sh','fy','ax'] and verb[-2] != verb[-1]:
            current_v = verb + verb[-1] + 'ing'
        else:
            current_v = verb + 'ing'
    else:
        current_v = verb


    past_verb = ''
    if  not short_verb.endswith('ed'):
        if short_verb.endswith('y') and short_verb[-2] not in 'aeiouAEIOU':
            past_verb = short_verb[:-1] + 'ied'
        elif short_verb[-2] != short_verb[-1] and short_verb[-2] in 'aeiouAEIOU' and short_verb[-3] in 'aeiouAEIOU':
            past_verb = short_verb + 'ed'
        elif short_verb[-2] != short_verb[-1] and short_verb[-2] in 'aeiouAEIOU' and short_verb[-1] not in 'wh':
            past_verb = short_verb + short_verb[-1] + 'ed'            
        elif short_verb.endswith('e'):
            past_verb = short_verb + 'd'
        else:
            past_verb = short_verb + 'ed'
    else:
        past_verb = short_verb

    plural_n = make_plural_noun(noun)

    singular_noun = ''
    if noun[-1]=='s':
        singular_noun = noun[:-1]
    else:
        singular_noun = noun

    short_plural_n = ''                     
    if short_noun[-1]!='s':
        if short_noun.endswith('y'):
            short_plural_n = short_noun.replace('y','ies')
        elif short_noun.endswith('ch'):
            short_plural_n = short_noun + 'es'
        else:
            short_plural_n = short_noun + 's'

    #just for memes
    family = ['Mom', 'Dad', 'Boy', 'Girl']
    start_pronouns = ['We', 'They', 'He', 'She']
    end_pronouns = ['Him','Her','Them','Me','Us']

    rapper_pref = ['Yung', 'Lil', 'Big', 'Thicc', 'MC', 'Professor']
    rapper = random.choice(rapper_pref)

    hard = random.choice(GL.genre_hard)
    rap = random.choice(GL.genre_rap)
    mid = random.choice(GL.genre_mid)
    soft = random.choice(GL.genre_soft)

    metalcore1 = (f'{verb} the {noun}', hard)
    metalcore2 = (f'{verb} {prep} the {noun}', hard)
    metalcore3 = (f'{prep} {art_pre_adj} {ad} {noun}', hard)

    vowelless_band = make_indie_aesthetic()

    indie1 = (f'The {plural_n}', mid)
    indie2 = (f'{art_pre_verb.capitalize()} {past_verb} {singular_noun}', mid)
    indie3 = (f'The {past_verb}', mid)
    indie4 = (f'{current_v} {prep} {art_pre_noun} {noun}', mid)
    indie5 = (f'{noun} {short_plural_n}', mid)
    indie6 = (f'{ad} {noun}', mid)
    indie7 = (f'{current_v} {adverb}', mid)
    indie8 = (f"{vowelless_band[0]} ({vowelless_band[1]})",mid) 

    skramz1 =(short_noun+short_verb.lower(), hard)
    skramz2 = (f'{prep} {art_pre_noun} {noun}', hard)

    rapper1 = (f'{rapper} {short_noun}', rap)
    rapper2 = (f'{short_noun}mane', rap)
    rapper3 = (f'{rapper} {solo[0]}',rap)
    rapper4 = (f'{solo[0]} {solo[1]}',f"{solo[0]}'s Solo Project")

    emo1 = (f'{random.choice(family)} {plural_n}', 'Midwest Emo Band')
    emo2 = (f'{short_adj} {plural_n}', mid)

    pop_punk1 = (f'{art_pre_noun.capitalize()} {noun} {" ".join([i.capitalize() for i in prep.split()])} {art_pre_adj} {ad} {short_noun}', soft)
    pop_punk2 = (f'{art_pre_noun.capitalize()} {noun} {" ".join([i.capitalize() for i in prep.split()])} {random.choice(end_pronouns)}', soft)

    long_1 = (f'{random.choice(start_pronouns)} {past_verb} {art_pre_noun} {noun}', soft)
    long_2 = (f'{art_pre_noun.capitalize()} {noun} is {art_pre_adj} {ad} {noun2}', mid)
    
    sports = (make_baseball_team(), 'Sports Team? idk..')

    return [metalcore1,metalcore2,metalcore3,
    indie1,indie2,indie3,indie4,indie5,indie6,indie7,indie8,
    skramz1,skramz2,
    rapper1,rapper2,rapper3,rapper4,
    emo1,emo2,pop_punk1,pop_punk2,
    long_1,long_2,]



for i in make_name_1():
    print(i)