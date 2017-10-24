import math as math
class VectorHelper:

    @staticmethod
    def sort(vector):
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

    @staticmethod
    def inverse(vector):
    	size=len(vector)
    	milieu=(size+1)/2
    	i=0
    	while i<=milieu :
    		vector[i],vector[size-i-1]=vector[size-i-1],vector[i]
    		i+=1

    @staticmethod
    def formule(vector):
    	#sigmoid
    	size=len(vector)
    	ind=0
    	while ind<size:
    		vector[ind]=1/(1+math.exp(-vector[i]))
    		ind+=1















