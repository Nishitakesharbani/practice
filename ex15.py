from sys import argv
script=argv
filename =argv
txt =open("ex15sample.txt")
print(f"Here is youe file {filename}: ")
print(txt.read())
print("Type the filename again: ")
file_again =input(">")
txt_again =open(file_again)
print(txt_again.read())