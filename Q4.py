def sum_of_squares(N):
    if N == 1:
        return 1
    else:
        return N**2 + sum_of_squares(N - 1)
