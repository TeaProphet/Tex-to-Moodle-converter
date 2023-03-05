from sys import argv

usage = 'Usage: python3 tex-to-moodle-converter.py <path to tex file>'
try:
    if len(argv) == 1 or argv[1] == '--help':
        print(usage)
    else:
        path_to_tex = argv[1]
        file = open(path_to_tex, 'r')
        lines = file.readlines()
        file.close()
        for i in range(len(lines)):
            lines[i] = lines[i].replace("\\\\", "")
            is_first_dollar = True
            j = 0
            while j < len(lines[i]):
                if '$' == lines[i][j]:
                    if is_first_dollar:
                        lines[i] = lines[i].replace('$', '\\(', 1)
                        is_first_dollar = False
                        j += 1
                    else:
                        lines[i] = lines[i].replace('$', '\\)', 1)
                        is_first_dollar = True
                        j += 1
                j += 1
        if path_to_tex.__contains__('.'):
            new_path = path_to_tex.split('.')
            new_path = new_path[0] + '-moodle.' + new_path[1]
        else:
            new_path = path_to_tex + '-moodle'
        file = open(new_path, 'w')
        file.writelines(lines)
        file.close()
except FileNotFoundError:
    print("File doesn't exist.")
    print(usage)
