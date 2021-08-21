print("Lets practice everything.")
print("you \'d need to know \' bout escapes with \\ that do:")
print("\n new line \t tabs")
poem="""
\t The lovely word
with logic so firely planted 
cannot discern \n the needs of love
nor comprehend passion from intution
and requires an exlanation
\n\twhere there is none
"""
print("--------------------")
print(poem)
print("--------------------")
five = 10-2+3-6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans=started*500
    jars=jelly_beans/1000
    craters=jars/100
    return jelly_beans,jars,craters
start_point=10000
beans,jars,craters=secret_formula(start_point)

print("With a starting point{}".format(start_point))
print(f"We'd have {beans} beans,{jars} jars,{craters} craters.")

print("we can also do that this way:")
formula=secret_formula(start_point)
print("We'd have {} beans,{} jars,{} craters.".format(*formula))