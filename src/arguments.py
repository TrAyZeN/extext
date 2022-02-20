import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Extract text data on the screen")

    parser.add_argument("-q", "--quiet", action="store_true",
                        help="Don't print recognized text")
    parser.add_argument("-c", "--clipboard", action="store_true",
                        help="Save the recognized text to clipboard")

    return parser.parse_args()
