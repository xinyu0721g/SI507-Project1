import unittest
import proj1_w18 as proj1
import json

infile = open('sample_json.json','r')
infile_text = infile.read()
infile.close()
dict_lst = json.loads(infile_text)
json_movie = dict_lst[0]
json_song = dict_lst[1]
json_media = dict_lst[2]

class TestMedia(unittest.TestCase):

	def testConstructor(self):
		m1 = proj1.Media()
		m2 = proj1.Media(json_media)

		self.assertEqual(m1.title, "No Title")
		self.assertEqual(m1.author, "No Author")
		self.assertEqual(m1.release_year, None)

		self.assertEqual(m2.title, "Bridget Jones's Diary (Unabridged)")
		self.assertEqual(m2.author, "Helen Fielding")
		self.assertEqual(m2.release_year, 2012)

	def testString(self):
		m1 = proj1.Media()
		m2 = proj1.Media(json_media)

		self.assertEqual(m1.__str__(),"No Title by No Author (None)")
		self.assertEqual(m2.__str__(),"Bridget Jones's Diary (Unabridged) by Helen Fielding (2012)")

	def testLength(self):
		m1 = proj1.Media()
		m2 = proj1.Media(json_media)

		self.assertEqual(len(m1),0)
		self.assertEqual(len(m2),0)		

	def testNotRelevant(self):
		m1 = proj1.Media()
		m2 = proj1.Media(json_media)

		with self.assertRaises(AttributeError):
			value1 = m1.rating

		with self.assertRaises(AttributeError):
			value2 = m2.album

		with self.assertRaises(AttributeError):
			value3 = m1.genre

		with self.assertRaises(AttributeError):
			value4 = m2.track_length

class TestSong(unittest.TestCase):

	def testConstructor(self):
		s1 = proj1.Song()
		s2 = proj1.Song(json_song)

		self.assertEqual(s1.title, "No Title")
		self.assertEqual(s1.author, "No Author")
		self.assertEqual(s1.release_year, None)
		self.assertEqual(s1.album, "No Album")
		self.assertEqual(s1.genre, "No Genre")
		self.assertEqual(s1.track_length,0)

		self.assertEqual(s2.title, "Hey Jude")
		self.assertEqual(s2.author, "The Beatles")
		self.assertEqual(s2.release_year, 1968)
		self.assertEqual(s2.album, "TheBeatles 1967-1970 (The Blue Album)")
		self.assertEqual(s2.genre, "Rock")
		self.assertEqual(s2.track_length,431333)

	def testString(self):
		s1 = proj1.Song()
		s2 = proj1.Song(json_song)

		self.assertEqual(s1.__str__(),"No Title by No Author (None) [No Genre]")
		self.assertEqual(s2.__str__(),"Hey Jude by The Beatles (1968) [Rock]")

	def testLength(self):
		s1 = proj1.Song()
		s2 = proj1.Song(json_song)

		self.assertEqual(len(s1),0)
		self.assertEqual(len(s2),431)

	def testNotRelevant(self):
		s1 = proj1.Song()
		s2 = proj1.Song(json_song)

		with self.assertRaises(AttributeError):
			value1 = s1.rating

		with self.assertRaises(AttributeError):
			value2 = s2.movie_length

class TestMovie(unittest.TestCase):

	def testConstructor(self):
		mv1 = proj1.Movie()
		mv2 = proj1.Movie(json_movie)

		self.assertEqual(mv1.title, "No Title")
		self.assertEqual(mv1.author, "No Author")
		self.assertEqual(mv1.release_year, None)
		self.assertEqual(mv1.rating, "No Rating")
		self.assertEqual(mv1.movie_length, 0)

		self.assertEqual(mv2.title, "Jaws")
		self.assertEqual(mv2.author, "Steven Spielberg")
		self.assertEqual(mv2.release_year, 1975)
		self.assertEqual(mv2.rating, "PG")
		self.assertEqual(mv2.movie_length,7451455)

	def testString(self):
		mv1 = proj1.Movie()
		mv2 = proj1.Movie(json_movie)

		self.assertEqual(mv1.__str__(),"No Title by No Author (None) [No Rating]")		
		self.assertEqual(mv2.__str__(),"Jaws by Steven Spielberg (1975) [PG]")

	def testLength(self):
		mv1 = proj1.Movie()
		mv2 = proj1.Movie(json_movie)

		self.assertEqual(len(mv1),0)		
		self.assertEqual(len(mv2),124)		

	def testNotRelevant(self):
		mv1 = proj1.Movie()
		mv2 = proj1.Movie(json_movie)

		with self.assertRaises(AttributeError):
			value1 = mv1.album

		with self.assertRaises(AttributeError):
			value2 = mv2.genre

		with self.assertRaises(AttributeError):
			value3 = mv1.track_length

class TestFunctions(unittest.TestCase):

	def test_get_medias_from_itunes(self):
		medias1 = proj1.get_medias_from_itunes()
		medias2 = proj1.get_medias_from_itunes('baby',20)
		medias3 = proj1.get_medias_from_itunes('love')
		medias4 = proj1.get_medias_from_itunes('moana',25)
		medias5 = proj1.get_medias_from_itunes('helter skelter',15)
		medias6 = proj1.get_medias_from_itunes('&@#!$')

		self.assertTrue(0<=len(medias1)<=10)
		self.assertTrue(0<=len(medias2)<=20)
		self.assertTrue(0<=len(medias3)<=10)
		self.assertTrue(0<=len(medias4)<=25)
		self.assertTrue(0<=len(medias5)<=15)
		self.assertTrue(0<=len(medias6)<=10)

	def test_get_songs_from_itunes(self):
		songs1 = proj1.get_songs_from_itunes()
		songs2 = proj1.get_songs_from_itunes('baby',20)
		songs3 = proj1.get_songs_from_itunes('love')
		songs4 = proj1.get_songs_from_itunes('moana',25)
		songs5 = proj1.get_songs_from_itunes('helter skelter',15)
		songs6 = proj1.get_songs_from_itunes('&@#!$')

		self.assertTrue(0<=len(songs1)<=10)
		self.assertTrue(0<=len(songs2)<=20)
		self.assertTrue(0<=len(songs3)<=10)
		self.assertTrue(0<=len(songs4)<=25)
		self.assertTrue(0<=len(songs5)<=15)
		self.assertTrue(0<=len(songs6)<=10)	

	def test_get_movies_from_itunes(self):
		movie1 = proj1.get_movies_from_itunes()
		movie2 = proj1.get_movies_from_itunes('baby',20)
		movie3 = proj1.get_movies_from_itunes('love')
		movie4 = proj1.get_movies_from_itunes('moana',25)
		movie5 = proj1.get_movies_from_itunes('helter skelter',15)
		movie6 = proj1.get_movies_from_itunes('&@#!$')

		self.assertTrue(0<=len(movie1)<=10)
		self.assertTrue(0<=len(movie2)<=20)
		self.assertTrue(0<=len(movie3)<=10)
		self.assertTrue(0<=len(movie4)<=25)
		self.assertTrue(0<=len(movie5)<=15)
		self.assertTrue(0<=len(movie6)<=10)

	def test_get_from_itunes(self):
		all1 = proj1.get_from_itunes()
		all2 = proj1.get_from_itunes('baby',20)
		all3 = proj1.get_from_itunes('love')
		all4 = proj1.get_from_itunes('moana',25)
		all5 = proj1.get_from_itunes('helter skelter',15)
		all6 = proj1.get_from_itunes('&@#!$')

		self.assertTrue(0<=len(all1)<=10)
		self.assertTrue(0<=len(all2)<=20)
		self.assertTrue(0<=len(all3)<=10)
		self.assertTrue(0<=len(all4)<=25)
		self.assertTrue(0<=len(all5)<=15)
		self.assertTrue(0<=len(all6)<=10)
		

unittest.main()
