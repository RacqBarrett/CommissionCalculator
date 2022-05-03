#Author: Racquel Barrett
#Date Created: April 4, 2022
#Course: ITT103
#Purpose: To calculate the commission received by each sales person. The commission rate is based on the Class to which a salesperson belongs.

salesperson_ID = int(input("Please enter salesperson number: "))
sales_amount = float(input("Please enter sales amount: $ "))
Class = int(input("Please enter the Class: "))


if Class == 1:     #If class is equal to 1
        
        if sales_amount <= 1000:        #If sales amount is less than or equal to 1000       

                comission = (6 * sales_amount)/100      #6% comission rate is applied

        elif sales_amount > 1000 and sales_amount < 2000:       #If sale amount is greater than 1000 but less than 2000

                comission = (7 * sales_amount)/100      #7% comission rate is applied     
        else:
                comission = (10 * sales_amount)/100     #10% comission rate is applied

        print("Commission received: $ %.2f" % comission)       #Output the total commission received, rounded to two decimal place, after calculation 


elif Class == 2:        #If class is equal to 2
                        #Same conditions as above will apply, with the commission rates being different
        if sales_amount < 1000: 

                comission = (4 * sales_amount)/100
        else:
                comission = (6 * sales_amount)/100

        print("Commission received: $ %.2f" % comission)


elif Class == 3:        #If Class is equal to 3

        comission = (4.5 * sales_amount)/100

        print("Commission received: $ %.2f" % comission)

else:   #If an invalid class is enetered, "comission" variable will have no assigned value and will raise an error.
        print("Invalid Class entered. Please restart.")
