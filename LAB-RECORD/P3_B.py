def merge_dictionaries():
    print("Enter the first dictionary (key-value pairs separated by commas, e.g., a:1,b:2):")
    dict1_input = input("First dictionary: ")
    dict1 = {k.strip(): v.strip() for k, v in (item.split(":") for item in dict1_input.split(","))}
    
    print("Enter the second dictionary (key-value pairs separated by commas, e.g., x:10,y:20):")
    dict2_input = input("Second dictionary: ")
    dict2 = {k.strip(): v.strip() for k, v in (item.split(":") for item in dict2_input.split(","))}
    
    merged_dict = {**dict1, **dict2}
    print("\nMerged Dictionary:")
    print(merged_dict)

merge_dictionaries()