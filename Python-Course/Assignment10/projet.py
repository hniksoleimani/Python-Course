import pytube
from Media import Media
from Film import Film
from Clip import Clip
from Documentary import Documentary
from Actor import Actor
from Series import Series

    # def load(self):
    #     print('Loading...')
    #     myFile = open('database.txt', 'r')
    #     data = myFile.read() 
    #     media_list = data.split('\n')
    #     for i in range(len(media_list)):
    #         dict = {}
    #         media_info = data.split[i].split(',')
    #         dict['ID'] = media_info[0]
    #         dict['Name'] = media_info[1]
    #         dict['Director'] = media_info[2]
    #         dict['IMDB_score'] = media_info[3]
    #         dict['Duration'] = media_info[4]
    #         dict['Cast'] = media_info[5]
    #         Media_list.append(dict)
    #     print(len(Media_list))
    #     print(data)
    #     print('Welcome...!')

 


Media_list = []
Cast_list = []
# class Dict2Class(object):
#     def __init__(self, dict):
#         for key in dict:
#             setattr(self, key, dict[key])   

def load():
    print('Loading...')
    myFile = open('database.txt', 'r+')
    data = myFile.read() 
    media_list = data.split('\n')   
    for i in range(len(media_list)):
        # dict = {}
        media_info = media_list[i].split(',')
        # dict['ID'] = media_info[0]
        # dict['Name'] = media_info[1]
        # dict['Director'] = media_info[2]
        # dict['IMDB_score'] = media_info[3]
        # dict['Url'] = media_info[4]
        # dict['Duration'] = media_info[5]
        # dict['Cast'] = media_info[6]
        # dict['Type'] = media_info[7]
        # dict['Year'] = media_info[8]
        Cast_list.append(Actor(media_info[6]))
        Media.casts = Cast_list
        if media_info[7] == " 'Film'":
            # dict['Genre'] = media_info[9]

            # result = Dict2Class(dict)
            # Media_list.append(result)
            Media_list.append(Film(media_info[0], media_info[1], media_info[2], media_info[3], media_info[4], media_info[5], media_info[6], None, media_info[8], media_info[9]))

        elif media_info[7] == " 'Series'":
            # dict['numbOfSeasons'] == media_info[9]
            Media_list.append(Series(media_info[0], media_info[1], media_info[2], media_info[3], media_info[4], media_info[5], media_info[6], None, media_info[8], media_info[9]))

        elif media_info[7] == " 'Documentary'":
            # dict['Location'] == media_info[9]
            Media_list.append(Documentary(media_info[0], media_info[1], media_info[2], media_info[3], media_info[4], media_info[5], media_info[6], None, media_info[8], media_info[9]))

        elif media_info[7] == " 'Clip'":
            # dict['Inhr'] == media_info[9]
            Media_list.append(Clip(media_info[0], media_info[1], media_info[2], media_info[3], media_info[4], media_info[5], media_info[6], None, media_info[8], media_info[9]))


        
        # Media_list.append(result)

    print('Welcome...!')
    myFile.close()
def show_menu():
    print('1 - Add Media')
    print('2 - Edit Media')
    print('3 - Delete Media')
    print('4 - Search')
    print('5 - Show list')
    print('6 - Download')
    print('7 - Advanced search')
    print('8 - Exit')
Media_add = [[], [], [], [], [], [], [], [], [], []]
def add_media():
    # dict = {}
    # dict['ID'] = input('Enter ID:')
    # dict['Name'] = input('Enter media name:')
    # dict['Director'] = input('Enter director name:')
    # dict['IMDB_score'] = input('Enter IMDB score:')
    # dict['Url'] = input('Enter url:')
    # dict['Duration'] = input('Enter duration:')
    # dict['Cast'] = input('Enter cast name:')
    # dict['Type'] = input('Enter media type:')
    # if dict['Type'] == 'Film':
    #     dict['Genre'] == input('Enter movie genre:')
    # elif dict['Type'] == 'Series':
    #     dict['numbOfSeasons'] == input('Enter number of seasons:')
    # elif dict['Type'] == 'Documentary':
    #     dict['Location'] == input('Enter documentary location:')
    # elif dict['Type'] == 'Clip':
    #     pass
    # result = Dict2Class(dict)

    Media_add[0] = " " + input('Enter ID:')
    Media_add[1] = " " + input('Enter media name:')
    Media_add[2] = " " + input('Enter director name:')
    Media_add[3] = " " + input('Enter IMDB score:')
    Media_add[4] = " " + input('Enter url:')
    Media_add[5] = " " + input('Enter duration:')
    Media_add[6] = " " + input('Enter cast name:')
    Media_add[7] = " " + input('Enter media type:')
    Media_add[8] = " " + input('Enter media creation year:')
    if Media_add[7] ==  ' Film':
        Media_add[9] == " " + input('Enter movie genre:')
        Media_list.append(Film(Media_add[0], Media_add[1], Media_add[2], Media_add[3], Media_add[4], Media_add[5], Media_add[6], Media_add[7], int(Media_add[8][2:6]), Media_add[9]))

    elif Media_add[7] == ' Series':
        Media_add[9] == " " + input('Enter number of seasons:')
        Media_list.append(Series(Media_add[0], Media_add[1], Media_add[2], Media_add[3], Media_add[4], Media_add[5], Media_add[6], Media_add[7], int(Media_add[8][2:6]), Media_add[9]))

    elif Media_add[7] == ' Documentary':
        Media_add[9] == " " + input('Enter documentary location:')
        Media_list.append(Documentary(Media_add[0], Media_add[1], Media_add[2], Media_add[3], Media_add[4], Media_add[5], Media_add[6], Media_add[7], int(Media_add[8][2:6]), Media_add[9]))

    elif Media_add[7] == ' Clip':
        Media_add[9] == " " + input('Enter clip extension:')
        Media_list.append(Clip(Media_add[0], Media_add[1], Media_add[2], Media_add[3], Media_add[4], Media_add[5], Media_add[6], Media_add[7], int(Media_add[8][2:6]), Media_add[9]))
    else:
        print('Invalid video type')
        
    # myFile = open('database.txt', 'a+')
    # myFile.write('\n' + dict['ID'] + ', ' + dict['Name'] + ', ' + dict['Director'] + ', ' + dict['IMDB_score'] + ', ' + dict['Duration'] + ', ' + dict['Cast'] + ', ' + dict['Type'] + ', ' + dict['Url'])
    # myFile.close()
Media_edit = [[], [], [], [], [], [], [], [], [], []]
def edit_media():
    oldName = input('Enter product name you want to change:')
    for i in range(len(Media_list)):
        if Media_list[i].name == " '" + oldName + "'":
                # dict = {}    
                # dict['ID'] = input('Enter new product ID:')
                # dict['Name'] = ' ' + input('Enter new name for the media:')
                # dict['Director'] = ' ' + input('Enter director`s name:')
                # dict['IMDB_score'] = ' ' + input('Enter IMDB_score:')
                # dict['Url'] = ' ' + input('Enter Media`s url:')
                # dict['Duration'] = ' ' + input('Enter media`s Duration:')
                # dict['Cast'] = ' ' + input('Enter Actor`s name:')
                # dict['Type'] = ' ' + input('Enter Media`s type:')
                # if dict['Type'] == 'Film':
                #     dict['Genre'] == input('Enter movie genre:')
                # elif dict['Type'] == 'Series':
                #     dict['numbOfSeasons'] == input('Enter number of seasons:')
                # elif dict['Type'] == 'Documentary':
                #     dict['Location'] == input('Enter documentary location:')
                # elif dict['Type'] == 'Clip':
                #     dict['Inhr'] == None
                # result = Dict2Class(dict) 
                
                Media_list[i].ID = " " + input('Enter ID:')
                Media_list[i].name = " " + input('Enter media name:')
                Media_list[i].director = " " + input('Enter director name:')
                Media_list[i].IMDB_score = " " + input('Enter IMDB score:')
                Media_list[i].url = " " + input('Enter url:')
                Media_list[i].duration = " " + input('Enter duration:')
                Media_list[i].cast = " " + input('Enter cast name:')
                Media_list[i].year = " " + input('Enter media type:')
                if type(Media_list[i]).__name__ ==  'Film':
                    Media_list[i].genre == " " + input('Enter movie genre:')
                    # Media_list.append(Film(Media_add[0], Media_add[1], Media_add[2], Media_add[3], Media_add[4], Media_add[5], Media_add[6], Media_add[7], int(Media_add[8][2:6]), Media_add[9]))

                elif type(Media_list[i]).__name__ == ' Series':
                    Media_list[i].name == " " + input('Enter number of seasons:')
                    # Media_list.append(Series(Media_add[0], Media_add[1], Media_add[2], Media_add[3], Media_add[4], Media_add[5], Media_add[6], Media_add[7], int(Media_add[8][2:6]), Media_add[9]))

                elif type(Media_list[i]).__name__ == ' Documentary':
                    Media_list[i].name == " " + input('Enter documentary location:')
                    # Media_list.append(Documentary(Media_add[0], Media_add[1], Media_add[2], Media_add[3], Media_add[4], Media_add[5], Media_add[6], Media_add[7], int(Media_add[8][2:6]), Media_add[9]))

                elif type(Media_list[i]).__name__ == ' Clip':
                    Media_list[i].name == " " + input('Enter clip extension:')
                    # Media_list.append(Clip(Media_add[0], Media_add[1], Media_add[2], Media_add[3], Media_add[4], Media_add[5], Media_add[6], Media_add[7], int(Media_add[8][2:6]), Media_add[9]))
        # continue
        



                # myFile = open('database.txt','w+')
                # k = len(Media_list)
                # for i in range(k-1):
                #     myFile.write(Media_list[i]['ID'] + ',' + Media_list[i]['Name'] + ',' + Media_list[i]['Director'] + ',' + Media_list[i]['IMDB_score']+ ',' + Media_list[i]['Duration'] + ',' + Media_list[i]['Cast'] + ',' + Media_list[i]['Type'] + ',' + Media_list[i]['Url'] + '\n')
                # myFile.write(Media_list[k-1]['ID'] + ',' + Media_list[k-1]['Name'] + ',' + Media_list[k-1]['Director'] + ',' + Media_list[k-1]['IMDB_score']+ ',' + Media_list[k-1]['Duration'] + ',' + Media_list[k-1]['Cast'] + ',' + Media_list[k-1]['Type'] + ',' + Media_list[k-1]['Url'])
                # myFile.close()
def delete_media():
    Media_list2 = []
    oldName = input('Enter product name you want to delete:')
    # for i in range(len(Media_list)):
    #     if Media_list[i]['Name'] != ' ' + Name:
    #         Media_list2.append(Media_list[i])
    for i in range(len(Media_list)):
        if Media_list[i].name == " '" + oldName + "'":
            Media_list.remove(Media_list[i])
            break
        else:
            print('Name not found.')
    # Media_list = []
    # Media_list = Media_list2
    # myFile = open('database.txt', 'w+')
    # for i in range(len(Media_list2)):
        # myFile.write(Media_list2[i]['ID'] + ',' + Media_list2[i]['Name'] + ',' + Media_list2[i]['Director'] + ',' + Media_list2[i]['IMDB_score']+ ',' + Media_list2[i]['Duration'] + ',' + Media_list2[i]['Cast'] + ',' + Media_list2[i]['Type'] + ',' + Media_list2[i]['Url'])
    #     if i == len(Media_list2)-1:
    #         print()
    #     else:
    #         myFile.write('\n')
    # myFile.close()
def search():
    oldName = input('Enter media name you want to find:')
    for i in range(len(Media_list)):
        if Media_list[i].name == " '" + oldName + "'":
            print(f'ID:\t{Media_list[i].ID}'+ '\n'
                + f'Name:\t{Media_list[i].name}\n'+
                  f'Director`s name:\t{Media_list[i].director}\n'+ 
                  f'IMDB_score:\t{Media_list[i].IMDB_score}\n'+ 
                  f'Url:\t{Media_list[i].url}\n'+
                  f'Duration:\t{Media_list[i].duration}\n'+ 
                  f'Cast:\t{Media_list[i].cast}\n'+ 
                  f'Year:\t{Media_list[i].year}\n')
            if type(Media_list[i]).__name__ == ' Film':
                print(f'Genre:\t{Media_list[i].genre}\n')
            elif type(Media_list[i]).__name__ == ' Series':
                print(f'Number of seasons:\t{Media_list[i].numberOfSeasons}\n')
            elif type(Media_list[i]).__name__ == ' Documentary':
                print(f'Location:\t{Media_list[i].location}\n')
            elif type(Media_list[i]).__name__ == ' Clip':
                print(f'Format:\t{Media_list[i].format}\n')


        else:
            print('Name not found.')

def show_list():
    # print('Loading...')
    # myFile = open('database.txt', 'r')
    # data = myFile.read() 
    # media_list = data.split('\n')
    # for i in range(len(media_list)):
    #     dict = {}
    #     media_info = media_list[i].split(',')
    #     dict['ID'] = media_info[0]
    #     dict['Name'] = media_info[1]
    #     dict['Director'] = media_info[2]
    #     dict['IMDB_score'] = media_info[3]
    #     dict['Url'] = 
    #     dict['Duration'] = media_info[4]
    #     dict['Cast'] = media_info[5]
    #     dict['Type'] = media_info[6]
    #     dict['Url'] = media_info[7]

    #             dict['Url'] = ' ' + input('Enter Media`s url:')
    #             dict['Duration'] = ' ' + input('Enter media`s Duration:')
    #             dict['Cast'] = ' ' + input('Enter Actor`s name:')
    #             dict['Type'] = ' ' + input('Enter Media`s type:')
    #             if dict['Type'] == 'Film':
    #                 dict['Genre'] == input('Enter movie genre:')
    #             elif dict['Type'] == 'Series':
    #                 dict['numbOfSeasons'] == input('Enter number of seasons:')
    #             elif dict['Type'] == 'Documentary':
    #                 dict['Location'] == input('Enter documentary location:')
    #             elif dict['Type'] == 'Clip':
    #                 dict['Inhr'] == None
    #             Media_list.append(dict)

    #     Media_list.append(dict)
    # print(data)
    # myFile.close()
    for i in range(len(Media_list)):
        print(f'ID:\t{Media_list[i].ID}'+ '\n'
                + f'Name:\t{Media_list[i].name}\n'+
                  f'Director`s name:\t{Media_list[i].director}\n'+ 
                  f'IMDB_score:\t{Media_list[i].IMDB_score}\n'+ 
                  f'Url:\t{Media_list[i].url}\n'+
                  f'Duration:\t{Media_list[i].duration}\n'+ 
                  f'Cast:\t{Media_list[i].cast}\n'+ 
                  f'Year:\t{Media_list[i].year}\n')
        if type(Media_list[i]).__name__ == ' Film':
            print(f'Genre:\t{Media_list[i].genre}\n')
        elif type(Media_list[i]).__name__ == ' Series':
            print(f'Number of seasons:\t{Media_list[i].numberOfSeasons}\n')
        elif type(Media_list[i]).__name__ == ' Documentary':
            print(f'Location:\t{Media_list[i].location}\n')
        elif type(Media_list[i]).__name__ == ' Clip':
            print(f'Format:\t{Media_list[i].format}\n')



def duration(Z):
    dur = (int(Z[0])*60)+int(Z[2]+Z[3])
    return dur
def duration2(Y):
    dur = (int(Y[1])*60)+int(Y[3]+Y[4])
    return dur

def duration3(W):
    dur = (int(W[2])*60)+int(W[4]+W[5])
    return dur

def advanced_search():
    A = input("Enter timeframe A in format h:mm:")
    B = input("Enter timeframe A in format h:mm:")
    upper = max(duration(A), duration(B))
    lower = min(duration(A), duration(B))

    # for i in range(len(Media_list)):
    #     if duration2(Media_list[i]['Duration']) >= lower and duration2(Media_list[i]['Duration']) <= upper:
    #         print(Media_list[i].values())


    for i in range(len(Media_list)):
        if duration3(Media_list[i].duration) >= lower and duration3(Media_list[i].duration) <= upper:
            print(f'ID:\t{Media_list[i].ID}'+ '\n'
                + f'Name:\t{Media_list[i].name}\n'+
                  f'Director`s name:\t{Media_list[i].director}\n'+ 
                  f'IMDB_score:\t{Media_list[i].IMDB_score}\n'+ 
                  f'Url:\t{Media_list[i].url}\n'+
                  f'Duration:\t{Media_list[i].duration}\n'+ 
                  f'Cast:\t{Media_list[i].cast}\n'+ 
                  f'Year:\t{Media_list[i].year}\n')
            if type(Media_list[i]).__name__ == ' Film':
                print(f'Genre:\t{Media_list[i].genre}\n')
            elif type(Media_list[i]).__name__ == ' Series':
                print(f'Number of seasons:\t{Media_list[i].numberOfSeasons}\n')
            elif type(Media_list[i]).__name__ == ' Documentary':
                print(f'Location:\t{Media_list[i].location}\n')
            elif type(Media_list[i]).__name__ == ' Clip':
                print(f'Format:\t{Media_list[i].format}\n')


def download(self):
    oldName = input('Enter media name you want to download:')
    for i in range(len(Media_list)):
        if Media_list[i].name == " '" + oldName + "'":
            first_stream = pytube.YouTube(Media_list[i].url).streams.first()
            first_stream.download(output_path = './', filename = f"{Media_list[i].name}.mp4")
            continue

def exit():

    myFile = open('database.txt','w+')
    k = len(Media_list)
    for i in range(k-1):
        myFile.write(Media_list[i].ID + ',' + Media_list[i].name + ',' + Media_list[i].director + ',' + Media_list[i].IMDB_score + ',' + Media_list[i].url + ',' + Media_list[i].duration + ',' + Media_list[i].cast + ', ' + "'" + str(type(Media_list[i]).__name__) + "'" + ',' + Media_list[i].year + ',' )
        if type(Media_list[i]).__name__ == 'Film':
            myFile.write(Media_list[i].genre + '\n')
        elif type(Media_list[i]).__name__ == 'Series':
            myFile.write(Media_list[i].numberOfSeasons + '\n')
        elif type(Media_list[i]).__name__ == 'Documentary':
            myFile.write(Media_list[i].location + '\n')
        elif type(Media_list[i]).__name__ == 'Clip':
            myFile.write(Media_list[i].format + '\n')



    myFile.write(Media_list[k-1].ID + ',' + Media_list[k-1].name + ',' + Media_list[k-1].director + ',' + Media_list[k-1].IMDB_score+ ',' + Media_list[k-1].url + ',' + Media_list[k-1].duration + ',' + Media_list[k-1].cast + ', ' + "'" + str(type(Media_list[k-1]).__name__) + "'" + ',' + Media_list[i].year + ','  )
    if type(Media_list[k-1]).__name__ == 'Film':
        myFile.write(Media_list[i].genre)
    elif type(Media_list[k-1]).__name__ == 'Series':
        myFile.write(Media_list[k-1].numberOfSeasons)
    elif type(Media_list[i]).__name__ == 'Documentary':
        myFile.write(Media_list[k-1].location)
    elif type(Media_list[k-1]).__name__ == 'Clip':
        myFile.write(Media_list[k-1].format)

    myFile.close()









    quit()


load()
show_menu()
while(True):
    choice = int(input('Please choose a number:'))
    if choice == 1:
        add_media()
        show_menu()
    elif choice == 2:
        edit_media()
        show_menu()
    elif choice == 3:
        delete_media()
        show_menu()
    elif choice == 4:
        search()
        show_menu()
    elif choice == 5:
        show_list()
        show_menu()
    elif choice ==6:
        download()
        show_menu()
    elif choice ==7:
        advanced_search()
        show_menu()
    elif choice ==8:
        exit()