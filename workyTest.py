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
subredditName = input("Para comenzar ingresa el nombre del subreddit que deseas clasificar:")

#Guarda el número de post que se van a clasificar
subredditLimit = input("Ahora ingresa el número de post que deseas clasificar:")

#Guarda las palabras que serás usadas como filtro
subredditFilter = input("Escribe las palabras con las que se clasificarán los post, separas por una coma (,)")
print('ESPERA, LOS POST SE ESTÁN AGRUPANDPO...')

#Cambia a mayúsculas las palabras que se usarán como filtro
subredditFilterUpper = subredditFilter.upper()

#Ordena el filtro alfabéticamente
filters = sorted(subredditFilterUpper.split(","))

#Guarda los post clasficados según los filtros
f_posts = {}

#Guarda el filtro que tiene más posts
popular_post = ['', 0]

#Crea el diccionaro asignando como llave los filtros y valor un arreglo vacío
for filter in filters:
	f_posts[filter] = []

#.hot corresponde al ordenamiento por 'hot' en Reddit 
#(si se quisiera extraer los post con ordenamiento 'new', se usa '.new(limit=100)'),
#limit corresponde a la cantidad de post que se obtienen
subreddit = reddit.subreddit(subredditName).hot(limit=int(subredditLimit))

filterSubreddit.filterSubreddit(subreddit, filters, f_posts)
print("POST ORDENADOS POR CATEGORIAS")
filterSubreddit.print_json(f_posts)
filterSubreddit.popularPost(filters,f_posts, popular_post)
print("CATEGORÍA MÁS POPULAR")
print(popular_post[0])
filterSubreddit.makeUpvote(f_posts, popular_post[0], reddit)