from os import name
from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = 'c545bc87620d4ced81cbddb8a90b4a51'
__human_name__ = 'for'


""" Write your functions here. """
def shortest_names(countryList):
    shortest = countryList[0]
    newList = []
    for item in countryList:
        if len(shortest) > len(item):
            newList = []
            shortest = item
            newList.append(shortest)
        elif len(shortest) == len(item):
            newList.append(item)
    
    return newList


def most_vowels(countryList):
    vowels = ['a', 'e', 'o', 'i', 'u']
    newList = []
    countstep = 0
    countmax = 0
    countCountry = 0
    for country in countryList:
        lowercase = country.lower()
        count = 0
        countCountry += 1
        for vowel in vowels:
            if vowel in lowercase:
                count += 1
        if count >= countmax:
            countmax = count
            newList.insert(0, country)
        elif count > countstep:
            countstep = count
            newList.insert(countCountry, country)
        elif count < countstep:
            newList.append(country)
    return newList[:3]


def alphabet_set(countryList):
    newList = []
    for item in countryList:
        alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'e', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for letter in alphabet_list:
            if letter in item.lower():
                alphabet_list.remove(letter)
                newList.append(item)
    
    return set(newList)
    
        



# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == '__main__':
    countries = get_countries()

    """ Write the calls to your functions here. """
    shortest_names(countries)
    print(most_vowels(countries))
    alphabet_set(countries)