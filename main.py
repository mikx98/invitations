import csv

whats = ['účastník', 'náhradník']
babas = [True, False]

B = [ x for x in open('baby.data').read().splitlines() ]

for what in whats:
	for baba in babas:
		A = [
			( x['user__first_name'] + ' ' + x['user__last_name'], x['user__email'] )
			for x in csv.DictReader(open('data'))
			if x['type'] == what and not (baba ^ (x['user__first_name'] in B))
		]

		print(what + ' (' + ('baba' if baba else 'chalan') + '):')
		# print('\n'.join([', '.join(x) for x in A])) # meno, email
		# print('\n'.join([x[0] for x in A])) # meno
		print('\t' + ', '.join([x[1] for x in A])) # email, email, ...
		print()
