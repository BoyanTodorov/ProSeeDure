__author__ = 'boyan'

import os

path = '/home/pi/milara/procedures/'


def read_contents(path_to_procedures):
    root = []
    dirs = []
    files = []

    for directory, dir_names, file_names in os.walk(path_to_procedures):
        root = directory
        dirs = dir_names
        files = file_names

    return files


def draw_menu(list_of_files):
    os.system('clear')

    menu = ''
    logo = '{0}\n{1:*^125}\n{0}\n'.format('=' * 125, ' Milara Inc. ')
    begin = '|*'
    end = '*|\n'
    menu += logo

    for i in range(len(file_list)):
        menu += '{0}{1:2} -> {2:115}{3:>3}'.format(begin, i + 1, file_list[i], end)
    menu += '=' * 125
    print(menu)


def select_file():
    selected = input('Select a procedure and type its number:')

    is_valid_selection = 1 <= int(selected) <= len(file_list)

    while not is_valid_selection:
        selected = input('Invalid procedure number\nPlease enter number in range [1 - {0}]\n'.format(list_length))
        is_valid_selection = 1 <= int(selected) <= len(file_list)

    sys_string = 'evince -f -i 1 {0}{1} 2> /dev/null'.format(path, file_list[int(selected) - 1])
    os.system(sys_string)
    # print(sys_string)


file_list = read_contents(path)
list_length = len(file_list)

# Starting the program
draw_menu(read_contents(path))
select_file()
