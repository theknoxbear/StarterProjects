password = input('password: ')
if password == 'jadeisthebest':
    print("Welcome")
else:
    print("Incorrect")

# Elif statements mean else or if. They are used after if statements to check whether another condition is
# True or False

dog_size = int(input('How big is the dog?'))

if 75 < dog_size:
    print("That's a big boi")

elif dog_size <25:
    print('That is a smol pupper')

else:
    print("That's a very average doggo")

temperature = int(input('How hot is the oven?'))
if temperature > 200:
    print("Oven is too hot")

elif temperature < 150:
    print('Oven is too cold')

elif temperature == 180:
    print('Oven is just right')

else:
    print('The temperature is close enough')