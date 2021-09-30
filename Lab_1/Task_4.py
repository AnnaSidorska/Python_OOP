def max_weight(c, w):
    """ Returns the max weight of the gold that fits in knapsack. """
    
    knapsack = [[0 for i in range(capacity + 1)] for i in range(len(w) + 1)]
    """ Build a matrix to find the result. """
    
    for i in range(len(w) + 1):
        for j in range(c + 1):
            if i == 0 or j == 0:
                knapsack[i][j] = 0
            elif w[i - 1] <= j:
                knapsack[i][j] = max(w[i - 1] + knapsack[i - 1][j - w[i - 1]], knapsack[i - 1][j])
            else:
                knapsack[i][j] = knapsack[i - 1][j]

    """ To return the result of the matrix. """
    return knapsack[len(w)][c]


listUserBars = list(map(int, input('Enter bars weights: ').split()))
userBag = int(input('Enter bag capacity: '))
""" User should input list of weights of bars and the capacity of bag. """

print(max_weight(userBag, listUserBars))
""" Prints the max weight of gold. """
