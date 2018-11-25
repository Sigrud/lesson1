price=100
vat_rate=18
vat=price/100*vat_rate
print(vat)

price_not_vat=price-vat
print(price_not_vat)

def get_vat(price,vat_rate):
	vat=price/100*vat_rate
	price_not_vat=price-vat
	print(price_not_vat)

price1=100
vat_rate1=18
get_vat(price1,vat_rate1)

price2=500
vat_rate2=10
get_vat(price2,vat_rate2)

get_vat(50,int('5'))
get_vat(-100,18)

def get_summ(one,two,delimeter=' '):
	return (str(one)+ str(delimeter)+ str(two))

get_summ('hello','world',delimeter='&')
get_summ('hello','world','+')
get_summ('hello','world')

sum_string=get_summ('learn','python')
print(sum_string.upper())
