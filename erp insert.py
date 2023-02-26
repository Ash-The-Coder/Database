import sqlite3

erpdtb = sqlite3.connect('erp.db')
erpdtb.execute('''CREATE TABLE attd 
    (
    sub VARCHAR(10),
    date INT,
    day INT,
    year INT,
    state VARCHAR(1)
    )
    ''')

data = erpdtb.cursor()


data.execute('''INSERT INTO attd VALUES ('cc',02,02,2023,'p')''')
data.execute('''INSERT INTO attd VALUES ('daa',02,02,2023,'p')''')
data.execute('''INSERT INTO attd VALUES ('app',02,02,2023,'p')''')
data.execute('''INSERT INTO attd VALUES ('os',02,02,2023,'a')''')
data.execute('''INSERT INTO attd VALUES ('evs',02,02,2023,'p')''')
data.execute('''INSERT INTO attd VALUES ('se',02,02,2023,'p')''')
data.execute('''INSERT INTO attd VALUES ('sepm',02,02,2023,'p')''')
data.execute('''INSERT INTO attd VALUES ('cc',03,02,2023,'a')''')
data.execute('''INSERT INTO attd VALUES ('daa',03,02,2023,'p')''')
data.execute('''INSERT INTO attd VALUES ('app',03,02,2023,'p')''')
data.execute('''INSERT INTO attd VALUES ('os',03,02,2023,'a')''')
data.execute('''INSERT INTO attd VALUES ('evs',03,02,2023,'p')''')
data.execute('''INSERT INTO attd VALUES ('se',03,02,2023,'p')''')
data.execute('''INSERT INTO attd VALUES ('sepm',03,02,2023,'a')''')

erpdtb.commit()
erpdtb.close()



