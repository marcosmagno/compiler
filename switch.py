estado = 1
for i in range(0,10):
	print "estado", estado
	a = raw_input()


	if estado == 1:

		if a == 'a':
			print "a"
		elif a == 'b':
			print "b"
			estado = 3
	elif estado == 3:
		
		if a == "c":
			print "c"
			print estado
		else:
			print "err"

