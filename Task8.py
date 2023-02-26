def read_base():
    base = open('base.txt,' 'r', encoding='utf-8')
    base_list = base.read()
    base.close()
    print(base_list)
    return base_list

def search_base():
    base = open('base.txt,' 'r', encoding='utf-8')
    list_of_base = base.read().split('\n')
    base.close()
    for i in range(len(list_of_base)):
       list_of_base[i] =  list_of_base[i].split(' ')
       data = str(input('Введите данные для поиска: '))
       data_check = False
       for i in range(len(list_of_base)):
           for j in list_of_base[i]:
               if str(data).lower() == j.lower():
                   data = list_of_base[i]
                   data_check = True
    if data_check: print(f'Нашлись следующие данные {data}') 
    else: print('Данные не найдены') 
    
def update_base():
    base = open('base.txt,' 'r', encoding='utf-8') 
    new_data = input('Введите данные нового сотрудника: ')   
    base.write(f'{new_data}' + str('\n')) 
    base.close()
    
def edit_base():
    print('Редактирование данных: ') 
    
def delit_base():
    print('Удаление данных: ')  
    
def intro_text():
    print('Меню: ')  
    print('1 Вывести команды , 2 Найти контакты')  
    print('3 Добавить сотрудника, 4 Изменить данные сотрудника' ) 
    print('5 Удалить сотрудника ')
    
def menu(command): 
    match command:
        case 1:
            read_base()
        case 2:
            search_base()
        case 3:
             update_base()
           
        case 4: 
              edit_base() 
        case 5:
            delit_base()
        case _:
            os.system('clear')   
            print('Выберите вариант из меню: ')
            intro_text()
            menu(int(input('Выберите действие: ')))
base_list = ()
intro_text()
menu(int(input('Выберите действие: ')))             
            
                   
                          
                   
