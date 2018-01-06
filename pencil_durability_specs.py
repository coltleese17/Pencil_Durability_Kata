#!/usr/bin/env python3

import unittest
import pencil

class PencilDurabilityTests(unittest.TestCase): 

	def whenYouWriteWithAPencilItReturnsThatWord(self):
		pencil = pencil.pencil()
		assertEqual("TestingPencil", pencil.write("TestingPencil"))

if __name__ == '__main__':
	unittest.main()