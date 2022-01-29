class Car:

    def __init__(self,name ,brand,price):
        self.__name= name
        self.__brand = brand
        self.__price = price

    def get_name(self):
        return self.__name

    def get_brand(self):
        return self.__brand

    def get_price(self):
        return self.__price

    def __str__(self):
        return "My car name is {}, the brand is {} and for Price: ${}".format(self.__name,self.__brand,self.__price)


root =True
start = input("Do you wanna play?")
try:
    if start.upper()=="Y":
        play = True
    elif start.upper()=="N":
        play=False
    else:
        play=False
        root=False

except Exception :
    print("Something Went Wrong")

list_m = []
while play==True:

    loopGame = True

    while loopGame==True :
        try:
            carName = input("Enter a Car Name: ")
            carBrand = input("Enter a Car Brand: ")
            carPrice = int(input("Enter a Car Price: "))

            c1 = Car(carName,carBrand,carPrice)
            print(c1)
            list_m.append(c1)
            loopGame=False
            repeat = True

            while repeat==True:
                ask = input("Do you wanna play Again?")
                if ask.upper() == "Y":
                    play = True
                    loopGame=True
                    break
                elif ask.upper() == "N":
                    play = False
                    loopGame=False
                    break
                else:
                    repeat =True


        except Exception:
            print("There was an Error!!")
            loopGame=True



if root==False and play==False:
    print("Game Never Started!!!")
else:
    print("Game Over!!")
    m = list_m[0]
    for i in list_m:
        if m.get_price() < i.get_price():
            m = i

    print("The Most Expensive Car from the lot is {} of Brand {} which Retails for ${}".format(m.get_name(),m.get_brand(),m.get_price()))

    for a in list_m:
        print(a)
