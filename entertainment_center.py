import fresh_tomatoes
import media

#create movie objects for movie library
coffee = media.Movie("Coffee & Cigarettes",
                     "People drink coffee and smoke cigarettes.",
                     "https://www.movieposter.com/posters/archive/main/64/MPW-32218",
                     "https://www.youtube.com/watch?v=mM6Mpn0-eyQ")
down = media.Movie("Down By Law",
                   "Prison break...",
                   "http://images.moviepostershop.com/down-by-law---movie-poster-1986-1020194501.jpg",
                   "https://www.youtube.com/watch?v=1H9zlFH7UhA")
ghost_dog = media.Movie("Ghost Dog",
                        "Ghostface Killah does things.",
                        "https://www.movieposter.com/posters/archive/main/66/MPW-33348",
                        "https://www.youtube.com/watch?v=Rml5ehAl7SM")
dead_man = media.Movie("Dead Man",
                       "William Blake shoots people.",
                       "https://www.movieposter.com/posters/archive/main/27/A70-13824",
                       "https://www.youtube.com/watch?v=_64Qv0jV_PY")
broken_flowers = media.Movie("Broken Flowers",
                        "Bill Murray searches for something...",
                        "https://upload.wikimedia.org/wikipedia/en/7/79/Broken_Flowers_poster.jpg",
                        "https://www.youtube.com/watch?v=c_TB7MkrGyc")
only_lovers = media.Movie("Only Lovers Left Alive",
                     "Two vampires roam Detroit and Tangiers. Shakespear dies.",
                     "http://t1.gstatic.com/images?q=tbn:ANd9GcRhk_O8kKXRE-RfYzxTHK6StpP3ez4wZr-oCyWpzNhhQrV8-HBf",
                     "https://www.youtube.com/watch?v=ycOKvWrwYFo")
#create list of movies
movies = [coffee, down, ghost_dog, dead_man, broken_flowers, only_lovers]
#open movies page using fresh tomatoes 
fresh_tomatoes.open_movies_page(movies)
