import sqlite3
import os 


PATH = os.path.abspath(__file__+'/..')

connect = sqlite3.connect(PATH + '/db.sqlite3')
cursor = connect.cursor()

# name = str(input("Enter name of workers :"))
# salary = int(input("Enter salary :"))
# posada = str(input("Enter posada of workers :"))
# koficeint = int(input("Enter koficient of workers :"))


create_table = '''CREATE TABLE workers(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name CHAR(255),
salary INTEGER,
posada CHAR(255),
koficeint INTEGER
);
'''
#cursor.execute(create_table)

# def add_staff():
#     create_workers = f'''INSERT INTO workers(name, salary, posada,koficeint)
#     VALUES("{name}",{salary},"{posada}",{koficeint});
#     '''

#     cursor.execute(create_workers)
#     connect.commit()
# add_staff()
# def get_by_id():
#     enter_id = input("Enter id of workers")
#     find_workers_by_id = f'''SELECT name,posada,salary,koficeint FROM workers WHERE id = {enter_id}
#     '''
#     connect.commit()
#     result = cursor.execute(find_workers_by_id)
#     result = result.fetchall()
#     print(result)
# get_by_id()




# def delte_worker():
#     enter_id = input("Enter id of worker")
#     del_worker_by_id = f'''DELETE FROM workers WHERE id <= {enter_id}
#     '''
   
#     result = cursor.execute(del_worker_by_id)
#     connect.commit()
#     result = result.fetchone()
#     print("Done")
# delte_worker()    



# def get_best_staff():
#     take_best_kofi = f'''SELECT name,posada,salary,koficeint FROM workers WHERE koficeint > {50}
#     '''
#     connect.commit()
#     result = cursor.execute(take_best_kofi)
#     result = cursor.fetchall()
#     print(result)
# get_best_staff()

# def add_bonus():
#     plus_bonus = f'''SELECT salary FROM workers WHERE koficeint >{50}
#     '''
#     connect.commit()
#     result = str(cursor.execute(plus_bonus))
#     result = str(cursor.fetchall())
#     add = result *0,2
#     add +=result
    
#     add_workers = f'''INSERT INTO workers(salary)
#     VALUES({add});
#      '''

# add_bonus()