def format_price(price):
	round(price)
	return('цена: '+ str(price) + ' руб.')
display_price=format_price(56.24)
print(display_price)