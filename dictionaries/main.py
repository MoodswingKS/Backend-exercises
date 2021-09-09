__winc_id__ = '25a8041d2d5e4e3ab61ab1be43bfb863'
__human_name__ = 'dictionaries'

def create_passport(name, dateOfBirth, placeOfBirth, height, nationality):
    passport = {
        'name':name,
        'date_of_birth':dateOfBirth,
        'place_of_birth':placeOfBirth,
        'height': height,
        'nationality': nationality
    }
    return passport

def add_stamp(passport, country):
    if country not in passport.values():
        if 'stamps' not in passport:
            passport['stamps'] = [country]
        elif 'stamps' in passport:
            passport['stamps'].append(country)
    return passport

def check_passport(passport, country, allowedCountries, notAllowedCountries):
    # . Ik moet checken of de country niet in birthplace of in stamps van passport zit.
    # Vervolgens of de country een allowedcountry is, op basis van de birthplace.
    # En als laatste of er geen stamps zijn, die volgens de country notallowedcountries zijn..

    if country not in passport.values():
        checkPlace = passport.keys('place_of_birth')
        notAllowed = notAllowedCountries.keys(checkPlace)
        if checkPlace in allowedCountries.keys(checkPlace):
            stampValue = passport.keys('stamps')
            if passport.keys('stamps') not in passport.keys():
                add_stamp(passport, country)
            elif stampValue not in notAllowed:
                add_stamp(passport, country)
    return False
