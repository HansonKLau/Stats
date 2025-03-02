import random
from sklearn.linear_model import LinearRegression

def kFold(k, x, y):
    # create k "even" sets of data
    xgroups, ygroups = getGroups(k, x, y)

    testGroupsX = []
    trainingGroupListsX = []
    testGroupsY = []
    trainingGroupListsY = []

    for i in range(k):
        testGroupsX.append(xgroups[i])
        trainingGroupListsX.append(xgroups[0:i] + xgroups[i+1:])
        testGroupsY.append(ygroups[i])
        trainingGroupListsY.append(ygroups[0:i] + ygroups[i+1:])

    evalScore = 0

    for i in range(k):
        newX = []
        newY = []

        for j in range(len(trainingGroupListsX[i])):
            newX += trainingGroupListsX[i][j]
            newY += trainingGroupListsY[i][j]
        
        # Convert lists to 2D arrays (needed for LinearRegression)
        # Reshaping each element of newX to be a 2D list
        newX = [[xi] for xi in newX]
        newY = [[yi] for yi in newY]

        # Create Linear Regression model (fitting model)
        reg = LinearRegression().fit(newX, newY)
        
        # Predict with testGroup
        # Reshape test data to 2D list
        testX = [[xi] for xi in testGroupsX[i]]  
        predictedY = reg.predict(testX)

        # Calculate the differences between actual and predicted values
        # Flatten to 1D for comparison
        differences = abs(testGroupsY[i] - predictedY.flatten())  

        evalScore += sum(differences)

    return evalScore

def getGroups(k, x, y):
    indicies = list(range(len(x)))

    xgroups = []  # List of groups of x
    ygroups = []  # List of groups of y

    for i in range(k):
        xgroups.append([])
        ygroups.append([])

    for i in range(len(x)):
        random_index = random.randrange(len(indicies))
        num = indicies.pop(random_index)

        xgroups[i % k].append(x[num])
        ygroups[i % k].append(y[num])

    return (xgroups, ygroups)

def main():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [i ** 2 for i in x]
    result = kFold(3, x, y)

    # the larger the Eval score, the poorer the model is
    print("Eval Score (non-linear data):", result)

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [i * 2 for i in x]
    result = kFold(3, x, y)
    # the smaller the Eval score, the better the model is
    print("Eval Score (linear data):", result)

if __name__ == "__main__":
    main()
