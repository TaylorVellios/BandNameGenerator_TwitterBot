# band name generator 2
import random
from datetime import date, datetime
import tweepy
import webbrowser

import sched, time
s = sched.scheduler(time.time, time.sleep)

from config import api_key, api_secret, bearer_token

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

    return art0, art1, art2

#Prepositions - Returns a Capitalized Single Word
def pull_prep():
    n = open('resources/prep_list.txt','r')
    f = [i.strip('\n') for i in n]
    prep = random.choice(f)
    n.close()
    return prep.capitalize()

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

    art = pull_art(ad,verb,short_verb,noun)
    art_pre_adj = art[0]
    art_pre_verb = art[1]
    art_pre_noun = art[2]
    art_pre_short_noun = art[3]


    prep = pull_prep()
    adverb = pull_adverb()

    current_v = ''                      #Controlling Tense With What pull_verb() outputs
    if not verb.endswith('ing'):
        if verb.endswith('e') or verb.endswith('ie'):
            current_v = verb[:-1] + 'ing'
        elif verb[-2] != verb[-1] and verb[-2] in 'aeiouAEIOU' and verb[-3] in 'aeiouAEIOU':
            current_v = verb + 'ing'
        elif verb[-2:] not in ['st','ct','nd','ng','rt','rd','lt','sh'] and verb[-2] != verb[-1]:
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

    genre_hard = ['Metalcore Band', 'Metalcore BoyBand', 'Primus Cover Band', 'Prog Metal Solo Project', 'Christian Metal Band', 'Early 2000s Rap Metal Group',
                    'Communist Labor Metal Band', 'Djent Band With Nice Haircuts', 'Stoner Metal', 'Skramz Band', 'Emotive Hardcore Band', 'Hardcore Band',
                    'Band That Wants to be Hard but Doesnt Tune Lower Than Drop D', 'classic Metal Band That Listens to Joe Rogan More Than They Practice',
                    'Band That Refuses to Take Off Their Oakley Sunglasses Inside', 'Costumed Gimmick Band']

    genre_rap = ['Soundcloud Rapper', 'Emo Rapper', 'Alias for Someone that Listened to GBC Once', 'UK Grime Alias', 'Political Hip Hop Alias', 'West Coast Rapper',
                    'Jewish Hip Hop Alias', 'Mumble Rapper', 'East Coast Rapper', 'Youtube Comments Beggar Rapper', 'Bounce DJ']

    genre_mid = ['Indie Band', 'Alternative Rock Band', 'Emo Band', 'Wedding Cover-Band Name', 'Indie Band Where Everyone Wears a Flat Brimmed Hat', 'Shoegaze Band', 
                    'Post Punk Band', 'New Wave Revival Band', 'Slacker Rock Band', 'Wishes-They-Were-Nirvana 2.0 Band', "Band That Doesn't Need The Keyboard Player",
                    'Local Band That Invites Everyone in their FB Friends List to Show Events']

    genre_soft = ['Guy That Plays Ukelele', 'Soft Rock Band With Excessive Pentatonic Riffage', 'Dad Rock Band', 'Blues Dad Band', 
                    'Radio-Rock Band That Tours With 3 Guitar Players and They All Play Strats', 'A Pop Band That INSISTS They are a Rock Band', 
                    'High School Talent Show Performance', 'Bon Jovi Cover Band', 'Band That Plays Way too Soft to be Wearing That Leather Vest',
                    'Aging Rock Band In Divorce Debt']

    hard = random.choice(genre_hard)
    rap = random.choice(genre_rap)
    mid = random.choice(genre_mid)
    soft = random.choice(genre_soft)

    metalcore1 = (f'{verb} the {noun}', hard)
    metalcore2 = (f'{verb} {prep} the {noun}', hard)
    metalcore3 = (f'{prep} {art_pre_adj} {ad} {noun}', hard)

    indie1 = (f'The {plural_n}', mid)
    indie2 = (f'{art_pre_verb.capitalize()} {past_verb} {singular_noun}', mid)
    indie3 = (f'The {past_verb}', mid)
    indie4 = (f'{current_v} {prep} {art_pre_noun} {noun}', mid)
    indie5 = (f'{noun} {short_plural_n}', mid)
    indie6 = (f'{ad} {noun}', mid)
    indie7 = (f'{current_v} {adverb}', mid)

    skramz1 =(short_noun+short_verb.lower(), hard)
    skramz2 = (f'{prep} {art_pre_noun} {noun}', hard)

    rapper1 = (f'{rapper} {short_noun}', rap)
    rapper2 = (f'{short_noun}mane', rap)

    emo1 = (f'{random.choice(family)} {plural_n}', 'Midwest Emo Band')
    emo2 = (f'{short_adj} {plural_n}', mid)

    pop_punk1 = (f'{art_pre_noun.capitalize()} {noun} {" ".join([i.capitalize() for i in prep.split()])} {art_pre_adj} {ad} {short_noun}', soft)
    pop_punk2 = (f'{art_pre_noun.capitalize()} {noun} {" ".join([i.capitalize() for i in prep.split()])} {random.choice(end_pronouns)}', soft)

    long_1 = (f'{random.choice(start_pronouns)} {past_verb} {art_pre_noun} {noun}', soft)
    long_2 = (f'{art_pre_noun.capitalize()} {noun} is {art_pre_adj} {ad} {noun2}', mid)
    
    sports = (make_baseball_team(), 'Sports Team? idk..')

    return [metalcore1,metalcore2,metalcore3,
    indie1,indie2,indie3,indie4,indie5,indie6,indie7,
    skramz1,skramz2,
    rapper1,rapper2,
    emo1,emo2,pop_punk1,pop_punk2,
    long_1,long_2,
    sports]


#Twitter Stuff
twitter_callback = 'oob'
auth = tweepy.OAuthHandler(api_key, api_secret, twitter_callback)
redirect_url = auth.get_authorization_url()

login = True
while login:
    webbrowser.open(redirect_url)
    print()
    user_pin = input('Enter the Pin from the Twitter Auth Pop-Up: ')
    print()
    try:
        auth.get_access_token(user_pin)
        print()
        print('Tokens Confirmed')
        login = False
    except:
        print('Pin Number INVALID. Please Try Again\n')

api = tweepy.API(auth)
me = api.me()
print(f'Confirming Tokens for user: {me.screen_name}\n'
        f'Access Token: {auth.access_token}\n'
        f'Access Token Secret: {auth.access_token}\n')

divider = '--------------------------------------------------------------'
print(divider)


def get_name_and_tweet():
    right_now = datetime.now()
    output = random.choice(make_name_1())

    band_name = output[0]
    genre = output[1]

    tweet_string = ''
    if genre[0].upper() in 'AEIOU':
        tweet_string = f'For an {genre}:\n{band_name}'
    else:
        tweet_string = f'For a {genre}:\n{band_name}'

    print(f'Tweeting at {right_now}: \n{tweet_string}')
    api.update_status(tweet_string)
    print(divider)
    s.enter(7400,1, get_name_and_tweet)


s.enter(1,1, get_name_and_tweet)
s.run()

s.cancel()