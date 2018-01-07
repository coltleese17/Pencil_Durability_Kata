#!/usr/bin/env python3


class Pencil:

	def __init__(self, point_durability):
		self.point_durability = point_durability
		self.initial_durability = point_durability



	def write(self, input, paper):
		input_after_degradation = self.point_degradation(input)
		words_on_page = paper.write(input_after_degradation);
		return words_on_page

	def point_degradation(self,input):
		for i, c in enumerate(input):
			if (self.point_durability <= 0):
				return input[0:i]
			if c.isupper():
				self.point_durability -= 2
			if c.islower():
				self.point_durability -= 1
		return input				


	def displayPointTotal(self):
		return self.point_durability

	def sharpen(self):
		self.point_durability = self.initial_durability				
						

