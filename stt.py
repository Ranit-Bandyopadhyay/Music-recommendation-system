                                                   # LOGIN PAGE
'''                                WELCOME TO THE MUSIC RECOMMENDATION SYSTEM. ENTER A MUSIC AND GET SIMILAR RECOMMENDATIONS
                                                SO LET'S GO!!!!!!!!!!!!  
                                                        '''

print('                                         WELCOME TO MUSIC RECOMMENDATION SYSTEM                                           ')
print('---------------------------------------------------------------------------------------------------------------------------')



password = []
username = []
i = 0


def enter_info(x):
    global i
    y = x.split(' ')
    password.append(y[-1])
    username.append(y[0])
    for i in range(len(password)):
        for j in range(i + 1, len(password)):
            if (password[i] == password[j]):
                try:
                    while (password[i] == password[j]):
                        print('enter again, same password')
                        password.remove(password[i])
                        password.append(input('password'))
                        if (password[i] != password[j]):
                            break
                        i += 1
                except IndexError:
                    print('logged out!')
                    print('choose another password or your info can be stolen')
                    return;

        print('logged in as {}!'.format(y[0]))
        return ;


t = int(input('enter number of users'))
for i in range(t):
    enter_info(input('username and password with a space'))

print()

def reveal_info():

    for i in range(t):
        for j in range(i + 1, t):
            if (password[i] == password[j]):
                password.remove(password[j])
                print('yes')
    print('-' * 46)
    print('Username          |password')
    print('-' * 46)
    for i, j in zip(username, password):
        print(i + ' '*(18-len(i)) + '|' + j)
        print('-' * 46)



#reveal_info()