class salespersons:
    def __init__(self, salesperson_name, salesperson_commission):
        self.salesperson_name = salesperson_name
        self.salesperson_commission = salesperson_commission
class items:
    def __init__(self, name, price, quantity, tax_rate,sales_man_sold):
        self.name = name
        self.price=price
        self.quantity=quantity
        self.tax_rate=tax_rate
        self.sales_man_sold=sales_man_sold
print('Welcome to Data Entry system ')
salespersonslist=[]
itemlist=[]
salesperson=salespersons('','')
item=items('',0,0,0.0)
while(True):
    opt=input('Chose the option \nPress 1 for Entering Salesperson Information \nPress 2 for Entering Item information \nPress 3 to Display \nPress 4 to Print \n ')
    if(opt=='1'):
        print('Enter Salesman Data')
        salesperson.salesperson_name=input('Enter salesperson name')
        salesperson.salesperson_commission=input('Enter salesperson commission')
        salespersonslist.append(salesperson)
    if(opt=='2'):
        print('Enter Item Data')
        item.name=input('Enter Item name')
        item.price=(input('Enter Item price'))
        item.quantity=input('Enter Item QTY')
        item.tax_rate=input('Enter tax rate')
        itemlist.append(item)        
    if(opt=='exit'):
        break
    if()
for i in itemlist:
    print(i.name)
    print(i.tax_rate)
    print(i.price)
    print(i.quantity)