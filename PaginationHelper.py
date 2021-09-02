# For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array.
# The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. The types of values contained within the collection/array are not relevant.

import math

class PaginationHelper:
	# The constructor takes in an array of items and a integer indicating
	# how many items fit within a single page
	def __init__(self, collection, items_per_page):
		self.items_per_page = items_per_page
		self.size = len(collection)
		self.n_pages = int(math.ceil(len(collection) / items_per_page))

  	# returns the number of items within the entire collection
	def item_count(self):
		return self.size

  	# returns the number of pages
	def page_count(self):
		return self.n_pages

  	# returns the number of items on the current page. page_index is zero based
  	# this method should return -1 for page_index values that are out of range
	def page_item_count(self, page_index):
		if 0 < page_index < self.n_pages:
			return self.items_per_page if page_index != self.n_pages - 1 else self.size % self.items_per_page or self.items_per_page
		else:
			return -1

# determines what page an item is on. Zero based indexes.
# this method should return -1 for item_index values that are out of range
	def page_index(self, item_index):
		return  item_index // self.items_per_page if 0 < item_index < self.size else -1 

collection = range(1,25)
helper = PaginationHelper(collection, 10)

print(helper.page_count(), 3, 'page_count is returning incorrect value.')
print(helper.page_index(23), 2, 'page_index returned incorrect value')
print(helper.item_count(), 24, 'item_count returned incorrect value')

helper = PaginationHelper(range(1, 25), 10)
print(helper.page_item_count(2), 4, 'page_item_count is returning incorrect value')
