#Python Reddit API Wrapper
import praw

#Obtiene una instancia de Reddit
reddit = praw.Reddit(  client_id = 'RPjn4fqZlJqniA',
                       client_secret = 'T_sp_HWEx-BpyYf4LXmh4LVD7YU',
                       user_agent = 'worky.tech.test.lmpg',
                       #Para poder generar el upvote se deben agregar las credenciales de la cuenta
                       username = 'luudz',
                       password = 'pruebaWorky'
                     )

#.hot corresponde al ordenamiento por 'hot' en Reddit 
#(si se quisiera extraer los post con ordenamiento 'new', se usa '.new(limit=100)'),
#limit corresponde a la cantidad de post que se obtienen
subreddit = reddit.subreddit('lotr').hot(limit=100)

print('ESPERA, LOS POST SE ESTÁN AGRUPANDPO...')

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

#Guarda la lista de hobbits con más post
popular_hobbit = ['',0]

#Guarda los hobbits ordenados alfabéticamente
hobbits = ['BILBO', 'FRODO', 'GOLLUM', 'MERRY', 'PIPPIN', 'SAM']

#Filtra los post por hobbit
for post in subreddit:
    for hobbit in filters:
        if hobbit in post.title.upper():
            if hobbit == 'SAMSAGAZ':
                f_hobbits['SAM'].append(post)
            elif hobbit == 'MERIADOC':
                f_hobbits['MERRY'].append(post)
            elif hobbit == 'SMEAGOL':
                f_hobbits['GOLLUM'].append(post)
            else:    
                f_hobbits[hobbit].append(post)

#Obtiene el/los hobbit(s) con más post
for hbt in f_hobbits:
    if len(f_hobbits[hbt]) == popular_hobbit[1]:
    	new_popular = hobbits.index(hbt)
    	current_popular = hobbits.index(popular_hobbit[0])
    	if new_popular < current_popular:
    		popular_hobbit[0] = hbt
    elif len(f_hobbits[hbt]) > popular_hobbit[1]:
        popular_hobbit[0] = hbt
        popular_hobbit[1] = len(f_hobbits[hbt])

#Hace el upvote a los post del hobbit más popular
for post in f_hobbits[popular_hobbit[0]]:
    submission = reddit.submission(id=post.id)
    submission.upvote()	

#imprime en json los post agupados por hobbit
def print_json():
    print('{')
    for hobbit in f_hobbits:
        print('\t' + hobbit + ": [")
        for post in f_hobbits[hobbit]:
            print('\t\t' + post.title + ',')
        print('\t]')
    print('}')

print('POST AGRUPADOS POR HOBBIT:')
print_json()
print('EL HOBBIT MÁS POPULAR ES:')
print(popular_hobbit[0])
