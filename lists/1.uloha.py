def types(list):
    for i in list:
        if type(i)==int or type(i)==float:
            print(i, '- number')
        elif type(i)==str:
            print(i, '- string')
        else:
            print(i, '- other type')

types([12, 'x', None, 3.14, [], range(5), '123'])