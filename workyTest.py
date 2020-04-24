#Python Reddit API Wrapper
import praw
import filterSubreddit

#Obtiene una instancia de Reddit
reddit = praw.Reddit(  client_id = 'RPjn4fqZlJqniA',
                       client_secret = 'T_sp_HWEx-BpyYf4LXmh4LVD7YU',
                       user_agent = 'worky.tech.test.lmpg',
                       #Para poder generar el upvote se deben agregar las credenciales de la cuenta
                       username = 'luudz',
                       password = 'pruebaWorky'
                     )

print("BIENVENIDO AL CLASIFICADOR DE POST DE REDDIT")

#Guarda el nombre del subreddit que se va a clasificar
subredditName = input("Para comenzar ingresa el nombre del subreddit que deseas clasificar:\n")

#Guarda el número de post que se van a clasificar
subredditLimit = input("Ahora ingresa el número de post que deseas clasificar:\n")

#Guarda las palabras que serás usadas como filtro
subredditFilter = input("Escribe las palabras con las que se clasificarán los post, separadas por una coma (,)\n")

#Cambia a mayúsculas las palabras que se usarán como filtro
subredditFilterUpper = subredditFilter.upper().split(",")
#Crea un copia para los filtros unificados
groups = subredditFilterUpper.copy()

print("¿Te gustaría unificar algunos filtos?")
#Guarda la respuesta
joinFilter = input("Escribe 'SI' o 'NO'\n")

#Guarda los grupos de filtros unificados
filterGroup = {}
#Crea el diccionario de filtros unificados
while joinFilter.upper() == 'SI':
	filterGroupValue = input("Escribe los filtros que vas a unificar, separados por una coma (,)\n")
	filterGroupKey = input("Escribe el nombre con el que te gustaría agregarlos\n")
	filterGroup[filterGroupKey.upper()] = filterGroupValue.upper().split(",")
	print("¿Te gustaría unificar otros filtos?")
	joinFilter = input("Escribe 'SI' o 'NO'\n")

#Crea la lista excluyen los filtros que se unificaron y agregando el filtro que los agrupa
for filter in subredditFilterUpper:
	for group in filterGroup:
		if filter in filterGroup[group]:
			groups.remove(filter)
			if group not in groups:
				groups.append(group)


print('ESPERA, LOS POST SE ESTÁN AGRUPANDPO...')

#Ordena el filtro alfabéticamente
sortedFilters = sorted(groups)

#Guarda los post clasficados según los filtros
f_posts = {}

#Guarda el filtro que tiene más posts
popular_post = ['', 0]

#Crea el diccionaro asignando como llave los filtros y valor un arreglo vacío
for filter in sortedFilters:
	f_posts[filter] = []

#.hot corresponde al ordenamiento por 'hot' en Reddit 
#(si se quisiera extraer los post con ordenamiento 'new', se usa '.new(limit=100)'),
#limit corresponde a la cantidad de post que se obtienen
subreddit = reddit.subreddit(subredditName).hot(limit=int(subredditLimit))

filterSubreddit.filterSubreddit(subreddit, subredditFilterUpper, f_posts, filterGroup)
print("POST ORDENADOS POR CATEGORIAS")
filterSubreddit.print_json(f_posts)
filterSubreddit.popularPost(sortedFilters,f_posts, popular_post)
print("CATEGORÍA MÁS POPULAR")
print(popular_post[0])
filterSubreddit.makeUpvote(f_posts, popular_post[0], reddit)


