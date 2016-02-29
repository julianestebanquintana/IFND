import webbrowser
		
class Movie():
	"""Instantiates an object that holds the information of every movie. """
	def __init__(self, movie_title, spanish_title, poster_image, trailer_youtube, movie_storyline,   release_date,
		director_name, protagonist1_name, protagonist2_name, stars):
		self.movie_title = movie_title
		self.spanish_title = spanish_title
		self.poster_image = poster_image
		self.trailer_youtube = trailer_youtube
		self.movie_storyline = movie_storyline
		self.release_date = release_date
		self.director_name = director_name
		self.protagonist1_name = protagonist1_name
		self.protagonist2_name = protagonist2_name
		self.stars = stars

	def show_trailer(self): 
		"""Method to open the trailer given as part of the movie object. """
		webbrowser.open(self.trailer_youtube)
