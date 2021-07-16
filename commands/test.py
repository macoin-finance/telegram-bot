web = urllib.urlopen("http://www.nasdaq.com/quotes/nasdaq-financial-100-stocks.aspx")
pattern = re.compile('var table_body = (.*?);')

soup = BeautifulSoup(web.read(), "lxml")
scripts = soup.find_all('script')
for script in scripts:
   if(pattern.match(str(script.string))):
       data = pattern.match(script.string)
       stock = json.loads(data.groups()[0])
       print (stock)
