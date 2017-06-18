#Just a simple fetcher

import urllib
import random
from urllib2 import urlopen
from bs4 import BeautifulSoup


def makebs4 (url):
   html_url = urlopen(url).read()
   return BeautifulSoup(html_url,"html.parser")
  
  
def image_get_method(url):
  bs4copy = makebs4(url)
  images =  bs4copy.findAll('img')
  no_of_img_found = len(images)
  print (str(no_of_img_found))
  print ('Downloading images......')
  for imga in images:
      imgUrl = imga.get('src')
      print imgUrl
      counter = 1
      random_num = random.randint(1,1000)
      filenamepic = 'displaypicture'+str(counter)+str(random_num)+'.jpg'
      urllib.urlretrieve(imgUrl, filenamepic)
      counter+=1


def instam_id():
  print 'Enter q to close'
  usr_id = raw_input('Enter the username: ')
  while usr_id is not 'q':
      instaurl = 'https://instagram.com/'+str(usr_id)
      #to check if link exists using https codes
      check_code = urllib.urlopen(instaurl).getcode()
      if check_code is 200:
        print 'Link OK'
        break 
      else : 
        print 'Link not found 404 error'
        break
  return instaurl

def main():
  main_url = instam_id()
  image_get_method(main_url)
  
if __name__ == '__main__':
  main()
