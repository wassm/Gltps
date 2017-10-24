import math as math
class VectorHelper:
	"""A class that handle vectors

	handle a vector presented in a list
	contain functions that:
	sort a vector.
	add two vectors.
	return its minimum and maximum.
	reverse a vector.
	apply a function on the elements of a vector.

	"""

    @staticmethod
    def sort(vector):
    	""" sort a vector. 

    	parameters:
    	vector: a list which contains the componenets of a vector.

    	apply changes in the parameter itself.

    	"""
            ind1 = ind2 = 0
            while (ind1 <= len(vector) - 2):
                ind2 = ind1 + 1
                while (ind2 <= len(vector) - 1):
                    if vector[ind1] > vector[ind2]:
                        vector[ind1],vector[ind2]=vector[ind2],vector[ind1]
                    ind2 += 1
                ind1 += 1


    @staticmethod
    def add(vector1, vector2):
    	"""add two vectors and returns the result.

    	rise an exception when the two parameters have not the sime length.

    	parameters:
    	vector1: the list of components of the first vector.
    	vector2: the list of components of the second vector.

    	return:
    	vector3 : a list of the components of the sum of the 2 vectors.

    	"""
        if len(vector1) != len(vector2):
            raise Exception("Impossible to add two vectors with different sizes !!")
        else:
            vector3 = list()
            i = 0
            while i<=len(vector1)-1:
                vector3.append(vector1[i]+vector2[i])
                i=i+1
            return vector3

    @staticmethod
    def maxandmin(vector):
<<<<<<< HEAD
        if len(vector)!=0:
        	minimum=maximum= vector[1]
        	for element in vector:
	            if element > maximum:
	                maximum = element
	            if element < minimum:
	                minimum = element
        	return maximum, minimum
        else :
        	raise Exception("Empty vector")
=======
    	"""return the maximum and the minimum in the vector.

    	parameters:
    	vector: the list of components of the vector.

    	return:
    	max: the maximum of the components of the vector.
    	min: the minimum of the components of the vector.

    	"""
        minimum = maximum = vector[1]
        for element in vector:
            if element > maximum:
                maximum = element
            if element < minimum:
                minimum = element
        return maximum, minimum

>>>>>>> d9b04a0c204d672ed15a40dca285e352b24cb191

    @staticmethod
    def inverse(vector):
    	"""reverse the vector.

    	reverse the components of the vector so they look like,
    	the first will be the last, the last will be the first ...

    	parameters:
    	vector: the list of components of the vector.

    	apply changes in the parameter itself.

    	"""
    	size=len(vector)
    	milieu=(size+1)/2
    	i=0
    	while i<=milieu :
    		vector[i],vector[size-i-1]=vector[size-i-1],vector[i]
    		i+=1

    @staticmethod
    def formule(vector):
    	""" apply a formula on the elements in the vector. 

        parameters:
    	vector: the list of components of the vector.

    	apply changes in the parameter itself.

    	"""
    	#sigmoid
    	size=len(vector)
    	ind=0
    	while ind<size:
    		vector[ind]=1/(1+math.exp(-vector[i]))
    		ind+=1















