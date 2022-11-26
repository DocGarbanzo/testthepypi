import sys


def lets_go(s='pypi'):
    print(f'Hallo {s}')


def main():
    if len(sys.argv) > 1:
        lets_go(sys.argv[1])
    else:
        lets_go()
