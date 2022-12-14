import requests
import xlsxwriter
from bs4 import BeautifulSoup


crypto_dict = {'BTC': 0, 'ETH': 1, 'BCH': 2, 'XRP': 3, 'LTC': 4, 'DASH': 5, 'BTG': 6,
               'MIOTA': 7, 'ADA': 8, 'ETC': 9, 'XMR': 10, 'XEM': 11, 'NEO': 12,
               'EOS': 13, 'XLM': 14, 'BCC': 15, 'QTUM': 16, 'ZEC': 17, 'OMG': 18,
               'LSK': 19, 'USDT': 20, 'HC': 21, 'WAVES': 22, 'STRAT': 23,
               'PPT': 24, 'BTS': 25, 'DCR': 26, 'MONA': 27, 'ARDR': 28, 'ARK': 29
               }
all_ticks = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
             [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
             [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
             [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

# i - amount of days we want to take from one month (didnt have time to make it better)
for i in range(1):
    date = 20171201+i  # Year Month Day
    date_str = str(date)
    new_date = date_str[:4] + "-" + date_str[4:6] + "-" + date_str[6:8]
    url = f"https://coinmarketcap.com/historical/{date}"

    # Data download
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    unparsed_data = soup.find_all('tbody')[0]  # Tag type

    # Fill the array with the scraped data
    for x in range(28):
        print(new_date)
        print(unparsed_data.contents[x])
        Name = unparsed_data.contents[x].contents[1].contents[0].contents[2].text
        Ticker = unparsed_data.contents[x].contents[2].contents[0].text
        MarketCap = unparsed_data.contents[x].contents[3].contents[0].text
        Price = unparsed_data.contents[x].contents[4].contents[0].text
        all_ticks[crypto_dict[Ticker]].append([new_date, Name, Ticker, MarketCap, Price])

# TODO: Saving every crypto into separate worksheet
# Save to xlsx file (Excel or Libre Office Calc)
# workbook = xlsxwriter.Workbook('hello.xlsx')
#
# worksheet = workbook.add_worksheet('BTC')
# worksheet.write('A1', 'Name')
# worksheet.write('B1', 'Ticker')
# worksheet.write('C1', 'Market Cap')
# worksheet.write('D1', 'Price')
# worksheet.write('E1', 'Date')
# worksheet.write(f"A{2+i}", unparsed_data.contents[0].contents[1].contents[0].contents[0]['alt'])
# worksheet.write(f"B{2+i}", unparsed_data.contents[0].contents[3].contents[0].text)
# worksheet.write(f"C{2+i}", unparsed_data.contents[0].contents[3].contents[0].text)
# worksheet.write(f"D{2+i}", unparsed_data.contents[0].contents[4].contents[0].text)
# worksheet.write(f"E{2+i}", new_date)
# workbook.close()
