#Program to rename multiple movie files of different types on a linux server
import os, re

#[title][optional garbage][year][optional garbage][.filetype]
PATH = "/home/user/Desktop/movies/"
PATT = re.compile(r"((?P<title>[0-9A-Za-z', ]+)(?P<year>[1-2][0-9]{3}).*|(?P<noYear>.{3,30}))(?P<ftype>\.avi|\.mp4|\.mkv)$")

#if more than one period in title, removes and replaces with space, replaces other special characters with spaces
def clean(rawList):
    for file in rawList:
        if os.path.isfile(PATH+file):
            old = file
            p = file.count('.')
            new = file.replace('.', ' ', p-1).replace('[', ' ').replace(']', ' ').replace('(', ' ').replace(')', ' ').replace('_', ' ').replace('-', ' ')
            os.rename(PATH+old, PATH+new)

def main():
    count = 0

    clean(os.listdir(PATH))
    dir = os.listdir(PATH)

    for movie in dir:
        m = PATT.match(movie)
        if m:
            if m.group('noYear'):
                new = str(m.group('noYear'))+str(m.group('ftype'))
                count+=1
            elif m.group('title'):
                new = str(m.group('title').strip())+" ("+str(m.group('year'))+")"+str(m.group('ftype'))
                count+=1
            os.rename(PATH+movie, PATH+new)

    print("Renamed "+str(count)+" movies.")

main()

