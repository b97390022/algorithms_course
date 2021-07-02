# Course1-Week1-Karatsuba Multiplication


def karatsuba(num_1, num_2):
    num1str, num2str = str(num_1), str(num_2)

    if num_1 < 10 or num_1 < 10:
        return num_1 * num_2

    maxLength = max(len(num1str), len(num2str))

    num1str = "".join(list("0" * maxLength)[: -len(num1str)] + list(num1str))
    num2str = "".join(list("0" * maxLength)[: -len(num2str)] + list(num2str))

    splitLength = maxLength // 2
    a, c = int(num1str[:-(splitLength)]), int(num2str[:-(splitLength)])
    b, d = int(num1str[-(splitLength):]), int(num2str[-(splitLength):])

    a_c = karatsuba(a, c)
    b_d = karatsuba(b, d)
    ad_bc = karatsuba((a + b), (c + d))

    return (
        a_c * (10 ** (2 * splitLength))
        + (ad_bc - a_c - b_d) * (10 ** splitLength)
        + b_d
    )


if __name__ == "__main__":
    karatsuba()
