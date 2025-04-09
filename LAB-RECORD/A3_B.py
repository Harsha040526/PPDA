def merge_dictionaries():
    print("Enter the first dictionary (key-value pairs separated by commas, e.g., a:1,b:2):")
    dict1_input = input("First dictionary: ")
    dict1 = {k.strip(): int(v.strip()) for k, v in (item.split(":") for item in dict1_input.split(","))}
    
    print("Enter the second dictionary (key-value pairs separated by commas, e.g., a:5,c:3):")
    dict2_input = input("Second dictionary: ")
    dict2 = {k.strip(): int(v.strip()) for k, v in (item.split(":") for item in dict2_input.split(","))}
    
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    
    print("\nMerged Dictionary:")
    print(merged_dict)

merge_dictionaries()