from sys import argv
from os.path import exists
script,from_file,to_file=argv
print(f"coping from {from_file} to {to_file}")
in_file=open(from_file)
indata=in_file.read()
print(f"The indicate file is {len(indata)} bytes long")
print (f"Does the output file exists? {exists(to_file)}")
print("ready hit return to continue or cntrl c to abort")
input()
out_file=open(to_file,'w')
out_file.write(indata)
print("Alright all done")
input()
in_file.close
out_file.closee