import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that came to life",
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Toy_Story.svg/1280px-Toy_Story.svg.png",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.impawards.com/2009/posters/avatar_xlg.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")
#print(avatar.storyline)
#avatar.show_trailer()

revolver = media.Movie("Revolver",
                       "Guy Ritchie, just fucking with your mind. And doing a mighty fine job",
                       "http://www.impawards.com/2007/posters/revolver_ver2.jpg",
                       "https://www.youtube.com/watch?v=e3REQGksaVE")
#revolver.show_trailer()
movies = [toy_story, avatar, revolver]

def main():
    fresh_tomatoes.open_movies_page(movies)

if __name__ == "__main__":
    # execute only if run as a script
    main()


#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)