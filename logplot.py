import argparse
import json
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('logfiles', type=str, nargs='+', help='log files')
parser.add_argument('-x', type=str, default='epoch')
parser.add_argument('-y', type=str, default='validation/main/accuracy')
parser.add_argument('--xlabel', type=str, default='epoch')
parser.add_argument('--ylabel', type=str, default='accuracy')
parser.add_argument('-o', '--output', type=str, default=None)
args = parser.parse_args()

plt.xlabel(args.xlabel)
plt.ylabel(args.ylabel)

for file in args.logfiles:
    x = []
    y = []
    with open(file, 'r') as f:
        log = json.load(f)
        for data in log:
            x.append(data[args.x])
            y.append(data[args.y])
    plt.plot(x, y, label=file)
plt.legend(loc='upper left')

if args.output:
    plt.savefig(args.output)

plt.show()
