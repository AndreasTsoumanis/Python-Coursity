# Ρουλέτα!
import random as rn

while True:
    draw = rn.randint(0,36)
    if draw == 0:
        print("Κληρώθηκε το 0")
    else:
        isSmall = True if draw < 18 else False
        isEven = True if draw%2 == 0 else False
        isRed = True if ((draw<11 or 18<draw<29 )and not isEven or 
                         (10<draw<19 or 28<draw<37)and isEven ) else False
        print('Ο αριθμος που κληρώθηκε είναι ο', draw,'με χαρακτηριστικα:')
        print("Μικρός" if isSmall else "Μεγάλος",
              "Κόκκινος" if isRed else "Μαύρος",
              "Ζυγός" if isEven else "Μονός")
        
        cont = input("Enter: Επόμενη Κλήρωση,‘q’+Enter: Τερματισμός:")
        if cont.lower() == 'q':
            break       
