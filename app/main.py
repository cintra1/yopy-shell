import sys


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    cmd = input()
    sys.stdout.write("{}: command not found".format(cmd))

if __name__ == "__main__":
    main()
