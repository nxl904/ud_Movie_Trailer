import media
#Imports the media.py class module into entertainment_center.py
import fresh_tomatoes
#Imports the fresh_tomatoes.py module into entertainment_center.py to apply html/css elements to generate a webpage. 

#Each movie to be rendred on the webpage with their assocaited attribute values. Each one calls the Movie class from the media.py module to assign attributes.
gangs_of_new_york = media.Movie("Gangs of New York", "130", "Amsterdam Vallon (Leonardo DiCaprio) is a young Irish immigrant released from prison. He returns to the Five Points seeking revenge against his father's killer...", "https://upload.wikimedia.org/wikipedia/en/a/ae/Gangs_of_New_York_Poster.jpg", "https://www.youtube.com/watch?v=1_CDJiYux1A")

toy_story = media.Movie("Toy Story", "90", "A story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc" )

shawshank_redemption = media.Movie("Shawshank Redemption", "210", "Redemption happens at Shawshank Prision", "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg","https://www.youtube.com/watch?v=6hB3S9bIaco")

Revolver = media.Movie("Revolver", "120","Jake is a hotshot gambler who always wins. When he wins a game against with Macha, a crime boss and casino owner, he puts out an order for a hit on Jake.", "https://upload.wikimedia.org/wikipedia/en/b/b6/Revolver2005.jpg", "https://www.youtube.com/watch?v=svGAucw3Y80")

last_king_of_scotland = media.Movie("Last King of Scotland", "95", "Nicholas Garrigan leaves his dominant father in hopes of a better future, only to find himself trapped by an even more powerful authority.", "https://upload.wikimedia.org/wikipedia/en/d/d9/Last_king_of_scotland_uk.jpg","https://www.youtube.com/watch?v=b8ZlPO5BlBI")

Avatar = media.Movie("Avatar","120","On the lush alien world of Pandora live the Na'vi, beings who appear primitive but are highly evolved. Because the planet's environment is poisonous, human/Na'vi hybrids, called Avatars, must link to human minds to allow for free movement on Pandora.", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")


movies = [gangs_of_new_york, shawshank_redemption, toy_story, Revolver, last_king_of_scotland, Avatar]


fresh_tomatoes.open_movies_page(movies)
#Calls the open_movies_page method from fresh_tomatoes on the movies list in entertainment_center

