import csv
f = open('file.csv',"a",newline="")
tup1= ('Bob',50)
writer = csv.writer(f)
writer.writerow(tup1)

tup2=('John',12)
writer.writerow(tup2)
f.close()