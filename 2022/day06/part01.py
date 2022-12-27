if __name__ == '__main__':
    with open('input') as f:
        datastream = f.read()

    start = 0
    end = 4

    while end <= len(datastream):
        buffer = datastream[start:end]
        start += 1
        end += 1
        if len(buffer) == len(set(buffer)):
            print(end-1)
            break
