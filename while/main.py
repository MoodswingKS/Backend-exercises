from hashlib import new
from helpers import random_koala_fact

__winc_id__ = 'c0dc6e00dfac46aab88296601c32669f'
__human_name__ = 'while'

def unique_koala_facts(num):
    fact = ''
    factList = []
    while num > 0:
        fact = random_koala_fact()
        if fact not in factList:
            factList.append(fact)
            num -= 1
    return factList
            
def num_joey_facts():
    koalaCount = 0
    joeyCount = 0
    fact = random_koala_fact()

    while koalaCount < 10:
        newFact = random_koala_fact()
        if newFact == fact:
            koalaCount += 1
        if ('joey' or 'joeys') in newFact:
            joeyCount += 1
    return joeyCount
    

def koala_weight():
    koalaKg = False
    while koalaKg == False:
        fact = random_koala_fact()
        if 'kg' in fact:
            koalaKg = True
            splitFact = fact.split('kg')[0]
            print(splitFact[-2:])
        else: 
            newFact = random_koala_fact()
            fact = newFact
    
    

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == '__main__':
    random_koala_fact()
    print(unique_koala_facts(2))
    print(num_joey_facts())
    print(koala_weight())
