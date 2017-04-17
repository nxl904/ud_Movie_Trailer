import webbrowser
"""Import webbrowser module from standard python library"""

class Video(): 
"""Define and initate the controller for class Video. Title, and duration defined in this class."""
	def __init__ (self, title, duration): 
		self.title = title
		self.duration = duration



class Movie(Video): 
"""Child class of Video. The only purpose that two classes exist in this code is to demonstarte inheritance. In this case the Movie class is 
inheriting title and duration from Video. The show_trailer method calls "open" from the webbrowser module prompting the youtube url to opne""" 
	
	def __init__ (self, title, duration, movie_storyline, poster_image, trailer_youtube): 
		Video.__init__(self, title, duration)
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer (self):
		webbrowser.open(self.trailer_youtube_url)

