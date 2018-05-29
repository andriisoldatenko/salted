import sys


def main():
    for line in sys.stdin:
        n, m = map(int, line.strip().split(','))
        matrix = []
        counter = 1
        for i in range(n):
            matrix.append([])
            for _ in range(m):
                matrix[i].append(counter)
                counter += 1
        print(matrix)

if __name__ == '__main__':
    main()
