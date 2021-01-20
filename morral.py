
def morral(size, weight, values, i):
    
    if i == 0 or size == 0:
        return 0

    if weight[i - 1] > size:
        return morral(size, weight, values, i - 1)

    return max(values[i - 1] + morral(size - weight[i - 1], weight, values, i -1),
                morral(size, weight, values, i - 1))


if __name__ == "__main__":
    values = [60, 100, 120]
    weight = [10, 20, 30]
    size = 5
    i = len(values)

    resultado = morral(size, weight, values, i)
    print(resultado)