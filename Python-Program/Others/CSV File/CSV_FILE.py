# import csv
# from csv import reader
# with open("CSV_FILE.csv","r") as f:
#     csv_read=csv.reader(f)
#     csv_read= reader(f)
#     for i in csv_read:
#         print(i)
    # print(csv_read)
    
# import csv
# with open("MY_CSV_FILE.csv","a") as f:
#     x=csv.writer(f)
#     x.writerow(['name','movie','year','age'])

            #  INSERT DATA FROM ONE FILE TO ANOTHER 
            
# import csv
# with open('CSV_FILE.csv','r') as f:
#     with open("MY_CSV_FILE.csv",'a', newline='') as wf:
#         csv_reader=csv.reader(f)
#         csv_writer=csv.writer(wf)
#         for i in csv_reader:
#             csv_writer.writerows([i])

from csv import DictWriter
with open('CSV_FILE.csv','a', newline='') as f:
    csv_wriier=DictWriter(f,fieldnames=['first_name','last_name','age'])
    csv_wriier.writeheader()
    # csv_wriier=DictWriter(f,fieldnames=['first_name','last_name',])
    csv_wriier.writerows([[ 'first_name': 'mangal'],['last_name':'don'],['age':22 ],['first_name': 'puneet'],['last_name':'chaudhary'],['age':2],['first_name': 'chota'],['age':20]])
    # csv_wriier.writerow({'first_name': 'mangal',
    #                      'last_name':'don',
    #                      'age':22 })
    # csv_wriier.writerow({'first_name': 'puneet',
    #                      'last_name':'chaudhary',
    #                      'age':25 })
    # csv_wriier.writerow({'first_name': 'chota',
    #                      'last_name':'don',
    #                      'age':20 }) 
    

