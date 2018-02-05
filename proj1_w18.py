import requests
import json
import webbrowser

class Media:

	def __init__(self,json=None): # dictionary
		if json == None:
			json = {}
		if 'collectionName' in json:
			self.title = json['collectionName']
		else:
			self.title = 'No Title'
		if 'artistName' in json:
			self.author = json['artistName']
		else:
			self.author = 'No Author'
		if 'releaseDate' in json:
			self.release_year = int(json['releaseDate'].strip()[:4])
		else:
			self.release_year = None
		if 'collectionViewUrl' in json:
			self.url = json['collectionViewUrl']
		else:
			self.url = None

	def __str__(self):
		return "{} by {} ({})".format(self.title,self.author,self.release_year)

	def __len__(self):
		return 0

def get_medias_from_itunes(name='',limit=10):
	medias = []
	base_url = 'https://itunes.apple.com/search'
	params = {}
	params['term'] = name
	params['limit'] = limit
	response = requests.get(base_url, params)
	response_diction = json.loads(response.text)
	for i in response_diction['results']:
		medias.append(Media(i))
	return medias

class Song(Media):

	def __init__(self,json=None): 
		if json == None:
			json = {}
		super().__init__(json)
		if 'trackName' in json:
			self.title = json['trackName']
		else:
			self.title = 'No Title'
		if 'collectionName' in json:
			self.album = json['collectionName']
		else:
			self.album = 'No Album'
		if 'primaryGenreName' in json:
			self.genre = json['primaryGenreName']
		else:
			self.genre = 'No Genre'
		if 'trackTimeMillis' in json:
			self.track_length = json['trackTimeMillis']
		else:
			self.track_length = 0
		if 'trackViewUrl' in json:
			self.url = json['trackViewUrl']
		else:
			self.url = None

	def __str__(self):
		return super().__str__() + " [{}]".format(self.genre)

	def __len__(self):
		return round(self.track_length / 1000) # track length in seconds

def get_songs_from_itunes(name='',limit=10):
	songs = []
	base_url = 'https://itunes.apple.com/search'
	params = {}
	params['term'] = name
	params['entity'] = 'song'
	params['limit'] = limit
	response = requests.get(base_url, params)
	response_diction = json.loads(response.text)
	for i in response_diction['results']:
		songs.append(Song(i))
	return songs

class Movie(Media):
	
	def __init__(self,json=None):
		if json == None:
			json = {}
		super().__init__(json)
		if 'trackName' in json:
			self.title = json['trackName']
		else:
			self.title = 'No Title'
		if 'contentAdvisoryRating' in json:
			self.rating = json['contentAdvisoryRating']
		else:
			self.rating = 'No Rating'
		if 'trackTimeMillis' in json:
			self.movie_length = json['trackTimeMillis']
		else:
			self.movie_length = 0
		if 'trackViewUrl' in json:
			self.url = json['trackViewUrl']
		else:
			self.url = None

	def __str__(self):
		return super().__str__() + " [{}]".format(self.rating)

	def __len__(self):
		return round(self.movie_length / 1000 / 60) # movie length in minutes, rounded to nearest minute

def get_movies_from_itunes(name='',limit=10):
	movies = []
	base_url = 'https://itunes.apple.com/search'
	params = {}
	params['term'] = name
	params['entity'] = 'movie'
	params['limit'] = limit
	response = requests.get(base_url, params)
	response_diction = json.loads(response.text)
	for i in response_diction['results']:
		movies.append(Movie(i))
	return movies

# get_from_itunes get a list of objects of all media types 
def get_from_itunes(name='',limit=10):
	all_types = []
	base_url = 'https://itunes.apple.com/search'
	params = {}
	params['term'] = name
	params['limit'] = limit
	response = requests.get(base_url, params)
	response_diction = json.loads(response.text)
	for i in response_diction['results']:
		if 'movie' in i['kind']:
			all_types.append(Movie(i))
		elif 'song' in i['kind']:
			all_types.append(Song(i))
		else:
			all_types.append(Media(i))
	return all_types

def grouped_medias(name='',limit=50):
	all_medias = get_from_itunes(name,limit)
	songs = []
	movies = []
	others = []
	for media in all_medias:
		if isinstance(media,Song):
			songs.append(media)
		elif isinstance(media,Movie):
			movies.append(media)
		else:
			others.append(media)
	return songs,movies,others

def medias_diction(name='',limit=50):
	(songs,movies,others) = grouped_medias(name,limit)
	diction = {}
	sl = len(songs)
	sm = len(movies)
	so = len(others)
	for i in range(sl):
		diction[i+1] = songs[i]
	for i in range(sm):
		diction[i+1+sl] = movies[i]
	for i in range(so):
		diction[i+1+sl+sm] = others[i]
	return diction

def print_medias(name='',limit=50):
	(songs,movies,others) = grouped_medias(name,limit)
	feedback = '\n\nSONGS'
	if len(songs) == 0:
		feedback += "\nThere's no song in this search."
	else:
		for i in range(len(songs)):
			feedback += "\n{} {}".format(i+1,songs[i].__str__())
	feedback += '\n\nMOVIES'
	if len(movies) == 0:
		feedback += "\nThere's no movie in this search."
	else:
		for i in range(len(movies)):
			feedback += "\n{} {}".format(i+1+len(songs),movies[i].__str__())
	feedback += '\n\nOTHER MEDIA'
	if len(others) == 0:
		feedback += "\nThere's no other media in this search."
	else:
		for i in range(len(others)):
			feedback += "\n{} {}".format(i+1+len(songs)+len(movies),others[i].__str__())
	print(feedback)

def get_more_info(diction,num):
	m = diction[num]
	print("\n\nLaunching {} in web browser...".format(m.url))
	webbrowser.open(m.url)

if __name__ == "__main__":
	# your control code for Part 4 (interactive search) should go here
	name = input('''\nEnter a search term, or "exit" to quit:''')
	if name != "exit":
		print_medias(name)
		diction = medias_diction(name)
		while True:
			more = input("\n\nEnter a number for more info, or another search term, or exit:")
			try:
				num = int(more)
				get_more_info(diction,num)
			except:
				if more == 'exit':
					break
				else:
					print_medias(more)
					diction = medias_diction(more)


