import urllib.request
import html

def read_website(url):
    mybytes = url.read() #read a html file as bytes
    print(mybytes)
    mystr = mybytes.decode("utf-8") #decode the bytes to a string
    mystr = html.unescape(mystr) #for special characters
    return mystr

def get_singles(mystr):
    position = mystr.find('<div class="title">') #looking for the title html tag
    count = 1
    while position != 1 and count <= 10: ##-1 is returned if the html is not found
        start = mystr.find('>',position + len('<div class="title">')+1) #find the first ">" after the html title tag
        stop = mystr.find('<', start) #find the first "<" after the html tag
        print(f'{count}.{mystr[start:stop]})')
        position = mystr.find('<div class="title">',stop)
        count += 1

if __name__ == '__main__':
    fp = urllib.request.urlopen("https://www.officialcharts.com/charts/singles-chart/")
    web_str = read_website(fp)
    get_singles(web_str)
