list_price = []

global tax_rate 
tax_rate = 0.08

def display(taxed, total_cost, list_price, subtotal):
    print(f"""
        LIST OF PRICES: {list_price}
        TAX: {taxed}
        SUBTOTAL: {subtotal}
        TOTAl COST: {total_cost}
        """)
    
def calculate_total(list):
    subtotal = 0
    for i in list:
        subtotal += i

    taxed = subtotal * tax_rate
    total_cost = subtotal + taxed
    display(taxed, total_cost, list_price, subtotal)
        
run = True

while run:
    print('Enter a price. Type [stop] to exit the program.')
    price = (input('>> '))
    if price == 'stop':
        calculate_total(list_price)
        break
    else:
        price = int(price)
        list_price.append(price)
        print(list_price, end='\n\n')
        continue