import argparse

parser = argparse.ArgumentParser()
parser.add_argument("f")
args = parser.parse_args()

print(args.f)
