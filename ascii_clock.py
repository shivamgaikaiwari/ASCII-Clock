# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Justin Nguyen
# Section: 570
# Assignment: Lab 8.17
# Date: 10/23/25
#

one=[' 1 ','11 ',' 1 ',' 1 ','111']
two =['222','  2','222','2  ','222']
three=['333','  3','333','  3','333']
four =['4 4','4 4','444','  4','  4']
five =['555','5  ','555','  5','555']
six =['666','6  ','666','6 6','666']
seven =['777','  7','  7','  7','  7']
eight =['888','8 8','888','8 8','888']
nine =['999','9 9','999','  9','999']
zero =['000','0 0','0 0','0 0','000']
A = [' A ','A A','AAA','A A','A A']
M = ['M   M','MM MM','M M M','M   M','M   M']
P = ['PPP','P P','PPP','P  ','P  ']
colon = [' ',':',' ',':',' ']

time_dict = {
   '1': one,
   '2': two,
   '3': three,
   '4': four,
   '5': five,
   '6': six,
   '7': seven,
   '8': eight,
   '9': nine,
   '0': zero,
   'A': A,
   'M': M,
   'P': P,
   ':': colon
}

def display_ascii(display, prefChar, ascii):
    for row in range(5):
        line_out = []
        for ch in display:
            if ch == " ":
                cell = "   "
            elif ch == ":":
                cell = ascii[ch][row]
            elif ch in "PAM":
                cell = ascii[ch][row]
            else:
                cell = ascii[ch][row]
                if prefChar:
                    cell = cell.replace(ch, prefChar)
            line_out.append(cell)
        print(" ".join(line_out))

#defines inputs
timeInput = input("Enter the time: ")
clockType = input("Choose the clock type (12 or 24): ")
prefChar = input("Enter your preferred character: ")

#changes 24 hour time to 12 hour time
if clockType == '12':
    timeInput_list = timeInput.split(':')
    timeInput_list_left = int(timeInput_list[0])
    if timeInput_list_left < 12:
        timeInput_list.append("AM")
        if timeInput_list_left == 0:
            timeInput_list_left = 12
    elif timeInput_list_left >= 12:
        timeInput_list.append("PM")
        if timeInput_list_left > 12:
            timeInput_list_left = int(timeInput_list[0]) - 12
    timeInput = f"{str(timeInput_list_left)}:{str(timeInput_list[1])}{str(timeInput_list[2])}" 


#disallows certain characters
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
#efdf
while prefChar not in "abcdeghkmnopqrsuvwxyz@$&*=":
    prefChar = input("Character not permitted! Try again: ")
print ("")
display_ascii(timeInput,prefChar,time_dict)