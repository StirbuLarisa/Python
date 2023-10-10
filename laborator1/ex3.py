
def count_occ (string, text):
    count = 0
    index = 0

    while True:
        index = text.find(string, index)  #cauta string in text de la pozitia index si returneaza pozitia
        if index == -1:
            break
        count+=1
        index+=1

    return count


if __name__ == '__main__':

    string = input("sirul care trebuie cautat:")
    text = input("textul in care se cauta:")

    result = count_occ(string,text)

    print (f"{string} se afla de {result} ori in {text}")