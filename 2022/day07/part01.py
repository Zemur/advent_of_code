if __name__ == '__main__':
    with open('input') as f:
        output = [i.strip() for i in f.readlines()]

    pwd = '/'
    command_output = ''
    tree = {}
    directory = {
        'children': [],
        'path': [],
        'size': '',
        'contents':
            [
                #{
                #    'filename': '',
                #    'size': 0
                #}
            ]
    }

    for line in output:
        if line.startswith('$'):
            match line:
                case 'cd':
                    # parse cd
                    cd_param = line.split(' ')[2]
                    if cd_param == '..':
                        # Go up a directory
                        pwd = tree[pwd]['path']
                    else:
                        pwd = line.split(' ')[2]
                        if pwd not in tree.keys():
                            tree[pwd]
        else:
            if line.startswith('dir'):
                if pwd in tree.keys():
                    tree[pwd]['children'].append(line.split(' ')[1])
                else:
                    tree(directory)
            else:
                size, filename = line.split(' ')
                tree[pwd]['contents'].append({'filename': filename, 'size': size})
        print(tree)
