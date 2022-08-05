str=input("Enter the Word:")
length=len(str)
list=[]
print("Encryption Message")
for element in range(0,length):
     c=ord(str[element])
     print(c,end=" ")
     list.append(c)

print("\nDecryption Message")
for element in range(0,length):
     d=chr(list[element])
     print(d,end="")
