#!/usr/bin/env python3

import unittest
import pencil as pen
import paper as pap

class PencilDurabilityTests(unittest.TestCase): 

	def testwhenYouWriteWithAPencilItReturnsThatWord(self):
		pencil = pen.Pencil()
		paper = pap.Paper("")
		self.assertEqual("TestingPencil", pencil.write("TestingPencil", paper))

	def testwhenYouInitializeAPaperWithWordsItHasContainsThoseWords(self):
		paper = pap.Paper("She")
		self.assertEqual("She", paper.display())


if __name__ == '__main__':
	unittest.main()