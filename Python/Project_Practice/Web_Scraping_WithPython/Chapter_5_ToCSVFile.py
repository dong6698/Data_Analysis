import csv

csvfile = open('test.csv', 'w+')
try:
    writer = csv.writer(csvfile)
    writer.writerow(('uumber', 'number plus 2', 'number times 2'))
    for num in range(5):
        writer.writerow((num, num + 2 , num * 2))
finally:
    csvfile.close()