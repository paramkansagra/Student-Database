import _sqlite3


def modify(file_name):
    print('modify module')
    con = _sqlite3.connect(file_name + '.db')
    csr = con.cursor()
    a = 'select * from ' + file_name + ';'
    csr.execute(a)
    a = csr.fetchall()
    csr.execute("PRAGMA table_info" + '(' + file_name + ');')
    x = csr.fetchall()
    test_name = []
    roll_no = []
    for i in a: #making roll no list
        roll_no.append(i[0])
    for i in x: #making test name list
        test_name.append(i[1])
    for i in a: # print name and values
        count = 0
        for j in i:
            print(x[count][1],end='=')
            print(j,end='   ')
            count += 1
        print()
    flag = True
    while(flag == True):
        print()
        roll = int(input('input the roll no'))
        test = str(input('input name of test without spaces'))
        test = test.upper()
        if((roll not in roll_no) or (test not in test_name)):
            print('wrong input')
            a = str(input('do you want to modify more? (y/n)'))
            a = a.lower()
            if(a == 'y'):
                flag = True
            else:
                flag = False
                print('module modify end ')
        else:
            print('roll no = ',roll)
            new = int(input('input the new marks of ' + str(test) + ' for ' + str(roll)+' '))
            a = 'update ' + file_name + ' set ' + test + '=' + str(new) + ' where roll_no=' + str(roll) + ';'
            csr.execute(a)
            a = 'select * from ' + file_name + ';'
            csr.execute(a)
            print(csr.fetchall())
            print()
            a = str(input('do you want to modify more? (y/n)'))
            a = a.lower()
            if (a == 'y'):
                flag = True
            else:
                flag = False
                print('module modify end ')
        a = 'select * from ' + file_name + ';'
        csr.execute(a)
        a = csr.fetchall()
        csr.execute("PRAGMA table_info" + '(' + file_name + ');')
        x = csr.fetchall()
        for i in a:  # print name and values
            count = 0
            for j in i:
                print(x[count][1], end='=')
                print(j, end='   ')
                count += 1
            print()
    con.commit()
    con.close()