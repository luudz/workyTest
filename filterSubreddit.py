#Clasifica los post por los filtros
def filterSubreddit(subreddit, filters, f_posts):
    for post in subreddit:
        for f in filters:
            if f in post.title.upper():
                f_posts[f].append(post)

#Obtiene el filtro con más post
def popularPost(filters, f_posts, popular_post):
    for post in f_posts:
        if len(f_posts[post]) == popular_post[1]:
            if popular_post[0] == '':
                popular_post[0] = post
            elif filters.index(post) < filters.index(popular_post[0]):
                popular_post[0] = post
        elif len(f_posts[post]) > popular_post[1]:
            popular_post[0] = post
            popular_post[1] = len(f_posts[post])

#Hace el upvote a los post del filtro más popular
def makeUpvote(f_posts, popular_post, reddit):
    for post in f_posts[popular_post]:
        submission = reddit.submission(id=post.id)
        submission.upvote()	

#Imprime en formato json los post agupados por los filtros
def print_json(f_posts):
    print('{')
    for post in f_posts:
        print('\t' + post + ": [")
        for post in f_posts[post]:
            print('\t\t' + post.title + ',')
        print('\t]')
    print('}')
