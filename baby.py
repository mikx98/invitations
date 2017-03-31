import csv, sys, os, argparse

parser = argparse.ArgumentParser()
parser.add_argument('--ooh', '-o', help='repair the database', action='store_true')
args = parser.parse_args()

if not os.path.exists('baby.data'):
	open('baby.data', 'w')
B = set([ x for x in open('baby.data', 'r').read().splitlines() ])

if args.ooh:
	R = set()
	for x in B:
		sys.stdout.write(x + '? ')
		sys.stdout.flush()
		if sys.stdin.readline() != '\n':
			R.add(x)
	open('baby.data', 'w').writelines('\n'.join(B - R) + '\n')
	exit()

A = set([
	x['user__first_name']
	for x in csv.DictReader(open('data'))
	if x['type'] != 'vedúci' and x['user__first_name'] not in B
])

for x in A:
	sys.stdout.write(x + '? ')
	sys.stdout.flush()
	if sys.stdin.readline() != '\n':
		B.add(x)

open('baby.data', 'w').writelines('\n'.join(B) + '\n')
