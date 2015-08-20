import sys
import getopt
import genetics

def main(argv):
	module_name = ''

    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile="])
    except getopt.GetoptError:
        print('Error: incorrect parameters.\n Usage: mGenetic.py -m <module_name>\n')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Usage: mGenetic.py -m <module_name>\n')
            sys.exit()
        elif opt in ("-m", "--module"):
            module_name = arg

	module = __import__(module_name)

    pass

if __name__ == "__main__":
    main(sys.argv[1:])