a = input("a: ")
b = input("b: ")

#Simultaneously switches values without using a temporary variable
#Example using temp: temp = a a = b b = temp
a,b = b,a

print("a: " + a)
print("b: " + b)
