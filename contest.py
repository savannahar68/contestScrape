import urllib2
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import tz
import string
import re
from prettytable import PrettyTable

#convert to local time
def utc_India_hackerrank(utc_time_str):
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('Asia/Calcutta')
    utc = datetime.strptime(utc_time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    utc = utc.replace(tzinfo=from_zone)
    central = utc.astimezone(to_zone)
    return str(central)[11:19] + " " + str(central)[8:10] + "-" + str(central)[5:7] + "-" + str(central)[0:4]

def time_converter_codechef(time):
	#return the string in proper format
	return time[11:19] + " " + time[8:10] + "-" + time[5:7] + "-" + time[0:4]

def hackerrankPage(pageurl):
	page = urllib2.urlopen(pageurl)
	soup = BeautifulSoup(page, "lxml") #lxml parser
	#print(soup.prettify()) #prints the whole URL page
	print('HACKERRANK CONTESTS \n')
	i = 1
	for links in soup.findAll('div', {'data-contest-state': 'Active'}):
		for x in links.findAll('div',{'class':'contest-name'}):
			contest_name = x.text
		contest_start_time = links.findChild('meta', {'itemprop': 'startDate'})
		contest_end_time = links.findChild('meta', {'itemprop': 'endDate'})
		if(contest_start_time and contest_end_time):
			print i,') ', contest_name ,' - startDate : ',  utc_India_hackerrank(contest_start_time['content']),' EndDate : ', utc_India_hackerrank(contest_end_time['content'])
		else:
			for y in links.findAll('div', {'class':'contest-status'}):
				print i,') ', contest_name,' : ', y.text
		i = i + 1;

def codechefPage(pageurl):
	page = urllib2.urlopen(pageurl)
	soup = BeautifulSoup(page, "lxml") #lxml parser
	#print(soup.prettify()) #prints the whole URL page
	print('\nCODECHEF CONTESTS \n')
	print('PRESENT CONTESTS ')
	i = 1
	for table in soup.find('h3', text="Present Contests").findNext('table'):
		tb = table.find_next_sibling('tbody')
		if tb is not None:
			break
	for links in tb.findAll('a'):
		start_date_tag = links.findParent().find_next_sibling('td')
		end_date_tag = start_date_tag.find_next_sibling('td')
		print i,') ', links.string ,'- startDate : ', time_converter_codechef(start_date_tag['data-starttime']),'endDate : ', time_converter_codechef(end_date_tag['data-endtime'])
		i = i + 1;
	i = 1
	print('\nFUTURE CONTESTS ')
	for table in soup.find('h3', text="Future Contests").findNext('table'):
		tb = table.find_next_sibling('tbody')
		if tb is not None:
			break
	for links in tb.findAll('a'):
		start_date_tag = links.findParent().find_next_sibling('td')
		end_date_tag = start_date_tag.find_next_sibling('td')
		print i,') ', links.string ,'- startDate : ', time_converter_codechef(start_date_tag['data-starttime']),'endDate : ', time_converter_codechef(end_date_tag['data-endtime'])
		i = i + 1

def codeforcePage(pageurl):
	page = urllib2.urlopen(pageurl)
	soup = BeautifulSoup(page, "lxml") #lxml parser
	#print(soup.prettify()) #prints the whole URL page
	details = []
	print('\nCODEFORCES CONTESTS \n')	
	for links in soup.findAll('div', {'class' : 'datatable'}):
		table = links.findNext('table')
		if table:
			for x in table.findAll('td'):
				details.append((x.text).strip('\r\n\t '))
			break;
	#details = [x.replace("\r\n","") for x in details]
	count = 0
	details = [re.sub("Before registration\r\n\s\s+"," ", x) for x in details]
	t = PrettyTable(['Name', 'Start', 'Duration', 'Days', 'Reg(End)'])
	for x in range(0, len(details)/6):
		l = details[count:count+6]
		l = [x for i,x in enumerate(l) if i!=1] 
		#print l
		t.add_row(l)
		count+=6
				 
	print t 
		

if __name__ == '__main__':
#the following are the URLs of the contest page of respective competitive websites
	hackerrank = 'https://www.hackerrank.com/contests'
	codechef = 'https://www.codechef.com/contests'
	hackerearth = 'https://www.hackerearth.com/challenges/'
	codeforces = 'http://codeforces.com/contests'

	hackerrankPage(hackerrank)
	codechefPage(codechef)
	codeforcePage(codeforces)