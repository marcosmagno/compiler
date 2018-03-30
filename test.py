
g = open("HelloJavinha.jvn","r")
count = 10
while True:
  count = count + 1
  
  c = g.read(1)
  if c == ";":
  	print "ddddd"
  	
	lookhead =  g.tell()
	print "ddddddddddddddddddddddddddddddddddd" , lookhead
	g.seek(lookhead+10)


  
  if not c:
    print "End of file"

    break
  print "Read a character:", c
  


'''
fo = open("HelloJavinha.jvn", "rw+")


# Again set the pointer to the beginning
fo.seek(5, 0)
line = fo.read(1)
print "seed: %s" % (line)

# Close opend file
fo.close()

'''