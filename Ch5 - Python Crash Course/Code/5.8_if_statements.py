# if statements
# Overcommented for explanatory reasons

# Check if a number is above threshold
number = int(input('Insert a high enough number'))
# Note the int conversion

if number > 10:
    print('Ok, your number is big enough')

# Same case, but adding an 'else' which revelas the threshold
number = int(input('Insert a high enough number'))
# Note the int conversion

if number > 10:
    print('Ok, your number is big enough')
else:
    print('Sorry, it has to be more than 10')
    
# Using elif
# Another silly game elif make tiers of ambition possible
number = int(input('Measure your ambition. Enter a number'))

if number <0:
    print('How modest')
elif 0 < number < 10:
    print('Not too much')
elif 11 < number < 100:
    print('Wooo')
elif 101 < number < 9000:
    print('Gulp')
elif number > 9000:
    print('Over 9000!')
# Did we cover all the outcomes? Nope!
else:
    print('case not considered')
