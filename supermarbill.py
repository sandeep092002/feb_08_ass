sugar=40
salt=20
dal=120
oil=140
bir_par=140
sugarquan=int(input('Enter sugar quantity: '))
saltquan=int(input('Enter salt quantity: '))
dalquan=int(input('Enter urad daal quantity: '))
oilquan=int(input('Enter oil packets quantity: '))
bir_parquan=int(input('Enter biryani particulars quantity: '))
total=(sugarquan*sugar)+(saltquan*salt)+(dalquan*dal)+(oilquan*oil)+(bir_parquan*bir_par)
if total>=5000:
    disc=total*10/100
    tax=total*10/100
elif total>=3000:
    disc=total*8/100
    tax=total*10/100
elif total>=2000:
    disc=total*5/100
    tax=total*18/100
elif total>=1000:
    disc=total*3/100
    tax=total*18/100
else:
    disc=0
    tax=total*18/100
marketbill=total-disc+tax
print('super market bill: ',marketbill)
