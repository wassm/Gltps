class VectorHelper:

    @staticmethod
    def sort(vector):
            ind1 = ind2 = 0
            while (ind1 <= len(vector) - 2):
                ind2 = ind1 + 1
                while (ind2 <= len(vector) - 1):
                    if vector[ind1] > vector[ind2]:
                        tmp = vector[ind1]
                        vector[ind1] = vector[ind2]
                        vector[ind2] = tmp
                    ind2 += 1
                ind1 += 1


    @staticmethod
    def add(vector1, vector2):
        if len(vector1) != len(vector2):
            raise Exception("Impossible to add to vectors with different sizes !!")
        else:
            vector3 = list()
            i = 0
            while i<=len(vector1)-1:
                vector3.append(vector1[i]+vector2[i])
            return vector3













