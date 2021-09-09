# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
leek_price = 2
print(f'Leek is {leek_price} euro per kilo.')

leek = 'leek 4'
leek_num = int(leek[-1])

sum_total = leek_price * leek_num

print(sum_total)

broccoli_order = 'broccoli 1.6'
broccoli_price = 2.34

sum_total01 = round(broccoli_price * float(broccoli_order[-3:]), 2)

print(broccoli_order[-3:] + 'kg broccoli costs ' + str(sum_total01) + 'e')
