class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Exception: division by zero:
        try:
            diff = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
            for i, coord in enumerate(coordinates[1:], 1):
                if (coord[1]-coordinates[i-1][1])/(coord[0]-coordinates[i-1][0])!=diff:
                    return False
            return True
        except:
            x_axis = coordinates[0][0]
            for coord in coordinates[1:]:
                if x_axis!=coord[0]:
                    return False
            return True