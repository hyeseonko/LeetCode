class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        chess = {'a':1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h':8}
        output = chess[coordinates[0]]+int(coordinates[1])
        if output%2==1:
            return True
        else:
            return False