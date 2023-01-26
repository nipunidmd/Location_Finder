import csv
from CampusLocationModel import CampusLocationModel

# locations
out1 = CampusLocationModel.locationDetails()

# location classifications
out2 = CampusLocationModel.buildingClassifications()

# Application 1 - Without GUI

class CampusLocation:

    # Step 1 - Select an option to find building details
    def selectOption():
        print("Select and input a option number")
        print("---------------Options---------------")
        print("1 - Search by Building/Location Name")
        print("2 - Search by Building/Location Reference Number")
        print("3 - Search by Building/Location Classification")
        option = input("Selected option ")
        print(option)
        return option

    # Step 2 - Enter name/ refernce or select a classification
    def selectLocation(opt,lol,cls):

        # opion 1 - Search by Name
        if(opt == '1'):
            searchString = input("Enter Full or Part of the Building Name \n")
            count = 0
            # try:
            for line in lol:
                
                # Search by Name
                if searchString.casefold() in line[1].casefold():
                    count +=1
                    # Step 3 - Display Building Deatils
                    print("Ref:"+line[0]," Name:"+line[1]," Classification:"+line[2])
            if(count==0):
                print("Not matching with a building name")
            else:
                print("%d matching results with '%s'"%(count,searchString))
            
        #option 2 - Search by reference
        elif(opt == '2'):
            searchString = input("Enter Full or Part of the Building Reference Number \n")
            count = 0
            # try:
            for line in lol:
                
                # Search by reference
                if searchString.casefold() in line[0].casefold():
                    count +=1
                    # Step 3 - Display Building Deatils
                    print("Ref:"+line[0]," Name:"+line[1]," Classification:"+line[2])
            if(count==0):
                print("Not matching with a building reference number")
            else:
                print("%d matching results with '%s'"%(count,searchString))

        # option 3 - Search by Classification
        elif(opt == '3'):
            
            cls_no = 0
            print("---Classifications---")
            for clsf in cls:
                cls_no += 1
                print(cls_no,clsf)
            
            code = int(input("Enter a number from the buidling classification list \n"))
            searchString = cls[code-1]
            
            count = 0
            for line in lol:
                
                # Search by Classification
                if searchString in line[2]:
                    count +=1
                    # Step 3 - Display Building Deatils
                    print("Ref:"+line[0]," Name:"+line[1]," Classification:"+line[2])
            if(count==0):
                print("No matching classification from the code you entered")
            else:
                print("%d matching results with '%s'"%(count,searchString))
        else:
            print("Invalid input")

    selectLocation(selectOption(),out1,out2)
    
    
