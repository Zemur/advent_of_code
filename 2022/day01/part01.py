if __name__ == '__main__':
    with open('input') as f:
        print(sum(sorted([sum(list(map(int, i.split('\n')))) for i in f.read().split('\n\n')], reverse=True)[0:3]))
