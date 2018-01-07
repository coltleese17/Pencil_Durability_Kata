#!/usr/bin/env python3

import unittest
import pencil as pen
import paper as pap

class PencilDurabilityTests(unittest.TestCase): 

	def setUp(self):
		self.pencil = pen.Pencil()

	def testwhenYouWriteWithAPencilItReturnsThatWordOnThePaper(self):
		paper = pap.Paper("")
		self.assertEqual("TestingPencil", self.pencil.write("TestingPencil", paper))

	def testwhenYouInitializeAPaperWithWordsItHasContainsThoseWords(self):
		paper = pap.Paper("She")
		self.assertEqual("She", paper.display())

	def testwhenYouWriteOnAPaperItAppenDsThoseWordsToTheAlreadyWrittenWords(self):
		paper = pap.Paper("She")
		self.pencil.write(" has", paper)
		self.assertEqual("She has", paper.display())	


if __name__ == '__main__':
	unittest.main()