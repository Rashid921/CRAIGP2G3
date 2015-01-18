import json
import urllib2
import urllib
import csv

url = "http://dev.c0l.in:8888"
response = urllib2.urlopen(url).read()
data = json.loads(response.decode('utf8'))
#commands that appear in python

   #the value of company is set to yes
company = "yes"
while company == "yes" or company == "y":
    ID = input("Insert a company ID=")
    sector = data[ID]['sector']
    print 'the sector is: ' + sector
    purchases = data[ID]['company']['purchases']
    print 'the purchases are: ' + str(purchases)
    name = data[ID]['company']['name']
    print 'the company name is: ' + name
    interestpayable = data[ID]['company']['interest_payable']
    print 'the interest)payable is: ' + str(interestpayable)
    sales = data[ID]['company']['sales']
    print 'the sales are: ' + str(sales)
    expenses = data[ID]['company']['expenses']
    print 'the expenses are: ' + str(expenses)
    interestreceivable = data[ID]['company']['interest_receivable']
    print 'the interest receivable is: ' + str(interestreceivable)
    openingstock = data[ID]['company']['opening_stock']
    print 'the opening stock is: ' + str(openingstock)
    closingstock = data[ID]['company']['closing_stock']
    print 'the closing stock is: ' + str(closingstock)
    id = data[ID]['id']
    print 'the id is: ' + str(id)
    fiscalyearbeginning = data[ID]['fiscal_year_beginning']
    print 'the fiscal year beginning is: ' + str(fiscalyearbeginning)
    
    #ask the user is he wants to view details about another company
    company = raw_input("Do you want to see details about another company? y or n: ") 

if company == "no" or "n":
    print "You chose to stop viewing details about companies"



#commands that appear in csv file
            
    with open('api8888.csv', 'w') as csvfile:
        fieldnames = ['sector', 'purchases', 'name', 'interest_payable', 'sales', 'expenses', 'interest_receivable', 'opening_stock', 'closing_stock', 'id', 'fiscal_year_beginning']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(5000):
            sector1 = data[i]['sector']
            purchases1 = data[i]['company']['purchases']
            name1 = data[i]['company']['name']
            interestpayable1 = data[i]['company']['interest_payable']
            sales1 = data[i]['company']['sales']
            expenses1 = data[i]['company']['expenses']
            interestreceivable1 = data[i]['company']['interest_receivable']
            openingstock1 = data[i]['company']['opening_stock']
            closingstock1 = data[i]['company']['closing_stock']
            id1 = data[i]['id']
            fiscalyearbeginning1 = data[i]['fiscal_year_beginning']
            writer.writerow({'sector': sector1, 'purchases': purchases1, 'name': name1,'interest_payable': interestpayable1, 'sales': sales1, 'expenses': expenses1, 'interest_receivable': interestreceivable1, 'opening_stock': openingstock1, 'closing_stock': closingstock1, 'id': id1, 'fiscal_year_beginning': fiscalyearbeginning1 })
            i+=1
