#!/usr/bin/env python3

import unittest
import pencil as pen
import paper as pap

class PencilDurabilityTests(unittest.TestCase): 

	# def setUp(self):
	# 	self.pencil = pen.Pencil()

	def testwhenYouWriteWithAPencilItReturnsThatWordOnThePaper(self):
		pencil = pen.Pencil(1000)
		paper = pap.Paper("")
		self.assertEqual("TestingPencil", pencil.write("TestingPencil", paper))

	def testwhenYouInitializeAPaperWithWordsItHasContainsThoseWords(self):
		paper = pap.Paper("She")
		self.assertEqual("She", paper.display())

	def testwhenYouWriteOnAPaperItAppenDsThoseWordsToTheAlreadyWrittenWords(self):
		paper = pap.Paper("She")
		pencil = pen.Pencil(10)
		pencil.write(" has", paper)
		self.assertEqual("She has", paper.display())

	def testWhenYouWriteAnUppercaseLetterPointDurabilityDecreasesByTwo(self):
		pencil = pen.Pencil(3)
		pencil.point_degradation("L")
		self.assertEqual(1, pencil.displayPointTotal())

	def testWhenYouWriteTwoUppercaseLettersPointDurabilityDecreasesByFour(self):
		pencil = pen.Pencil(5)
		pencil.point_degradation("LL")
		self.assertEqual(1, pencil.displayPointTotal())			

	def testWhenYouWriteALowercaseLetterPointDurabilityDecreasesByOne(self):
		pencil = pen.Pencil(3)
		pencil.point_degradation("a")
		self.assertEqual(2, pencil.displayPointTotal())

	def testWhenYouWriteALowercaseLetterPointDurabilityDecreasesByTwo(self):
		pencil = pen.Pencil(3)
		pencil.point_degradation("aa")
		self.assertEqual(1, pencil.displayPointTotal())

	def testWhenPointDurabilityIsLessThanOrEqualToZeroItReturnsTheRemainerOfTheWordAsWhiteSpace(self):
		pencil = pen.Pencil(4)
		# returned_word_after_degradation = pencil.point_degradation("Text")
		self.assertEqual("Tex", pencil.point_degradation("Text"))

	def testPointDurabilityBehaviorWhenWriting(self):
		pencil = pen.Pencil(4)
		paper = pap.Paper("")
		self.assertEqual("Tex", pencil.write("Text", paper))

	def testIfNoDurabilityReturnWhitespace(self):
		pencil = pen.Pencil(0)
		paper = pap.Paper("")
		self.assertEqual("", pencil.write("Text", paper))

	def testWhenSharpeningPencilItReturnsToItsOriginalDurability(self):
		pencil = pen.Pencil(1000)
		pencil.point_degradation("LMWEFASDFfer")
		pencil.sharpen()
		self.assertEqual(1000, pencil.displayPointTotal())





if __name__ == '__main__':
	unittest.main()