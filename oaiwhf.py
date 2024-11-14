import ast
x = "attachment = ['a', 'b', 'c']"
x = x.replace("attachment = ", "")
y = ast.literal_eval(x)
print(type(y))
print(y[-1])
