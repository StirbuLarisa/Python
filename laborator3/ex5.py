def validate_dict(rules, d):

## inceputul acesta lipsea, aici fac check daca key din dictionar
# se aflat printre regulile date, de asta key3 era considerat corect
# chiar daca el era gresit
    rules_keys = []
    for rule in rules:
        rules_keys.append(rule[0])

    for k in d:
        if k not in rules_keys:
            return False

    ###### aici pentru fiecare key din reguli este testat
    #daca se gaseste in dictionarul care trebuie verificat
    for key, prefix, middle, suffix in rules:

        if key in d:
            value = d[key]
            if not value.startswith(prefix):
                return False
            if middle not in value[1:-1]:
                return False
            if not value.endswith(suffix):
                return False
        else:
            return False

    return True

rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
data = {
    "key1": "come inside, it's too cold out",
    "key2": "start in middle of the winter",
    "key3": "this is not valid"
}

result = validate_dict(rules, data)
print(result)
