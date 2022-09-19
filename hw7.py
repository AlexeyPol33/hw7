
from operator import itemgetter
from functools import reduce




class File_manager:

    __mods = {'запись':['w','a','+'],'чтение':['r','+'],'иное':['x']}
    def __init__(self, file_name, file_mode = 'r', enc = 'utf-8') -> None:
        self.file_name = file_name
        self.file_mode = file_mode
        self.enc = enc
        mods = reduce(lambda x,y: x + y, self.__mods.values())
        if self.file_mode[0] in mods:
            pass
        else:
            raise IOError ('Мод отсутствует')

    def write (self, text):

        if self.file_mode in self.__mods['запись']:
            pass
        else:
            raise IOError ('Метод только для записи в файл')
        
        with open(self.file_name,self.file_mode,encoding=self.enc) as f:
            f.write(text)

    def readlines (self, lene_number):
        if self.file_mode in self.__mods['чтение']:
            pass
        else:
            raise IOError ('Метод только для записи в файл')
        outline = ''
        with open(self.file_name,self.file_mode,encoding=self.enc) as f:
            try:
                outline = f.readlines()[lene_number]
            except:
                return None
        return outline

        

    def __str__(self) -> str:
        out_text = ''
        with open (self.file_name,'r',encoding=self.enc) as f:
            out_text = f.read()
        return out_text

def create_cookbook (file_name):
    recipfile = File_manager(file_name)
    line_rate = 0
    cook_book = {}
    
    while recipfile.readlines(line_rate) != None:
        recip_name = ''
        recip_values = []

        recip = []

        while (len(recipfile.readlines(line_rate)) != 1) and recipfile.readlines(line_rate) != '\n':
            recip.append(recipfile.readlines(line_rate).rstrip('\n'))
            line_rate += 1
            if recipfile.readlines(line_rate) == None:
                break

        recip_name = recip.pop(0)
        recip.pop(0)
        
        for i in recip:
            i_list = i.split('|')
            recip_values.append({'ingredient_name': i_list[0].strip(), 'quantity': int(i_list[1].strip()), 'measure': i_list[2].strip()})
        
        cook_book.update({recip_name: recip_values})
        line_rate += 1
    return cook_book

def get_shop_list_by_dishes (dishes,person_count,cookboock = create_cookbook('recipes.txt')):

    shop_list = []
    for i in dishes:
        if i in cookboock.keys():
            shop_list += cookboock[i]
        else:
            print('Рецепт не найден')

    shop_list.sort(key = itemgetter('ingredient_name'))
    
    for i in range (len(shop_list)):
        try:
            while shop_list[i]['ingredient_name'] == shop_list[i + 1]['ingredient_name']:
                shop_list[i]['quantity'] = shop_list[i]['quantity'] + shop_list[i + 1]['quantity']
                shop_list.pop(i + 1)
        except:
            pass
        
    for i in range(len(shop_list)):
        shop_list[i]['quantity'] = shop_list[i]['quantity'] * person_count

    shop_dict = {}
    for i in shop_list:
        items = list(i.items())
        shop_dict.update({i['ingredient_name']:{items[2][0]:items[2][1],items[1][0]:items[1][1]}})
    
    return shop_dict

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'],2))
#filetest = File_manager('testfile.txt','r')
#print(filetest.readlines(0))
#print (create_cookbook('recipes.txt'))