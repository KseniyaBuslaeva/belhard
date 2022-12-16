#TODO На вход функции подается целое число N,
# сгенерировать треугольник паскаля глубиной N
def pascal_triangle(deep: int) -> list:
    line_0 = [1]
    line_1 = [1, 1]
    triangle = [line_0] + [line_1] + [[1] + [1]*i for i in range(2, deep + 1)]

    for i in range(2, len(triangle)):
        for j in range(1, len(triangle[i]) - 1):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    return triangle


if __name__ == '__main__':
    print(pascal_triangle(8))
