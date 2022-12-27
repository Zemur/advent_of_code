if __name__ == '__main__':
    with open('input') as f:
        print(([sum(list(map(int, i.split('\n')))) for i in f.read().split('\n\n')]))