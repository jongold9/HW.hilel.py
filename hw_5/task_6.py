dicts = {'first_color': 'Red', 'second_color': None, 'third_color': 'Green', 'Fourth_color': None}
dicts = {key: val for key, val in dicts.items() if val is not None}
print(dicts)

