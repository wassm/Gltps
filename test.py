import unittest
import VectorHelper as vectorHelper
class VectorHelperTest(unittest.TestCase):

	#teste de la methode sort()
	def test_sort(self):
		vector=[1,0,4,3,99,45,7,8,2]
		vectorHelper.VectorHelper.sort(vector)
		self.assertEqual(vector,[0,1,2,3,4,7,8,45,99])

	#teste de la methode add()
	def test_add(self):
		vector1=[1,0,4,3,99,45,7,8,2]
		vector2=[4,5,7,8,2,9,6,3,41]
		vectorResult=vectorHelper.VectorHelper.add(vector1,vector2)
		self.assertEqual(vectorResult,[5,5,11,11,101,54,13,11,43])

	#teste de le lancemant d'une exception a l'addition de deux vecteurs de tailles differentes 
	def test_add_exception(self):
		with self.assertRaises(Exception):
			vectorHelper.VectorHelper.add([1,2],[1,2,4])

	#teste de la methode maxandmin()
	def test_maxAndMin(self):
		maximum,minimum=vectorHelper.VectorHelper.maxandmin([44,1,0,55,7,-1])
		self.assertEqual(maximum,55)
		self.assertEqual(minimum,-1)

	#teste le lancemant d'une exception pour les vecturs vides
	def test_maxAndMin(self):
		with self.assertRaises(Exception):
			vectorHelper.VectorHelper.maxandmin([])

	#teste la methode inverse()
	def test_inverse(self):
		vector1=[1,0,2,4,5,8,9,7,6]
		vector2=[6,7,9,8,5,4,2,0,1]
		vectorHelper.VectorHelper.inverse(vector1)
		self.assertEqual(vector1,vector2)

	#teste la methode formule()
	def test_formule(self):
		vector1=[0.,1.,2.,3.]
		vector2=[0.5,
		0.7310585786300049,
		0.8807970779778823,
		0.9525741268224334]
		vectorHelper.VectorHelper.formule(vector1)
		self.assertEqual(vector1,vector2)


unittest.main()
