import add
import modify
import _sqlite3


def edit_marks(class_name):
    print('all info compile module')
    a = class_name[0]
    b = class_name[1]
    b = b.upper()
    file_name = b + '_' + str(a)
    file_name1 = file_name + '.db'
    con = _sqlite3.connect(file_name1)
    csr = con.cursor()
    try:
        a = 'select * from ' + file_name + ';'
        csr.execute(a)
        x = csr.fetchall()
        print(x)
        con.commit()
        con.close()
        a = str(input('input if you want to add(a) or modify(m) values '))
        if (a.lower() == 'a'):
            add.add_new(file_name)
        elif (a.lower() == 'm'):
            modify.modify(file_name)
        else:
            print('wrong input ')
    except:
        file_name = file_name.rstrip(';')
        add.add(file_name)

def intake():
    c = int(input('input the class'))
    s = str(input('input section'))
    s = s.upper()
    f = (c , s)
    return f

a = True
while(a == True):
    x = intake()
    if(x[0]>0 and x[0]<13):
        edit_marks(x)
        a = False
    else:
        print('wrong input')
        a = True