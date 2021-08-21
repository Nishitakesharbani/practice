from sys import argv
script=argv
input_file=argv
def print_all(f):
    print(f.read())
def rewind(f):
    f.seek(0)
def prinr_a_line(line_count,f):
    print(line_count,f.readline())
current_file=open( ex20.py)
print("First lets print the whole file:\n")
print_all(current_file)
print("Now lets rewind ")
rewind(current_file)
print("lets print three lines")
current_line=1
prinr_a_line(current_line,current_file)