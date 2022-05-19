password = input('Password: ')

if password == 'jadeisthebest':
    print('You have logged in successfully!')

# An 'if' statement has the following
# The if Keyword
# The body of code
# The condition

name = input("What is your name?")
is_admin = name == 'admin'

password = input("What is your password?")
is_password_correct = password == 'jadeisthebest'

if is_admin and is_password_correct:
    print('Welcome, Admin!')

if not is_admin or is_password_correct:
    print("Log in unsuccessful")