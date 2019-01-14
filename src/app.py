import os
import sys
import getopt
from inspector import Inspector

DEFAULT_PATH = os.path.expanduser('~')


def pprint(lang, count):
    if len(lang) < 10:
        lang += ' ' * (10-len(lang))
    print('%s: %d' % (lang, count))

def main(argv):
    try:
      opts, args = getopt.getopt(argv,"p:",["path="])
    except getopt.GetoptError:
        print('Usage: holmes -p <path>')
        sys.exit(1)
    path = DEFAULT_PATH
    for opt, arg in opts:
        if opt == '-p':
            path = arg
    print('Set path to %s' % path)
    print('Inspecting your folders, please be patient...')
    i = Inspector(path=path)
    for lang, count in i.stats.items():
        pprint(lang, count)

if __name__ == '__main__':
    main(sys.argv[1:])

