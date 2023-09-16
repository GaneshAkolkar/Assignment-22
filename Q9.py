def decimal_to_octal(n):
    if n == 0:
        return ""
    else:
        return decimal_to_octal(n // 8) + str(n % 8)
