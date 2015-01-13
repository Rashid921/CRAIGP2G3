import csv
import urllib2
import urllib
import json

url = "http://dev.c0l.in:8888/1234"
response = urllib2.urlopen(url).read()
data = json.loads(response.decode('utf8'))

#commands that appear in python
sector = data['sector']
print 'the sector is: ' + sector
purchases = data['company']['purchases']
print 'the purchases are: ' + str(purchases)
name = data['company']['name']
print 'the company name is: ' + name
interestpayable = data['company']['interest_payable']
print 'the interest)payable is: ' + str(interestpayable)
sales = data['company']['sales']
print 'the sales are: ' + str(sales)
expenses = data['company']['expenses']
print 'the expenses are: ' + str(expenses)
interestreceivable = data['company']['interest_receivable']
print 'the interest receivable is: ' + str(interestreceivable)
openingstock = data['company']['opening_stock']
print 'the opening stock is: ' + str(openingstock)
closingstock = data['company']['closing_stock']
print 'the closing stock is: ' + str(closingstock)
id = data['id']
print 'the id is: ' + str(id)
fiscalyearbeginning = data['fiscal_year_beginning']
print 'the fiscal year beginning is: ' + str(fiscalyearbeginning)

#commands that appear in csv file
with open('p2.csv', 'w') as csvfile:
    fieldnames = ['sector', 'purchases', 'name', 'interest_payable', 'sales', 'expenses', 'interest_receivable', 'opening_stock', 'closing_stock', 'id', 'fiscal_year_beginning']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'sector': sector, 'purchases': purchases, 'name': name,'interest_payable': interestpayable, 'sales': sales, 'expenses': expenses, 'interest_receivable': interestreceivable, 'opening_stock': openingstock, 'closing_stock': closingstock, 'id': id, 'fiscal_year_beginning': fiscalyearbeginning })
    writer.writerow({'sector': 'Asfs', 'name': 'lalala'})
    writer.writerow({'sector': 'ddsf', 'name': 'tuiyhn'})
