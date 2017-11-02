import os
def main():
	os.system('cls') 
	from datetime import date
	from datetime import time
	from datetime import datetime
	from datetime import timedelta
	now = datetime.today()
	afd = datetime(2018, 4, 2, 14)
	time_to_afd = afd-now
	print "Time untill camp:",time_to_afd.days,"days,",time_to_afd.seconds/60/60,"hours,",(time_to_afd.seconds-(time_to_afd.seconds/60/60)*60*60)/60,"minutes and",time_to_afd.seconds-(time_to_afd.seconds/60)*60,"seconds."
	n = raw_input("Press 'enter' to see new...")
	main()
main()