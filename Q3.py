def sum_of_even_numbers(N):
    if N == 1:
        return 2
    else:
        return 2 * N + sum_of_even_numbers(N - 1)
