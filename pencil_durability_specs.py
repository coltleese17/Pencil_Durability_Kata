#!/usr/bin/env python3

import unittest
import pencil as pen
import paper as pap

class PencilDurabilityTests(unittest.TestCase): 

	# def setUp(self):
	# 	self.pencil = pen.Pencil()

	def testwhenYouWriteWithAPencilItReturnsThatWordOnThePaper(self):
		pencil = pen.Pencil(5)
		paper = pap.Paper("")
		self.assertEqual("TestingPencil", pencil.write("TestingPencil", paper))

	def testwhenYouInitializeAPaperWithWordsItHasContainsThoseWords(self):
		paper = pap.Paper("She")
		self.assertEqual("She", paper.display())

	def testwhenYouWriteOnAPaperItAppenDsThoseWordsToTheAlreadyWrittenWords(self):
		paper = pap.Paper("She")
		pencil = pen.Pencil(5)
		pencil.write(" has", paper)
		self.assertEqual("She has", paper.display())

	def testWhenYouWriteAnUppercaseLetterPointDegradationDecreasesByTwo(self):
		pencil = pen.Pencil(3)
		pencil.point_degradation("L")
		self.assertEqual(1, pencil.displayPointTotal())

	def testWhenYouWriteTwoUppercaseLettersPointDegradationDecreasesByFour(self):
		pencil = pen.Pencil(5)
		pencil.point_degradation("LL")
		self.assertEqual(1, pencil.displayPointTotal())			



if __name__ == '__main__':
	unittest.main()