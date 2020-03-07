import argparse, sys

parser=argparse.ArgumentParser()

parser.add_argument('--dir', help='O diretório onde se encontram os livros')
parser.add_argument('--teste', help='teste livros')

args=parser.parse_args()

print(args.dir)
