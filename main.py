import csv

what = 'účastník'
# what = 'náhradník'

# baba = True
baba = False

B = [ x for x in open('baby.data').read().splitlines() ]

A = [
	( x['user__first_name'] + ' ' + x['user__last_name'], x['user__email'] )
	for x in csv.DictReader(open('inv.data'))
	if x['type'] == what and not (baba ^ (x['user__first_name'] in B))
]

# print('\n'.join([', '.join(x) for x in A])) # meno, email
# print('\n'.join([x[0] for x in A])) # meno
print(', '.join([x[1] for x in A])) # email, email, ...
