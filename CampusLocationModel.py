import csv

class CampusLocationModel:

    # constructor
    def __init__(self,name,ref,classification):
        self.name = name
        self.ref = ref
        self.classification = classification

    #  Building/location details list   
    def locationDetails():
        names=[]
        with open('buildings.csv') as csvfile:
            headings = next(csvfile) # removing header row
            csv_reader = csv.reader(csvfile)
            data = list(csv_reader)
            
            # sorted_data = sorted(data, key=lambda x: x[0])
            
            return data

    #  Building/location classification list
    def buildingClassifications():
        classifications=[]
        with open('buildings.csv') as csvfile:
            headings = next(csvfile) # removing header row
            csv_reader = csv.reader(csvfile)
            for rec in csvfile:
                buildingClassification=rec.split(',')
                classifications.append(buildingClassification[2])
                cls = {x.replace('\n', '') for x in classifications}
            cls = sorted(cls)

            return cls  
            
