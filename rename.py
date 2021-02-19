#Program to rename multiple movie files of different types on a linux server
import os, re

#/run/user/1000/gvfs/smb-share:server=raspberrypi,share=videos
PATH = "/home/warpig/Desktop/movies"
MAX = 20 #max title length

#if more than one period in title, removes and replaces with space
def clean(rawList):
    for file in rawList:
        old = file
        p = file.count('.')
        new = file.replace('.', ' ', p-1).replace('[', ' ').replace(']', ' ').replace('(', ' ').replace(')', ' ').replace('_', ' ').replace('-', ' ')
        os.rename(PATH+"/"+old, PATH+"/"+new)
        #print(new)

def main():
    #[title][optional garbage][year][optional garbage][.filetype]
    patt = re.compile(r"((?P<title>[0-9A-Za-z', ]+)(?P<year>[1-2][0-9]{3}).*|(?P<noYear>.{3,30}))(?P<ftype>\.avi|\.mp4|\.mkv)$")

    dir = os.listdir(PATH)
    clean(dir)

    for movie in dir:
        old = movie
        m = patt.match(movie)
        if m:
            if m.group('noYear'):
                new = str(m.group('noYear'))+str(m.group('ftype'))
            elif m.group('title'):
                new = str(m.group('title'))+"("+str(m.group('year'))+")"+str(m.group('ftype'))
            print(new)
            os.rename(PATH+"/"+old, PATH+"/"+new)


main()

