import os



dict_1 = os.environ

for name in dict_1:
	print "%s => %s" % (name,dict_1[name])
