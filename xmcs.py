import csv
import xml.etree.ElementTree as ET

def xml_to_csv(xml_file, csv_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # for child in root:
    #     print({x.tag  for x in root.findall('.//business/locations/location/*')})
    # for child in root.findall('.//business/locations/location/*'):
    #     print(child.tag)
    #     print(child.text)

    # Open the CSV file in write mode
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)

        # Write the header row
        headers = []
        # datas=[]
        for child in root:
            headers.append(child.tag)
            # datas.append(child.text)
            # for i in child:
                # print(i.tag)
        writer.writerow(headers)
        # writer.writerow(datas)

################################################################################################################
    # DYNAMIC FILE Generator

    # for child in root:
    #     t=child.tag
    #     b=t+".csv"
    #     print(b)

        
    #     with open(b, 'w', newline='') as f:
    #         writer = csv.writer(f)
        
    #         bussiness = []
    #         for child in root:
    #             bussiness.append(child.tag)

    #             # print(child.tag)
            
    #         writer.writerow(bussiness)

    #         for item in root:
    #             rows = []
    #             for child in item:
    #                 rows.append(child.text)
    #             writer.writerow(rows)







# ################################################################################################################    
#     ###ExchangeType
#     with open(csv_file_ExchangeType, 'w', newline='') as f:
#         writer = csv.writer(f)
    
#         bussiness = []
#         for child in root[0]:
#             # bussiness.append(child.tag)
#             print(child.tag)
           
#         writer.writerow(bussiness)

#         for item in root:
#             rows = []
#             for child in item:
#                 rows.append(child.text)
#             writer.writerow(rows)




# ####################################################################################################################
#     ###Bussiness
    # with open(csv_file_bussines, 'w', newline='') as f:
    #     writer = csv.writer(f)
    
    #     bussiness = []
    #     newData=[]
    #     for child in root[1]:
    #         # bussiness.append(child.tag)
    #         j=(child)
    #         for i in j:
    #             k=(i.tag)
    #             bussiness.append(k)
    #             l=(i.text)
    #             newData.append(l)


           
    #         writer.writerow(bussiness)
    #         writer.writerow(newData)    
################################################################################################################################
# filter bussiness

    test1=[]
    test2=[]
    
    for child in root[1]:
            # bussiness.append(child.tag)
        j=(child)
        for i in j:
            k=(i.tag)
            print(k)
            # for locat in i:
                # print(locat)
        for business in j:
            if business.tag == "businessId":
                busnId=(business.text)
                busTag=business.tag
                test2.append(busnId)
                test1.append(busTag)
            # for i in  business[1]:
                
            #     print(i)
        for child in root.findall('.//business/locations/location/*/*'):
            location_tag=child.tag
            location_text=child.text

                
            with open(csv_file_location, 'w', newline='') as f:
                    writer = csv.writer(f)
                    test1.append(location_tag)
                    test2.append(location_text)
                    # test2.append(busnId)
                    # test1.append(busTag)
                    # l=(i.text)
                    # test2.append(l)

                    writer.writerow(test1)
                    writer.writerow(test2)  








################################################################################################################################    
    # with open(csv_file_bussines, 'w', newline='') as f:
    #     writer = csv.writer(f)
    
    #     bussiness = []
    #     newData=[]
    #     for child in root[1]:
    #         # bussiness.append(child.tag)
    #         j=(child)
    #         for i in j:
    #             k=(i.tag)
    #             if k =="locations":
    #                 bussiness.append(k)
    #                 l=(i.text)
    #                 newData.append(l)


           
            # writer.writerow(bussiness)
            # writer.writerow(newData)    


        # for i in bussiness:
        #     print(i)

        # for item in root:
        #     rows = []
        #     for child in item:
        #         rows.append(i.tag)
        #     writer.writerow(rows)


# ####################################################################################################################
#     ###Providers
#     with open(csv_file_Provider, 'w', newline='') as f:
#         writer = csv.writer(f)
    
#         bussiness = []
#         for child in root[2]:
#             # bussiness.append(child.tag)
#             print(child.tag)
           
#         writer.writerow(bussiness)

#         for item in root:
#             rows = []
#             for child in item:
#                 rows.append(child.text)
#             writer.writerow(rows)




# ####################################################################################################################
#     ###Rosters
#     with open(csv_file_Roster, 'w', newline='') as f:
#         writer = csv.writer(f)
    
#         bussiness = []
#         for child in root[3]:
#             # bussiness.append(child.tag)
#             print(child.tag)
           
#      j=t.    writer.writerow(bussiness)

#         for item in root:
#             rows = []
#             for child in item:
#                 rows.append(child.text)
#             writer.writerow(rows)










################################################################################################################
        # Write the data rows
        # for item in root:
        #     row = []
        #     for child in item:
        #         # row.append(child.text)
        #     writer.writerow(row)
            

# Example usage
xml_file = 'xsd2xml.xml'   # Replace with your XML file path
csv_file = 'data.csv'
csv_file_ExchangeType = 'exchangeType.csv'   # Replace with the desired output CSV file path
csv_file_bussines = 'bussines.csv'
csv_file_Provider = 'provider.csv'
csv_file_Roster = 'roster.csv'
csv_file_location = 'location.csv'

xml_to_csv(xml_file, csv_file)
