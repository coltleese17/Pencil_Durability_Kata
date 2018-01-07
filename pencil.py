#!/usr/bin/env python3


class Pencil:

	def __init__(self, point_durability):
		self.point_durability = point_durability



	def write(self, input, paper):
		words_written = paper.write(input);
		return words_written

	def point_degradation(self,input):
		for c in input:
			if (self.point_durability <= 0):
				return input
			if c.isupper():
				self.point_durability -= 2
			if c.islower():
				self.point_durability -= 1	


	def displayPointTotal(self):
		return self.point_durability			
						

