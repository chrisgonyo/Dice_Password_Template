#Dice Password Template

import pandas as pd
import numpy as np
import secrets


#Welcome Users

greeting = "****EDUCATIONAL PURPOSES ONLY**** see README.md\n"
greeting += "\nWelcome to Dice Pass Template!\n"

greeting += "\n\nGrab some dice and let's create your password template.\n"
greeting += "(Enter 'q' to quit at anytime.)\n"


print(greeting)

#Prompt for user input and store values
dice_sides_user_input = ()
dice_number_user_input = ()

#Die sides user prompt
user_prompt = True
while user_prompt:

    active = True
    while active:
        try:
            dice_sides_input = input("\nEnter the number of sides per die: ")
            if dice_sides_input == 'q' or dice_sides_input == 'Q':
                exit()

            else:
                dice_sides_result = int(dice_sides_input)
                dice_sides_user_input = dice_sides_result
                if dice_sides_user_input > 1 and dice_sides_user_input < 21:
                    break
                else:
                    print("Whoops, please use a dice that has between 2 and 20 sides.")
        except ValueError:
            print("Whoops, please only use numbers. Letters don't work here.")


#Number of dice to roll user prompt
    active = True
    while active:
        try:
            total_dice_used = input("\nEnter the number of dice you will roll at once: ")
            if total_dice_used == 'q' or dice_sides_input == 'Q':
                exit()
            total_dice_result = int(total_dice_used)
            dice_number_user_input = total_dice_result
            if dice_number_user_input > 1 and dice_number_user_input < 21:
                break
            else:
                print("Whoops, please use at least two dice and less than 21 dice.")
        except ValueError:
            print("Whoops, please only use numbers. Letters don't work here.")


#Repeat back number of dice and number of dice sides
    dice_used_message = "\nPlease confirm the following values: \n"
    dice_used_message += "Sides per die: " + str(dice_sides_user_input)
    dice_used_message += "\nTotal dice per roll: " + str(dice_number_user_input)

    print(dice_used_message)
#Confirm user input and exit user_prompt loop
    dice_used_confirm_message = "\nIs this correct (y/n): "
    confirmation = input(dice_used_confirm_message)
    if confirmation == 'y' or confirmation == 'Y':
        user_prompt = False
    if confirmation == 'q' or confirmation == 'Q':
        exit()


print("\nExcellent - Here is your first template: \n")

#60 available password characters selected for handwritten legibility
pass_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'd', 'e', 'g', 'h', 'i', 'j', 'q', 'r', 't', '0', '1', '2',
    '3', '4', '5', '6', '7', '8', '9', '~', '!', '#', '%', '&', '*', '+',
    '=', '-', '[', ']', '?', '@', '$' ]

character_list_length = len(pass_characters)

####Store list of dice sides
sides = [i + 1 for i in range(0, dice_sides_user_input)]


#Store list of total dice
dice = [i + 1 for i in range(0, dice_number_user_input)]

#convert dice list values to a string and add Die label
str_dice = ["Die " + str(i) + ":" for i in dice]


#Store list of password characters
pass_values = []

#Store total dice rolled value
total_dice_count = 0
increment_dice_count = 0


#Create a class to assign random characters from pass_characters to a list.
#Format list length based number of sides
#Nest lists based on number of dice per roll

class TempValuesLoop():
    def __init__(self, sides, dice):
        self.sides = sides
        self.dice = dice

###append random character from pass_character to list
###stop loop when total random characters == number of sides per dice
    def single_list(self):
        temp_values_loop_results = []
        single_list_countup = 0

        active = True
        while active:
            if single_list_countup == self.sides:
                single_list_countup = 0
                active = False
            else:
                single_list_countup += 1
                temp_character = secrets.choice(pass_characters)
                temp_values_loop_results.append(temp_character)

        pass_values.append(temp_values_loop_results)

###Nest lists based on number of dice rolled
    def multiple_lists(self):
        total_list_countup = 0

        active = True
        while active:
            if total_list_countup == self.dice:
                active = False
            else:
                total_list_countup +=1
                self.single_list()


###Loop through password character and assign random character to DataFrame
#Calculate Password length, Entropy and Brute-Force cost

active = True
while active:
        pass_values = []
        temp_values = TempValuesLoop(dice_sides_user_input, dice_number_user_input)
        temp_values.multiple_lists()
        increment_dice_count = dice_number_user_input
        total_dice_count += increment_dice_count

        # set DataFrame title
        title = "Dice Value"
        title_center = title.center(((dice_sides_user_input * 3) + 5), ' ')

        #Create Dataframe
        df1 = pd.DataFrame(pass_values,
                    columns=sides, index=str_dice,)
        print(title_center)
        print(df1)

        #Calculate entropy
        entropy = np.log2(character_list_length) * total_dice_count
        print("\nPassword Length: " + str(total_dice_count))
        print("Current Entropy: " + str('%.2f'%entropy))

        #Calculate brute-force cost
        #MH/s Hash rate benchmark running Hashcat on AWS g4dn.xlarge
        #https://www.javydekoning.com/hashcat-performance-aws-ec2/
        hash_rates = {
            'SHA256': 3099.2,
            'MD5': 20625.3,
            'NTLM': 36730.7,
        }
        #Approx cost to run Hashcat brute-force application on AWS g4dn.xlarge
        cost_per_hour = 8.61

        #Calculate and print cost
        cost_message = 'Approx cost to brute-force using Hashcat on '
        cost_message += 'AWS by intercepted hash type:'
        print(cost_message)

        for k, v in hash_rates.items():
            #convert MH/s to hashes per hour
            v = v * 1000000 * 60 * 60

            #hours to exhaust all guesses
            #divide by 2 assumes hash will be found after 50%
            #multiply by AWS cost per hour
            v = ((2**entropy/v) / 2) * cost_per_hour
            #format with commas and round to two decimal places
            f_v = "{:,.2f}".format(v)
            if v < .01:
                print("\t" + k + ':', '< $0.01')
            else:
                print("\t" + k + ':', '$' + f_v)
#            print("\t" + k + ':', '$' + '%.2f'%v)
        #Prompt user to roll again to add length to password
        message = "\nWould you like to roll again? y/n: "
        roll_again_prompt = input(message)
        print("\n")

    #    print(roll_again_prompt)

        if roll_again_prompt == 'n' or roll_again_prompt == 'q':
            break
