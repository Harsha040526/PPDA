BCA = {
"1": "Swaroop",
"2": "Ram",
"3": "Neel"
}
for key in BCA:
    print(key)
    
#calling values    
print("Here are the values")
for key in BCA:
    print(BCA[key])
    
#adding new element
BCA["4"]="Aryan"
print(BCA.values())
print(BCA.keys())
print(BCA.items())

for key, values in BCA.items():
    print(key,values)
    
print(BCA)
if "5" in BCA:
    print("I am here")
else:
    print("NO")
