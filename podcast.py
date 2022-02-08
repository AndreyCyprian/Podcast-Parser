import feedparser
import json
import argparse
import os, sys, subprocess

#all of my arg parse arguments
parser = argparse.ArgumentParser(description='podcast feedparser')
parser.add_argument('-s', action='store_true', help= 'This argument will omit the summaries of the podcasts that you entered' )
parser.add_argument('-n', type=int, help='This argument will retrive the last n amount of podcast')
parser.add_argument('link', help='Please enter a link for the feedparser')

args = parser.parse_args()

n = args.n#the number

link = f'{args.link}'

feed = feedparser.parse(link)
len(feed.entries)

def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

#if the s argument is added this method simply doesn't imclude the summary entry
if args.s:
    for x in range(n):
        print(f'link {args.link}')
        print(feed.entries[x].title)
        print(feed.entries[x].author)
        print(feed.entries[x].published)
else:#include all variables 
    for x in range(n):
        print(f'link {args.link}')
        print(feed.entries[x].title)
        print(feed.entries[x].author)
        print(feed.entries[x].published)
        print(feed.entries[x].summary)
