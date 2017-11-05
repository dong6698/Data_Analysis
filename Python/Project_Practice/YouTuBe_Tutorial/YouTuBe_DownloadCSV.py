from urllib import request

goog_url = 'http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=4&e=4&f=2016&g=d&a=7&b=19&c=2004&ignore=.csv'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split('\\n')
    file_name = r'goog.csv'
    fw = open(file_name, 'w')
    for line in lines:
        fw.write(line + '\n')
    fw.close()

download_stock_data(goog_url)
