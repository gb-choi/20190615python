

'''
money = True
if money:
    print("택시를 타고가라")
else:
    print("걸어 가라")

'''

'''
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")
'''


'''
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

'''
'''
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어가라")
'''


a = "Life is too short, you need python"
if 'wife' in a:
    print("wife")
elif 'python' in a and 'you' not in a:
    print("python")
elif 'shirt' not in a:
    print("shirt")
elif 'need' in a:
    print("need")
else:
    print("none")
    