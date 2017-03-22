import csv, argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('--save', '-s', help='save emails, consider data outdated', action='store_true')
parser.add_argument('--reset', '-r', help='reset, forget saved data (except baby.data)', action='store_true')
args = parser.parse_args()

whats = ['účastník', 'náhradník']
babas = [True, False]

B = [ x for x in open('baby.data').read().splitlines() ]

SAVED = []
if os.path.exists('sent.data'):
	SAVED = [ x.split() for x in open('sent.data').read().splitlines() ]

C = []
for what in whats:
	for baba in babas:
		A = [
			( x['user__first_name'] + ' ' + x['user__last_name'], x['user__email'] )
			for x in csv.DictReader(open('data'))
			if x['type'] == what and not (baba ^ (x['user__first_name'] in B))
		]
		C.extend([x[1] + ' ' + what for x in A])

		# filtering out good ol' non-changed fellas
		SSS = [x[0] for x in SAVED if x[1] == what]
		A = list(filter(lambda x: x[1] not in SSS, A))

		# voulaaa -- printing out data
		if not (args.save or args.reset):
			print(what + ' (' + ('baba' if baba else 'chalan') + '):')

			if len(A):
				# print('\n'.join([', '.join(x) for x in A])) # meno, email
				# print('\n'.join([x[0] for x in A])) # meno
				print('\t' + ', '.join([x[1] for x in A])) # email, email, ...
			else:
				print('\t' + 'No good ol\' fella here.')

			print()


if args.save:
	open('sent.data', 'w').writelines('\n'.join(C) + '\n')
	print('Success!')
	exit()

if args.reset:
	if os.path.exists('sent.data'):
		os.remove('sent.data')
		print('Success!')
	else:
		print('Oh, come on, no sent.data file there...')
	exit()
