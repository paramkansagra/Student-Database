import _sqlite3


def add(file_name):
    print('add module')
    con = _sqlite3.connect(file_name + '.db')
    csr = con.cursor()
    a = 'create table ' + file_name
    b = '''(
    roll_no decimal(20) unique,
    name char(20)); '''
    a += b
    csr.execute(a)
    x = int(input('input the no of entries'))
    for i in range(x):
        a = int(input('input the roll no'))
        b = str(input('input the name'))
        x = (a, b)
        b = 'insert into ' + file_name + ' values' + str(x) + ';'
        csr.execute(b)
    a = 'select * from ' + file_name
    csr.execute(a)
    a = csr.fetchall()
    print(a)
    con.commit()
    con.close()


def add_new(file_name):
    print('add new module')
    file_name = file_name.rstrip(';')
    con = _sqlite3.connect(file_name + '.db')
    csr = con.cursor()
    csr.execute("PRAGMA table_info" + '(' + file_name + ');')
    x = csr.fetchall()
    header = []
    for i in x:
        count = 0
        for j in i:
            if (count == 1):
                header.append(j)
            else:
                pass
            count += 1
    print(header)
    a = 'select * from ' + file_name + ';'
    csr.execute(a)
    a = csr.fetchall()
    roll_no = []
    for i in a:
        roll_no.append(i[0])
    print('adding new coulmns')
    c = str(input('input the name of new marks to be entered without space'))
    c = c.upper()
    b = 'alter table ' + file_name + ' add ' + c + ' decimal(5);'
    csr.execute(b)
    a = 'select * from ' + file_name + ';'
    csr.execute(a)
    a = csr.fetchall()
    for i in roll_no:
        x = int(input('input the marks in ' + c + ' of ' + str(i)))
        b = 'update ' + file_name + ' set ' + c + '=' + str(x) + ' where roll_no=' + "'" + str(i) + "'" + ';'
        print(b)
        csr.execute(b)
    a = 'select * from ' + file_name + ';'
    csr.execute(a)
    a = csr.fetchall()
    print(a)
    con.commit()
    con.close()
