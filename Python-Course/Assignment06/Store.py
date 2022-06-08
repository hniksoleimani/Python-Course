import qrcode
from pyfiglet import Figlet
def show_menu():
      print('1- Add Product')
      print('2- Edit Product')
      print('3- Delete Product')
      print('4- Search')
      print('5- Show List')
      print('6- Buy')
      print('7-Qr code')
      print('8- Exit')
def add_product():
      mydict = {}
      mydict['ID'] = input('Enter product ID:')
      mydict['Name'] = input('Enter product Name:')
      mydict['Price'] = input('Enter product Price:')
      mydict['Count'] = input('Enter product Count:')
      Products.append(mydict)
      myFile = open('Database.txt','a+')
      data = myFile.write('\n' + mydict['ID'] + ', ' + mydict['Name'] + ', ' + mydict['Price'] + ', ' + mydict['Count'])

def edit_product():
      oldName = input('Enter product name you want to change:')
      for i in range(len(Products)):
            if Products[i]['Name'] == ' ' + oldName:
                  mydict = {}
                  mydict['ID'] = input('Enter new product ID:')
                  mydict['Name'] = ' ' + input('Enter new product Name:')
                  mydict['Price'] = ' ' + input('Enter new product Price:')
                  mydict['Count'] = ' ' + input('Enter new product Count:')
                  Products[i] = mydict
                  myFile = open('Database.txt','w+')
                  for i in range(len(Products)):
                        data = myFile.write(Products[i]['ID'] + ',' + Products[i]['Name'] + ',' + Products[i]['Price'] + ',' + Products[i]['Count']+ '\n')

                        
def find_product():
      Name = input('Enter product name you want to find:')
      for i in range(len(Products)):
            if Products[i]['Name'] == ' ' + Name:
                  print(Products[i].values())

def delete_product():
      Products2 = []
      Name = input('Enter product name you want to delete:')
      for i in range(len(Products)):
            if Products[i]['Name'] != ' ' + Name:
                  Products2.append(Products[i])
      
      myFile = open('Database.txt','w+')
      for i in range(len(Products2)):
            data = myFile.write(Products2[i]['ID'] + ',' + Products2[i]['Name'] + ',' + Products2[i]['Price'] + ',' + Products2[i]['Count']+ '\n')

def purchase():
      id = input('Enter product ID you wish to buy:')
      for i in range(len(Products)):
            if Products[i]['ID'] == id:
                  mydict = {}
                  goods = int(Products[i]['Count'])
                  amount = int(input('Enter the amount you wish to buy:'))
                  if goods >= amount:
                        Products[i]['Count'] = str(goods - amount)
                        total = amount*int(Products[i]['Price'])

                        mydict['ID'] = Products[i]['ID']
                        mydict['Name'] = Products[i]['Name']
                        mydict['Price'] = Products[i]['Price']
                        mydict['Amount'] = str(amount)
                        mydict['Total'] = str(total)
                        Reciept.append(mydict)
                        shop = int(input('Continue buying[1], Print reciept[2]:'))
                        if shop == 1:
                              purchase()
                        elif shop == 2:
                              reciept()
                              exit()
                        else:
                              print('Invalid input.')
                              reciept()
                              exit()
                  else:
                        print('Stocks not available.')
                        purchase()
            print('ID does not exist.')
            purchase()


def exit():
      Products = []
      myFile = open('Database.txt','w+')
      for i in range(len(Products)):
            data = myFile.write(Products[i]['ID'] + ',' + Products[i]['Name'] + ',' + Products[i]['Price'] + ',' + Products[i]['Count']+ '\n')
      quit()


def reciept():
      grandTotal = 0
      print(Reciept[0].keys())
      print('------------------------------------------------')
      for i in range(len(Reciept)):
            print(Reciept[i].values())
            grandTotal += int(Reciept[i]['Total'])
      print('------------------------------------------------')
      print(grandTotal, '$')


def Qr():
      id = input('Enter product ID you wish to buy:')
      for i in range(len(Products)):
            if Products[i]['ID'] == id:
                  img =qrcode.make(Products[i])
                  img.save('qrcode.png')
                  quit()
            print('ID does not exist.')
            Qr()
            
def show_list():
      for i in range (len(Products)):
            print(Products[i])
def load():
      print('Loading...')
      myFile = open('Database.txt','r')
      data = myFile.read()
      product_list = data.split('\n')
      for i in range(len(product_list)):
            mydict = {}
            product_info = product_list[i].split(',')
            mydict['ID'] = product_info[0]
            mydict['Name'] = product_info[1]
            mydict['Price'] = product_info[2]
            mydict['Count'] = product_info[3]
            Products.append(mydict)
      print(len(Products))
      print(data)
      print('Welcome!')


Reciept = []
Products = []

f = Figlet(font = 'Standard')
print(f.renderText('Hani Shop'))
load()
show_menu()
choice = int(input('Please choose a number:'))

if choice == 1:
      add_product()
elif choice == 2:
      edit_product()
elif choice == 3:
      delete_product()
elif choice == 4:
      find_product()
elif choice == 5:
      show_list()
elif choice == 6:
      purchase()
elif choice == 7:
      Qr()
elif choice == 8:
      exit()
else:
      print("invalid input")