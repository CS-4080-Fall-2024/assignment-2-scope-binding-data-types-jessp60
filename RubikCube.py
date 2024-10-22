# Assignment 2, Question 4
# Reference: https://medium.com/@ekollie324/how-to-build-a-rubiks-cube-in-python-c3bd19cbcd73

class RubiksCube:
    def __init__(self, size):
        self.size = size 
        self.endOfRow = self.size-1
        self.face = {
            # Create a dictionary of faces where each face has 9 different locations.
            "Front" : [["F" for i in range(self.size)] for j in range(self.size)],
            "Back" : [["B" for i in range(self.size)] for j in range(self.size)],
            "Left" : [["L" for i in range(self.size)] for j in range(self.size)], 
            "Right": [["R" for i in range(self.size)] for j in range(self.size)], 
            "Top" : [["T" for i in range(self.size)] for j in range(self.size)],
            # Named Down rather than Bottom because of the repeated B as part of matrix
            "Down" : [["D" for i in range(self.size)] for j in range(self.size)] 
    }


    # Use the faces as a way to turn the rows and columns of the Rubik's cube.
    def rotateFaceClockwise(self, faceName):
        face = self.face[faceName]
        # Save the value of the corner of the face
        temp = face[0][0]
        # Replace the first (top left) corner's value with the value in the bottom left square 
        face[0][0] = face[self.size-1][0]
        # Replace the bottom left corner's value with the value in the bottom right corner
        face[self.size-1][0] = face[self.size-1][self.size-1]
        # Replace the bottom right corner's value with the value in the top right corner 
        face[self.size-1][self.size-1] = face[0][self.size-1]
        # Replace the top right corner's value with the initial value of the top left corner stored in the temporary variable 
        face[0][self.size-1] = temp


        # Iterate through the entire face and swap symmetric values to adjust values that did not change 
        for i in range(self.size):
            for j in range(self.size):
                face[i][j], face[j][i] = face[j][i], face[i][j]
    


    def rotateFaceCounterClockwise(self, faceName):
        # Reverse the values in the face 
        self.face[faceName].reverse()
        # Rotate the reversed face clockwise to get the face rotated counterclockwise 
        self.rotateFaceClockwise(faceName)
            


    def rotateFrontClockwise(self):
        # Use the rotateFaceClockwise function to rotate the front face of the cube 
        self.rotateFaceClockwise("Front")
        # Save the connected top row of the front face in a temporary list 
        temp = [self.face["Top"][self.size-1][i] for i in range(self.size)]
        for i in range(self.size):
            # For each face surrounding the front face, rotate the values clockwise
            # The values in the bottom row of the top face become the values of the last column of the left face 
            self.face["Top"][self.size-1][i] = self.face["Left"][i][self.size-1]
            # The last column of the left face become the values of the first row of the down face
            self.face["Left"][i][self.size-1] = self.face["Down"][0][i]
            # The first row of the down face become the values of the first column of the right face
            self.face["Down"][0][i] = self.face["Right"][i][0]
            # The first column of the right face gets its values from the temporary list created of the original front face
            self.face["Right"][i][0] = temp[i]
    

    def rotateFrontCounterClockwise(self):
        # Use the rotateFaceCounterClockwise function to rotate the front face of the cube 
        self.rotateFaceCounterClockwise("Front")
        # Save the connected top row of the front face in a temporary list 
        temp = [self.face["Top"][i][self.size-1] for i in range(self.size)]
        for i in range(self.size):
            # For each face surrounding the front face, rotate the values counterclockwise
            # The values in the bottom row of the top face become the values of the first column of the right face
            self.face["Top"][self.size-1][i] = self.face["Right"][i][0]
            # The values in the first column of the right face becomes the values of the first row of the down face 
            self.face["Right"][i][0] = self.face["Down"][0][i]
            # The values in the first row of the down face becomes the values of the last column of the left face
            self.face["Down"][0][i] = self.face["Left"][i][self.size-1]
            # The last column of the left face gets its values from the temporary list created of the original front face 
            self.face["Left"][i][self.size-1] = temp[i]


    def rotateBackClockwise(self):
        # Use the rotateFaceClockwise function to rotate the back face of the cube 
        self.rotateFaceClockwise("Back")
        # Save the first row of the top face in a temporary list 
        temp = [self.face["Top"][0][i] for i in range(self.size)]
        for i in range(self.size):
            # The values in the first row of the top face become the values of the last column in the right face 
            self.face["Top"][0][i] = self.face["Right"][i][self.size-1]
            # The values in the last column of the right face become the values of the first row of the bottom face 
            self.face["Right"][i][self.size-1] = self.face["Down"][self.size-1][self.size-1]
            # The values in first row of the bottom face become the values of the first column of the left face
            self.face["Down"][0][i] = self.face["Left"][i][0]
            # The first column of the left face gets its values from the temporary list that contains the original values of the top face 
            self.face["Left"][i][0] = temp[i]

    def rotateBackCounterClockwise(self):
        # Use the rotateFaceCounterClockwise function to rotate the back face of the cube 
        self.rotateFaceCounterClockwise("Back")
        # Save the first row of the top face in a temporary list 
        tempRow = [self.face["Top"][0][i] for i in range(self.size)]
        for i in range(self.size):
            # The values in the first row of the top face become the values of the first column of the left face 
            self.face["Top"][0][i] = self.face["Left"][i][0]
            # The values in the first column of the left face become the values of the first row of the bottom face 
            self.face["Left"][i][0] = self.face["Down"][0][i]
            # The first row of the bottom face becomes the values of the last column of the right face 
            self.face["Down"][0][i] = self.face["Right"][i][self.size-1]
            # The last column of the right face gets its values from the temporary list that contains the original values of the top face 
            self.face["Right"][i][self.size-1] = tempRow[i]


    def rotateLeftClockwise(self):
        # Rotate the left face of the cube clockwise 
        self.rotateFaceClockwise("Left")
        # Save the first column of the top face in a temporary list
        tempColumn = [self.face["Top"][i][0] for i in range(self.size)]
        for i in range(self.size):
            # The first column of the top face become the last column of the back face 
            self.face["Top"][i][0] = self.face["Back"][i][self.size-1]
            # The last column of the back face will become the first column of the bottom face
            self.face["Back"][self.size-1-i][self.size-1] = self.face["Down"][i][0]
            # The first column of the bottom face will become the first column of the front face 
            self.face["Down"][i][0] = self.face["Front"][i][0]
            # The first column of the front face will get its values from the temporary list containing the original values of the top face 
            self.face["Front"][i][0] = tempColumn[i]

    def rotateLeftCounterClockwise(self):
        # Rotate the left face of the cube counterclockwise 
        self.rotateFaceCounterClockwise("Left")
        # Save the first column of the front face in a temporary list 
        tempColumn = [self.face["Front"][i][0] for i in range(self.size)]
        for i in range(self.size):
            # The first column of the front face becomes the first column of the bottom face 
            self.face["Front"][i][0] = self.face["Down"][i][0]
            # The first column of the bottom face becomes the last column of the back face 
            self.face["Down"][i][0] = self.face["Back"][i][self.size-1]
            # The last column of the back face becomes the first column of the top face 
            self.face["Back"][i][self.size-1] = self.face["Top"][i][0]
            # The first column of the top face will get its values from the temporary list containing the original values of the front face 
            self.face["Top"][i][0] = tempColumn[i]

    def rotateRightClockwise(self):
        # Rotate the right face of the cube clockwise 
        self.rotateFaceClockwise("Right")
        # Save the last column of the top face in a temporary list 
        tempColumn = [self.face["Top"][i][self.size-1] for i in range(self.size)]
        for i in range(self.size):
            # The last column of the top face becoems the last column of the front face
            self.face["Top"][i][self.size-1] = self.face["Front"][i][self.size-1]
            # The last column of the front face becomes the last column of the bottom face
            self.face["Front"][i][self.size-1] = self.face["Down"][i][self.size-1]
            # The last column of the bottom face becomes the first column of the back face
            self.face["Down"][i][self.size-1] = self.face["Back"][i][0]
            # The first column of the back face gets its values fromt the temporary list containing the original values of the top face 
            self.face["Back"][i][0] = tempColumn[i]

    def rotateRightCounterClockwise(self):
        # Rotate the right face counterclockwise 
        self.rotateFaceCounterClockwise("Right")
        # Save the last column of the front face in a temporary list 
        tempColumn = [self.face["Front"][i][self.size-1] for i in range(self.size)]
        for i in range(self.size):
            # The last column of the front face will become the last column of the top face 
            self.face["Front"][i][self.size-1] = self.face["Top"][i][self.size-1]
            # The last column of the top face will become first column of the back face 
            self.face["Top"][i][self.size-1] = self.face["Back"][i][0]
            # The first column of the back face will become the last column of the bottom face
            self.face["Back"][i][0] = self.face["Down"][i][self.size-1]
            # The last column of the bottoem face will get its values from the temporary list containing the original values of the front face
            self.face["Down"][i][self.size-1] = tempColumn[i]


    def rotateTopClockwise(self):
        # Rotate the top face clockwise
        self.rotateFaceClockwise("Top")
        # Save the first row of the front face 
        temp = self.face["Front"][0]
        # The first row of the front face will become  the first row of the right face
        self.face["Front"][0] = self.face["Right"][0]
        # The first row of the right face will become the first row of the back face 
        self.face["Right"][0] = self.face["Back"][0]
        # The first row of the back face will become the first row of the left face
        self.face["Back"][0] = self.face["Left"][0]
        # The first row of the left face will get its values from the temporary list containing the first row of the front face
        self.face["Left"][0] = temp

    def rotateTopCounterClockwise(self):
        # Rotate the top face counterclockwise 
        self.rotateFaceCounterClockwise("Top")
        # Save the first row of the front face 
        temp = self.face["Front"][0]
        # The first row of the front face becomes the first row of the left face
        self.face["Front"][0] = self.face["Left"][0]
        # The first row of the left face becomes the first row of the back face
        self.face["Left"][0] = self.face["Back"][0]
        # The first row of the back face becomes the first row of the right face
        self.face["Back"][0] = self.face["Right"][0]
        # The right face gets its values from the temporary list containing the first row of the front face
        self.face["Right"][0] = temp

    def rotateDownClockwise(self):
        # Rotate the bottom face clockwise
        self.rotateFaceClockwise("Down")
        # Save the last row of the front face 
        temp = self.face["Front"][self.size-1]
        # The last row of the front face becomes the last row of the left face
        self.face["Front"][self.size-1] = self.face["Left"][self.size-1]
        # The last row of the left face becomes the last row of the back face 
        self.face["Left"][self.size-1] = self.face["Back"][self.size-1]
        # The last row of the back face becomes the last row of the right face 
        self.face["Back"][self.size-1] = self.face["Right"][self.size-1]
        # The last row of the right face gets its values from the temporary list containing the last row of the front face
        self.face["Right"][self.size-1] = temp
    
    def rotateDownCounterClockwise(self):
        # Rotate the bottom face counterclockwise 
        self.rotateFaceCounterClockwise("Down")
        # Save the last row of the front face 
        temp = self.face["Front"][self.size-1]
        # The last row of the front face becomes the last row of the right face
        self.face["Front"][self.size-1] = self.face["Right"][self.size-1]
        # The last row of the right face becoems the last row of the back face 
        self.face["Right"][self.size-1] = self.face["Back"][self.size-1]
        # The last row of the back face becomes the last row of the left face 
        self.face["Back"][self.size-1] = self.face["Left"][self.size-1]
        # The last row of the left face gets its values from the temporary list containing the last row of the front face
        self.face["Left"][self.size-1] = temp


    def showCube(self):
        "Function that prints each face with each corresponding row of the face."
        print("-------------------------------")
        # For every face of the cube, print each row.
        for face in self.face:
            for row in self.face[face]:
                print(row)
            print()
        print("-------------------------------")

def main(): 
    
    # Create a new cube
    sampleCube = RubiksCube(3)

    # Call the different cube functions.
    sampleCube.rotateFrontClockwise()
    sampleCube.rotateBackClockwise()
    sampleCube.rotateRightCounterClockwise()
    sampleCube.rotateDownClockwise()
    sampleCube.rotateLeftCounterClockwise()
    sampleCube.rotateDownCounterClockwise
    sampleCube.rotateFrontCounterClockwise()
    sampleCube.showCube()
   
main()
