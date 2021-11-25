#Title: AMAZON CSO & ASCS GIFTS
print('\n\t\t\t\t\tAMAZON CSO & ASCS GIFTS')

#Initializing Security keys to block repeated gift claims
key1 = 'start'
key2 = 'start'

#Choosing the type of gift
while True:
    code = input('''\n\n
    Enter the code as in the below format to claim your gifts
    [ (amazonId) for CSO  |  (amazonID)ASCS  for ASCS gift ] :  ''')

    #Defining function to gather employee details
    def get_details():
            name = input('\n\nEnter your name: ')
            print('Name: %s'%name)
            phone_number = input('\n\nEnter your phone number: ')
            print('Phone Number: %s'%phone_number)
            address = input('\n\nEnter your address: ')
            print('Address: %s'%address)
            pincode = input('\n\nEnter your pincode: ')
            print('Pincode: %s'%pincode)
            gifts_quantity = int(input('\n\nEnter number of gifts you want: '))
            print('Number of Gifts added to cart: %d'%gifts_quantity)
            #Employee is allowed to choose only one gift
            while gifts_quantity > 1:
                print('''\n
                Sorry! You can only select one gift''')
                gifts_quantity = int(input('\n\nEnter number of gifts you want: '))
                print('Number of Gifts added to cart: %d'%gifts_quantity)
            return
            
    #For CSO gift
    if code == 'kbhaala':
        #Rejecting more than one claim of the same gift
        if key1 == 'end':
            print('''\n\n
            Sorry! You have claimed your gift already!''')
        #Getting details of the employee 
        while key1 == 'start':
            print('\n\n\t\t\t\t\tCSO GIFT')
            get_details()
            print('''\n\n
            Your response has been recorded! 
            You will be recieving your CSO gift soon.....!''')
            key1 = 'end' 
        
         
    #For ASCS gift             
    elif code == 'kbhaalaASCS':
        #Rejecting more than one claim of the same gift
        if key2 == 'end':
            print('''\n\n
            Sorry! You have claimed your gift already!''')
        #Getting details of the employee       
        while key2 == 'start':
            print('\n\n\t\t\t\t\tASCS GIFT')
            get_details()
            print('''\n\n
            Your response has been recorded! 
            You will be recieving your ASCS gift soon.....!''')
            key2 = 'end'
        
        
    #Throws error if the employee gives a different employee ID other than their own.
    else:
        print('''\n\n
        Sorry, Please enter only the code associated with your employeeID 
        or type the code in the correct format as mentioned!''')
        


