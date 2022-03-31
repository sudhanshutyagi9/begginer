username = input("enter your username :")
password = input("create your password :")
password_len = len(password)
code = '*' * password_len
print(
    f'username: {username} \n password: {code} \n your password is {password_len} length long'
)
