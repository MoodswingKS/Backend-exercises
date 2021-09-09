# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name, greeting_template='Hello, <name>!'):
    return greeting_template.replace('<name>', name)

def force(mass, body='earth'):
    surface_gravity = { 
        'earth': 9.8, 
        'sun': 274, 
        'jupiter': 24.9, 
        'neptune': 11.2, 
        'saturn': 10.4, 
        'uranus': 8.9, 
        'venus': 8.9, 
        'mars': 3.7, 
        'mercury': 3.7, 
        'moon': 1.6, 
        'pluto': 0.6 }
    return mass * surface_gravity[body]

def pull(m1, m2, d):
    # G is the gravitational constant, approximately 6.674×10-11 N m2/kg2
    G = 6.674 * (10 ** -11)
    F = G * ((m1 * m2) / (d ** 2))
    return F