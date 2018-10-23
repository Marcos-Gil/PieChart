# Importing the required libraries to be able to draw the Pie Graph
import matplotlib.pyplot as plt
from matplotlib.pyplot import pie
from matplotlib.pyplot import axes
from matplotlib.pyplot import show
from matplotlib.pyplot import title
from matplotlib.pyplot import figure

# Intro formatting for user
print('=====================')
print(' Chart Creator Menu  ')
print('=====================')

# Asking user for required inputs to begin
whatTitle = input('Enter a title for the chart: ')
legendOrLabel = int(input('Choose 1) A Legend, or 2) Sector Labels? '))

# Making sure the user can only enter 1 or 2 to decide it the Pie Graph has a legend or it's labelled
while legendOrLabel != 1 and legendOrLabel != 2:
	print('Sorry, you can only enter 1 or 2.')
	legendOrLabel = int(input('Choose 1) A Legend, or 2) Sector Labels? '))

# Rest of required inputs
numSectors = int(input('Enter the number of sectors: '))
sectorTotal = int(input('Enter the total: '))

# Setting up the type of Pie Graph and it's dimenions
figure(1, figsize=(8,8))
ax = axes([.1, .1, 0.8, 0.8])

# Creating labels and percentages(fracs) as lists so values can be added to them with append
labels = []
fracs = []

# For loop repeating for the amount of Sectors the user inputs. Gets the label for each sector and
# the sectors value, then appends them to the labels/fracs lists. Also includes a check to make sure
# that frac is an integer
for z in range(1, numSectors+1):
    label = input('\nEnter the label for sector {z}: '.format(z=z))
    labels.append(label)
    frac = input('Enter the value for the {label} sector: '.format(label=label))
    while not frac.isdigit():
        print('Sorry, this can only be an integer.')
        frac = input('Enter the value for the {label} sector: '.format(label=label))
    frac = int(frac)
    fracs.append(frac)

# After the user enters the values above, if the provided percentages do not add up to equal the amount
# specified by the user at the start of the program, it prints a message letting them now that this
# is the case and now reprompts them to re-enter the Pie Graph info until it adds up properly
while sectorTotal != sum(fracs):
    labels = []
    fracs = []
    print('Sorry, the sector values entered did not amount to your specified total. Please try again. ')
    for z in range(1, numSectors+1):
        label = input('\nEnter the label for sector {z}: '.format(z=z))
        labels.append(label)
        frac = input('Enter the value for the {label} sector: '.format(label=label))
        while not frac.isdigit():
            print('Sorry, this can only be an integer.')
            frac = input('Enter the value for the {label} sector: '.format(label=label))
        frac = int(frac)
        fracs.append(frac)

# Custom message letting the user know the Pie Graph will now be drawn
print("\nYour custom graph will now be drawn.")

# If/Elif loop to draw will decide in the graph is labelled or using a legend based on what the user entered earlier
if legendOrLabel == 1:
	pie(fracs, autopct='%1.1f%%', shadow=True, startangle=90)
	plt.legend(labels, loc = "lower right")
elif legendOrLabel == 2:
	pie(fracs, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

# Functions to draw and label the Pie Graph
title(whatTitle, bbox={'facecolor':'0.8', 'pad':5})
show()
