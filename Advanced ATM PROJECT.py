import random
#import validation 
#import database
database = { 
    3455698649: ['sam', 'godwin', 'samgodwin03@gmail.com','passwords', ]

 }
 
current_balance = 100000
    

def init():
    print('welcome to wema bank')
    print('what will you like to do?')
    print('1. login')
    print('2. register')
    SelectedOption = int(input('please select an option: \n'))
    if(SelectedOption == 1):
        print(login())
    elif(SelectedOption == 2):
        print(register())



def login():
    print('========== login===========')
    name = int(input('what is your account number?: \n'))
    password = input('what is your password? \n')

    
    for account_Number, user_details in database.items():
        if (account_Number == name):
            if user_details[3] == password:
                print('proceed')

                bankoperation(user_details)
                

        
        
               

            

              
   
  
def register():
    Email = input('What is your email? \n')
    firstname = input('what is your first name? \n')
    lastname = input('what is you lastname? \n')
    password= input(' whar is your password? \n')

    account_Number = generationofAccountNumber()
    database[account_Number] = [firstname, lastname, Email, password ]

    
    print('your pass word has been created')
    print('your password is: %d' % account_Number)
    login()


def bankoperation(user):
    print('we have the following options:')
    print('1. deposit')
    print('2. withdrawal')
    print('3. complaint')

    selectedAction = int(input('please select an action: \n'))
    if (selectedAction == 1):
        print(depositOperation())
        
        
        
    elif(selectedAction == 2):
        print(withdrawalOperation())
      
    elif(selectedAction == 3):
        print(complaintOperation())
        

def depositOperation():
    deposit = int(input('how much do you want to deposit?: \n'))
    print(deposit + current_balance)
    
  
      
def withdrawalOperation():
    withdraw = int(input('how much do you want to withdraw?: \n'))
    if(withdraw <= current_balance):
        print('Take Cash')
    if(withdraw > current_balance):
        print('insufficient balance')

def complaintOperation():
    complaint = input('do you have any complaint \n')
    print('complaint received. will get back to you shortly.')



def generationofAccountNumber():
   
    return random.randrange(1111111111,9999999999)


init()


