person = {
	"p1": {"name": "Iniyan", "profession": "engineer"},
	"p2": {"name": "Raj", "profession": "doctor"},
	"p3": {"name": "Sarah", "profession": "teacher"}
}
# Access a value
p1_name = person["p1"]["name"]
# Update a value
person["p1"]["profession"] = "farmer"
# Delete an entry
del person["p2"]
# Iterate through dictionary
for p, details in person.items():
	print(f"{p}:")
for key, value in details.items():
	print(f" {key}: {value}")
