import csv, sys, os

if not os.path.exists('baby.data'):
	open('baby.data', 'w')
B = set([ x for x in open('baby.data', 'r').read().splitlines() ])

A = set([
	x['user__first_name']
	for x in csv.DictReader(open('inv.data'))
	if x['type'] != 'vedúci' and x['user__first_name'] not in B
])

for x in A:
	sys.stdout.write(x + '? ')
	sys.stdout.flush()
	if sys.stdin.readline() != '\n':
		B.add(x)

open('baby.data', 'w').writelines('\n'.join(B) + '\n')
