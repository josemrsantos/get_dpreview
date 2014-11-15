from lxml import html
import requests
import urllib
import random
import sys

#########################################################
# Main
#########################################################
def main(argv):
    file_write = argv[1]
    # Select a closed chanlenge from the first page
    page = requests.get('http://www.dpreview.com/challenges/ChallengesFinished.aspx')
    tree = html.fromstring(page.text)
    winners = tree.xpath('//a[contains(@id,"lnkChallengeDetail")]/@href')
    selected = random.choice(winners)
    # Select an entry from that chanlenge - top 5 only
    page_selected = requests.get(selected)
    tree_selected = html.fromstring(page_selected.text)
    first_place = tree_selected.xpath('//a[contains(@class, "imgIcon zoomIcon")]/@href')
    first_place_bigger = random.choice(first_place[:5])
    # Get image and write it to a file
    id = first_place_bigger[49:].replace('&View=Results&Rows=4','')
    url =  "http://www.dpreview.com/challenges/DownloadOriginal.aspx?id=%s"% id
    urllib.urlretrieve(url, file_write)

# Call main if not imported
if __name__ == "__main__":
    main(sys.argv)
