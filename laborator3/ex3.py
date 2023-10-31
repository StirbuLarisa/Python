def compare_dicts(dict1, dict2):
    if len(dict1) != len(dict2):
        return False

    for key in dict1:
        if key not in dict2:
            return False

        value1 = dict1[key]
        value2 = dict2[key]

        if isinstance(value1, dict) and isinstance(value2, dict):
            if not compare_dicts(value1, value2):
                return False
        elif isinstance(value1, list) and isinstance(value2, list):
            if len(value1) != len(value2):
                return False
            for i in range(len(value1)):
                if value1 != value2:
                    return False
        elif value1 != value2:
            return False

    return True

dict1 = {
    "nume": 'ana',
    'ani': 16,
    'adresa': {'oras': 'iasi', 'nr': '12345'},
    'ore': [{'oras': 'iasi', 'nr': '12345'},'python', 'java'],
}

dict2 = {
    'nume': 'ana',
    'ani': 16,
    'adresa': {'oras': 'iasi', 'nr': '12345'},
    'ore': [{'oras': 'iasi', 'nr': '12345'},'python', 'java'],
}

result = compare_dicts(dict1, dict2)
print(result)
