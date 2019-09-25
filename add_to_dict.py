def add_to_dict(key, columns, dictionary):
    if key not in dictionary:
        dictionary[key] = []
        dictionary[key].append(columns)
    else:
        dictionary[key].append(columns)
