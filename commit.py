import os
from datetime import datetime
from time import time

start_time = time()
first_time = True

while True:
	seconds_before_update = 30

	if (time() - start_time >= seconds_before_update) or first_time:
		first_time = False
		start_time = time()

		
		os.system("git add .")
		os.system("git commit -m 'm'")
		os.system("git push")
