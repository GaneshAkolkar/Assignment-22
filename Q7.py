def decimal_to_binary(n):
    if n == 0:
        return ""
    else:
        return decimal_to_binary(n // 2) + str(n % 2)
