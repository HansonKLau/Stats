import random

# list of x
# list of y


# def kFold(k, x, y):

#     # create k "even" sets of data

#     indicies = []

#     for i in range(len(x)):
#         indicies.append(i)

#     last = -1

#     if len(x) % k != 0:
#         last = len(x) - (k * (len(x) // k))
#         5 - (3 * (5 // 3)) = 5 - (3 * 1)

    
#     xgroups = [] # list of groups of x

#     ygroups = [] # list of groups of y

#     for i in range(k):

#         xgroup = []
#         ygroup = []

#         if i == k - 1 and last != -1:
#             for j in range(last):
#                 random_index = random.randrange(len(indicies))
#                 num = indicies.pop(random_index)
#                 xgroup.append(x[num])
#                 ygroup.append(y[num])

#         else:
#             for j in range(len(x) // k):
#                 random_index = random.randrange(len(indicies))
#                 num = indicies.pop(random_index)
#                 xgroup.append(x[num])
#                 ygroup.append(y[num])
        
#         xgroups.append(xgroup)
#         ygroups.append(ygroup)
    
#     return (xgroups, ygroups)


def kFold(k, x, y):

    # create k "even" sets of data
    xgroups, ygroups = getGroups(k, x, y)

    # take out one group to use as test data
    # use the remaing groups as training

    # there will be a total of k evaluation scores
    evalScore = 0
    testGroups = []
    trainingGroupLists = []

    #ex test group = [[1, 2, 3]  ]
    #ex training group list = [[[2, 4, 6], [3, 5, 7]]  ]



    # [1, 2, 3, 4, 5]


    for i in range(k):
        testGroups.append(xgroups[i])
        trainingGroupLists.append(xgroups[0:i] + xgroups[i+1:len(xgroups)])
    
    print(testGroups)
    print(trainingGroupLists)



def getGroups(k, x, y):
    indicies = []

    for i in range(len(x)):
        indicies.append(i)

    
    xgroups = [] # list of groups of x
    ygroups = [] # list of groups of y

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

    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    kFold(3, x, y)



if __name__ == "__main__":
    main()