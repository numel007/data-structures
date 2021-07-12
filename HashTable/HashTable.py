#!python

from LinkedList import LinkedList


class HashTable(object):

	def __init__(self, num_buckets=8):
		"""Initialize this hash table with the given initial size."""
		self.buckets = [LinkedList() for i in range(num_buckets)]

	def __str__(self):
		"""Return a formatted string representation of this hash table."""
		items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
		return '{' + ', '.join(items) + '}'

	def __repr__(self):
		"""Return a string representation of this hash table."""
		return 'HashTable({!r})'.format(self.items())

	def _bucket_index(self, key):
		"""Return the bucket index where the given key would be stored."""
		return hash(key) % len(self.buckets)

	def load_factor(self):
		"""Return the load factor, the ratio of number of entries to buckets.a"""
		print(f'{len(self.items())} items in {len(self.buckets)} buckets')
		return len(self.items()) / len(self.buckets)

	def items(self):
		"""Return a list of all entries (key-value pairs) in this hash table."""
		all_items = []
		for bucket in self.buckets:
			all_items.extend(bucket.items())
		return all_items

	def get(self, key):
		"""Return the value associated with the given key, or raise KeyError.
		Best case running time: O(1) if key exists as first item in a bucket
		Worst case running time: O(N) if key exists as last item in longest bucket or simply does not exist
		"""

		hash = self._bucket_index(key)

		value = self.buckets[hash].find(key)
		
		if not value:
			return 'This key does not exist'
		else:
			return value.data

	def set(self, key, value):
		"""Insert the given key with its associated value.
		Best case running time: O(1), locates duplicate key existing as first item in a bucket, and updates key/value
		Worst case running time: O(N), key was not found after searching through all buckets, finally adds key/value to a bucket
		"""
		hash = self._bucket_index(key)

		target = self.buckets[hash].find(key)

		if not target:
			self.buckets[hash].append((key, value))
		else:
			target.data = (key, value)

		load_factor = self.load_factor()

		if load_factor > 0.75:
			print('Load factor exceeds 0.75, generating new table')
			self._resize()

	def delete(self, key):
	  # THIS IS STRETCH WILL NEED TO IMPLEMENT DELETE IN LL
		"""Delete the given key and its associated value, or raise KeyError.
		Best case running time: O(1) if the key is the first node in a bucket's LL
		Worst case running time: O(N) if the key to be deleted doesn't exist or is last in a bucket's LL
		"""

		hash = self._bucket_index(key)

		target = self.buckets[hash].find(key)

		if not target:
			print("Can not delete non-existing key")
		else:
			self.buckets[hash].delete_one(key)

	def _resize(self, new_size=None):
		"""Resize this hash table's buckets and rehash all key-value entries.
		Should be called automatically when load factor exceeds a threshold
		such as 0.75 after an insertion (when set is called with a new key)."""
		items = self.items()

		bucket_size = len(self.buckets)
		while len(items)/bucket_size >= 0.75:
			bucket_size += 1

		self.buckets = [LinkedList() for i in range(bucket_size)]

		for item in items:
			hash = self._bucket_index(item[0])
			self.buckets[hash].append(item)
		self.load_factor()


def test_hash_table():
	ht = HashTable(4)
	print('HashTable: ' + str(ht))

	print('Setting entries:')
	ht.set('I', 1)
	print('set(I, 1): ' + str(ht))
	ht.set('V', 5)
	print('set(V, 5): ' + str(ht))

	print('buckets: ' + str(len(ht.buckets)))
	print('load_factor: ' + str(ht.load_factor()))
	ht.set('X', 10)
	print('set(X, 10): ' + str(ht))
	ht.set('L', 50)  # Should trigger resize
	print('set(L, 50): ' + str(ht))

	print('buckets: ' + str(len(ht.buckets)))
	print('load_factor: ' + str(ht.load_factor()))

	print('Getting entries:')
	print('get(I): ' + str(ht.get('I')))
	print('get(V): ' + str(ht.get('V')))
	print('get(X): ' + str(ht.get('X')))
	print('get(L): ' + str(ht.get('L')))

	print('Deleting entries:')
	ht.delete('I')
	print('delete(I): ' + str(ht))
	ht.delete('V')
	print('delete(V): ' + str(ht))
	ht.delete('X')
	print('delete(X): ' + str(ht))
	ht.delete('L')
	print('delete(L): ' + str(ht))

	print('buckets: ' + str(len(ht.buckets)))
	print('load_factor: ' + str(ht.load_factor()))


test_hash_table()