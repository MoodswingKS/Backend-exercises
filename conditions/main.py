# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(weather, time_of_day, cow_milking_status, location_cows, season, slurry_tank, grass_status):
    if location_cows == 'pasture' and (time_of_day == 'night' or weather == 'rainy'):
        return 'take cows to cowshed'
    
    if location_cows == 'cowshed' and cow_milking_status == True:
        return 'milk cows'
    elif cow_milking_status == True and location_cows != 'cowshed':
        return 'take cows to cowshed\nmilk cows\ntake cows back to pasture'

    if slurry_tank == True:
        if location_cows == 'cowshed' and weather != ('sunny' or 'windy'):
            return 'fertilize pasture'
        elif location_cows != 'cowshed' and weather != ('sunny' or 'windy'):
            return 'take cows to cowshed\nfertilize pasture\ntake cows back to pasture'
    
    if location_cows != 'pasture':
        if grass_status == True and season == 'spring' and weather == 'sunny':
            return 'mow grass'
    elif location_cows == 'pasture':
        if grass_status == True and season == 'spring' and weather == 'sunny':
            return 'take cows to cowshed\nmow grass\ntake cows back to pasture'
        
    return 'wait'

print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))
