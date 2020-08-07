import sqlite3 as sql
from os import system
name_db = sql.connect('customer.db')
write_db = name_db.cursor()
system('cls')
while True:
    try:
        mode = input('[0].make Table\n[1].write Table\n[2].selcet Table\nType \'exit\' for exit program\n')
        if mode == 'exit':
            print('exit ./.\./')
            system('cls')
            break
        mode = int(mode)
        if mode == 0:
            write_db.execute("""CREATE TABLE customer (last_name None, frist_name None, email None)""")
            system('cls')
            print('create success')
            print('- ' * 10)
        elif mode == 1:
            last_name = input('send last name client ')
            frist_name = input('send frist name client ')
            email = input('send email client ')
            data = (last_name,frist_name,email)
            write_db.execute(f"INSERT INTO customer VALUES {data}")
            system('cls')
            print('edit success')
            print('- ' * 10)
        elif mode == 2:
            write_db.execute("SELECT * FROM customer")
            system('cls')
            for iteam in write_db.fetchall():
                  print('- ' * 10)
                  print(f'first name: {iteam[0]}\nlast name: {iteam[1]}\nemail: {iteam[2]}')
            print('selcet success\n' + '- ' * 10)
        else:
            system('cls')
            print('not found optoins')
    except Exception as erro:
        system('cls')
        print('debug {0}'.format(erro))
        continue
    
name_db.commit()
name_db.close()
print('save settings')