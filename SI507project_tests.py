import sqlite3
import unittest


class FinalProjectTests(unittest.TestCase):

	def setUp(self):
		self.conn = sqlite3.connect("books.db_project_final") # Connecting to database that should exist in autograder
		self.cur = self.conn.cursor()

	def test_for_books_table(self):
		self.cur.execute("select id, title, author_id, rating, image_link, year_published from books where title = 'The Hunger Games'")
		data = self.cur.fetchone()
		self.assertEqual(data,(1, 'The Hunger Games', 1, 4.34, "https://images.gr-assets.com/books/1447303603m/2767052.jpg", 2008), "Testing data that results from selecting The Hunger Games")


	def test_for_authors_table(self):
		res = self.cur.execute("select * from authors")
		data = res.fetchall()
		self.assertTrue(data, 'Testing that you get a result from making a query to the authors table')




	# def test_foreign_key_chocolate(self):
	# 	res = self.cur.execute("select * from chocolatebars INNER JOIN countries ON chocolatebars.companyCountry = countries.id")
	# 	data = res.fetchall()
	# 	self.assertTrue(data, "Testing that result of selecting based on relationship between chocolatebars and countries does work")
	# 	self.assertTrue(len(data) in [1795, 1796], "Testing that there is in fact the amount of data entered that there should have been -- based on this query of everything in both tables.{}".format(len(data)))
    #

	def tearDown(self):
		self.conn.commit()
		self.conn.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
