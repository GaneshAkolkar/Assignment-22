def sum_of_cubes(N):
    if N == 1:
        return 1
    else:
        return N**3 + sum_of_cubes(N - 1)
