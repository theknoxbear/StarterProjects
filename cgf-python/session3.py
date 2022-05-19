today = input ("What day is it?")
is_monday = today == "Monday"
print('Today is Monday: {}'.format(is_monday))

#== Equal to
#!= Not equal
#> Greater than
#< Less than
#>= Greater than or equal to
#<= Less than or equal to

# Float() can convert strings to decimals

temperature = input('What is the temperature?')
is_freezing = float(temperature) <= 0.0
print('The temperature is freezing: {}'.format(is_freezing))

# .format is a way for us to plug in a variable to a string

price = input('How much is the burger?')
within_budget = float(price) <= 10.00
vegetarian = input('Is the restaurant vegetarian?')

is_vegetarian = vegetarian == 'yes'
should_buy_burger = within_budget and is_vegetarian
print('Should I buy the burger?: {}'.format(should_buy_burger))

# and - both expressions are True
# or - at least one expression is True
# not - reverse the expression (True becomes False, and vice-versa)

mars_choice = input('Would you like to live on Mars? y/n')
is_willing = mars_choice == 'y'

affordable = input('Can you afford to visit Mars? y/n')
can_afford = affordable == 'y'

should_visit_mars = is_willing and can_afford

print('You should visit Mars: {}'.format(should_visit_mars))

