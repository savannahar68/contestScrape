import urllib2
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import tz

#convert to local time
def utc_India_hackerrank(utc_time_str):
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('Asia/Calcutta')
    utc = datetime.strptime(utc_time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    utc = utc.replace(tzinfo=from_zone)
    central = utc.astimezone(to_zone)
    return str(central)[11:19] + " " + str(central)[8:10] + "-" + str(central)[5:7] + "-" + str(central)[0:4]

def hackerrankPage(pageurl):
	page = urllib2.urlopen(pageurl)
	soup = BeautifulSoup(page, "lxml") #lxml parser
	#print(soup.prettify()) #prints the whole URL page
	print('HACKERRANK CONTESTS \n')
	for links in soup.findAll('div', {'data-contest-state': 'Active'}):
		for x in links.findAll('div',{'class':'contest-name'}):
			contest_name = x.text
		contest_start_time = links.findChild('meta', {'itemprop': 'startDate'})
		contest_end_time = links.findChild('meta', {'itemprop': 'endDate'})
		if(contest_start_time and contest_end_time):
			print contest_name ,' : startDate : ',  utc_India_hackerrank(contest_start_time['content']),' EndDate : ', utc_India_hackerrank(contest_end_time['content'])
		else:
			for y in links.findAll('div', {'class':'contest-status'}):
				print contest_name,' : ', y.text

if __name__ == '__main__':
#the following are the URLs of the contest page of respective competitive websites
	hackerrank = 'https://www.hackerrank.com/contests'
	codechef = 'https://www.codechef.com/contests'
	hackerearth = 'https://www.hackerearth.com/challenges/'
	codeforces = 'http://codeforces.com/contests'

	hackerrankPage(hackerrank)