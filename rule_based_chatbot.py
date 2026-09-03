import random
from colorama import Fore,init
init();

# dictionary
destinations = {
"beaches": ["Bali", "Maldives", "Phuket"],
"mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas","Hunza"],
"cities": ["Tokyo", "Paris", "New York","islamabad"]
}
def recommend():
    print(Fore.PINK + 'travelBot:-beaches,mountains or cites')
    choice = input().strip().lower()
    if choice in destinations():
        suggestion = random.choice(destinations[choice]) 
        print(Fore.RED+"travelBot:how about ",suggestion,"?")
        print(Fore.RED+ "travelBot:do you like it?(yes/no)")
        answer = input().strip().lower()
        if answer == "yes":
          print(Fore.GREEN + "travelBot:-Lets try another....")
          recommend()
    else:
        print(Fore.RED + "travellot:-sorry i dont have that kind of information..........")
    

def chat():
    print(Fore.RED + "hello i am a travelBot")
    NAME = input(Fore.GREEN +"your name")
    print(Fore.YELLOW +"nice to meet you "+ NAME)
    print(Fore.BLUE + "i can suggest travel spots (type 'recommend')")
    print(Fore.RED + "i can offer packing tips(say 'say paking') ")
    print(Fore.BLUE +"type 'exit'to endd.\n" )
    while True:
        user_input = input().strip().lower()
        if user_input =='recomend':
            recommend()
        elif user_input=="packing":
            print(Fore.GREEN +"* YOU SHOULD TAKE YOUR SKINCARE..")
            print(Fore.GREEN +"* TAKE CLOTHS ACCORDING TO YOUR NEED....")
            print(Fore.GREEN +"* TAKE FOOD OR SOMETHING TO EAT FROM HOME TO SAVE MONEY..")
            print(Fore.GREEN +"* CHECK WEATHER FORCAST....")
        elif user_input=='exit':
            print(Fore.RED +"safe travels good byeeeee")
            break
        else:
            print("invalid choice")
chat()
