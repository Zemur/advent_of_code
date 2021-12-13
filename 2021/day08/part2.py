if __name__ == '__main__':
    output_values = 0
    with open('input', 'r') as f:
        while line := f.readline():
            input_data, output = line.strip().split(" | ")
            d = {l: set(s) for s in input_data.split() if (l := len(s)) in (2, 4)}

            n = ""
            for data in output.split():
                data_len = len(data)
                if data_len == 2:
                    n += "1"
                elif data_len == 3:
                    n += "7"
                elif data_len == 4:
                    n += "4"
                elif data_len == 7:
                    n += "8"
                elif data_len == 5:
                    # 2, 3, 5
                    s = set(data)
                    if len(s & d[2]) == 2:
                        n += "3"
                    elif len(s & d[4]) == 2:
                        n += "2"
                    else:
                        n += "5"
                elif data_len == 6:
                    # 0, 6, 9
                    s = set(data)
                    if len(s & d[2]) == 1:
                        n += "6"
                    elif len(s & d[4]) == 4:
                        n += "9"
                    else:
                        n += "0"
            output_values += int(n)

    print(output_values)
