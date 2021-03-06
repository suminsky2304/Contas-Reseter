from datetime import datetime
from time import time

start_time = time()
first_time = True

while True:
	seconds_before_update = 360

	if (time() - start_time >= seconds_before_update) or first_time:
		first_time = False
		start_time = time()

		print(datetime.now(), 'IN')
		with open('contas.txt', 'r') as f:
			lines = [_.strip() for _ in f.readlines()]

		print(datetime.now(), 'OUT')
		with open('reset_contas.txt', 'a+') as f:
			f.write('\n'.join(lines[:10]))

		with open('contas.txt', 'w') as f:
			f.write('\n'.join(lines[10:]))

