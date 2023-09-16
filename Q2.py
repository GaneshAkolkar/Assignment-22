def sum_of_odd_numbers(N):
    if N == 1:
        return 1
    else:
        return 2 * N - 1 + sum_of_odd_numbers(N - 1)
