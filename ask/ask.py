#!/usr/bin/env python3

"""Select random students from list to ask questions.

Read lists of students and select random student for questioning from it

Press enter to get a new name
Press 'b' or 'back' to go back to previous student
Press 'x' or 'exit' to exit the script
"""

import random
import sys

USAGE_TPL = '''
Read lists of students and select random student for questioning from it
USAGE:
    {script_name} file_name.txt file_name2.txt ..

Press enter to get a new name
Press 'b' or 'back' to go back to previous student
Press 'x' or 'exit' to exit the script
'''

USAGE_TPL = USAGE_TPL.strip()


def process(filename, sort=True):
    """Expect a text file in UTF-8, with elements separated by \n."""

    # could be done as open().read(), but ctx mgr is better
    with open(filename) as f:
        text = f.read()             # read file as a whole implying it's small
        names = text.splitlines()
        # Filter out empty lines
        names = [name for name in names if name is not ""]
        # print(f'Got names: {names}')
        return names


def selector(sequence):
    """Print random student from list when prompted"""
    elements = list(sequence)   # ensure it's a list
    random.shuffle(elements)    # randomize list
    el = None
    last_element = None
    while elements:
        inputCode = input('Press enter for new name\n')

        if inputCode == "x" or inputCode == "exit":     # exit
            exit()
        elif inputCode == "b" or inputCode == "back":   # print previous element
            if (el is not None) and (last_element is not None):
                # push back previous read element
                elements.insert(0, el)
                random.shuffle(elements)
                el = last_element
                print(f'====>\t{el}')
        elif inputCode == '' or inputCode == "enter":   # print element from list and remove it from there
            last_element = el
            el = elements.pop()
            print(f'====>\t{el}')
        else:
            print("Input either enter, x, exit, b or back\n")


def run(args):
    """Main function."""

    # Separate script name from other args
    script_name = args[0]
    args = args[1:]
    print(f'Args now: {script_name} | {args}')

    # no arguments provided -- print USAGE and exit with error
    if not args:
        text = USAGE_TPL.format(script_name=script_name)
        print(text, file=sys.stderr)
        exit(-1)
    names = []
    # read all files passed as arguments
    for filename in args:
        names += process(filename)
    # print(f'Got names: {names}')
    selector(names)


if __name__ == '__main__':
    run(sys.argv)
