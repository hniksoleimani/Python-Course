import qrcode
from pyfiglet import Figlet
def show_menu():
      print('1- Add new word')
      print('2- English2Persian')
      print('3- Persian2English')
      print('4- Exit')
def new_word():
      i = len(nest['english'])          
      nest['english'][f'word{i}'] = str(input('Enter word in english:'))
      nest['persian'][f'word{i}'] = str(input('Enter same word in persian:'))
      wordz = []
      header = 'words = ['
      end = ']'

      for l in range(len(nest['english'])):
            wordz.append(nest['english'][f'word{l}'])
            wordz.append(nest['persian'][f'word{l}'])
      myFile = open('Data.txt','w+')
      data = myFile.write(header)
      for k in range(len(nest['english'])):
            data = myFile.write('\n\t\t'+ "'{english'" + ":'" + nest['english'][f'word{k}'] + "', " + "'persian'" + ':' + "'"+ nest['persian'][f'word{k}']+ "'" + '},')
      data = myFile.write('\n' + end)
      myFile.close()
def eng2per():
      translation = []
      state = input('Enter english sentence you want translated to persian:')
      words = state.split(' ')
      for word in words:
            for i in range(len(nest['english'])):
                  if nest['english'][f'word{i}'] == word:
                        translation.append(nest['persian'][f'word{i}'])
      for i in range(len(translation)):
            print(translation[i], end = ' ')
      print()
      a = input('Press any key to continue:')
                    


def per2eng():
      translation = []
      state = input('Enter persian sentence you want translated to english:')
      words = state.split(' ')
      for word in words:
            for i in range(len(nest['persian'])):
                  if nest['persian'][f'word{i}'] == word:
                        translation.append(nest['english'][f'word{i}'])
      for i in range(len(translation)):
            print(translation[i], end = ' ')
      print()
      a = input('Press any key to continue...')

def exit():
      quit()
         
def load():
      print('Loading...')
      myFile = open('Data2.txt','r')
      data = myFile.read()
      word_list = data.split('\n')
      listKey = []
      listVal = []
      for i in range(1,len(word_list)-1):

            word_dict = word_list[i].split(',')
            it = 1
  
            for j in range(len(word_dict)-1):
                  word = word_dict[j].split("'")
                  it += 1
                  
                  if it%2 == 0:
                        listKey.append(word[3])
                  elif it%2 == 1:
                        listVal.append(word[3])
      for l in range(len(listKey)):
            nest['english'][f'word{l}'] = listKey[l]
            nest['persian'][f'word{l}'] = listVal[l]
      
      print('Welcome!')

nest = {'english':{}, 'persian':{}}
while True:

      load()
      show_menu()
      choice = int(input('Please choose a number:'))

      if choice == 1:
            new_word()
      elif choice == 2:
            eng2per()
      elif choice == 3:
            per2eng()
      elif choice == 4:
            exit()
      else:
            print("invalid input")