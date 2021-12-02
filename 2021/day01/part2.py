import shared

if __name__ == '__main__':
    depths = shared.read_input()
    sum_windows = [sum(depths[i:i+3]) for i in range(len(depths)) if i+3 <= len(depths)]
    print(shared.compare_depth(sum_windows))
