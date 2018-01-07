#!/usr/bin/env python3

class Paper:

	def __init__(self, paper_text):
		self.paper_text = paper_text

	def write(self,input):	
		self.paper_text += input
		return self.paper_text

	def display(self):
		return self.paper_text	