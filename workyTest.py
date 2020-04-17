#Python Reddit API Wrapper
import praw

#Obtiene una instancia de Reddit
reddit = praw.Reddit(  client_id = '_SoK1EYN-0Hfnw',
                       client_secret = 'UzlixDpdcrUeupUNFbsxuo9Wk6E',
                       user_agent = 'worky.tech.test.lmpg'
                     )

#.hot corresponde al ordenamiento por 'hot' en Reddit 
#(si se quisiera extraer los post con ordenamiento 'new', se usa '.new(limit=100)'),
#limit corresponde a la cantidad de post que se obtienen
subreddit = reddit.subreddit('lotr').hot(limit=100)

#Filtros para  separar los post por hobbit
filters = ['FRODO', 'BILBO', 'SAMSAGAZ',
           'SAM', 'MERIADOC', 'MERRY',
           'PEREGRIN', 'PIPPIN', 'SMEAGOL',
           'GOLLUM']

#Es el objeto que contiene los resultados del filtrado   
f_hobbits = {
    'FRODO': [],
    'BILBO': [],
    'SAM': [],
    'MERRY': [],
    'PIPPIN': [],
    'GOLLUM': []
}

for post in subreddit:
    for hobbit in filters:
        if hobbit in post.title.upper():
            if hobbit == 'SAMSAGAZ':
                f_hobbits['SAM'].append(post.title)
            elif hobbit == 'MERIADOC':
                f_hobbits['MERRY'].append(post.title)
            elif hobbit == 'SMEAGOL':
                f_hobbits['GOLLUM'].append(post.title)
            else:    
                f_hobbits[hobbit].append(post.title)

print(f_hobbits)
