# renamer
Given a path to a directory containing avi/mp4/mkv files named like [title][any #  of optional characters][YYYY][any #  of optional characters][.filetype]
this program will rename each file with the format: "title (YYYY).[filetype]"
i.e. "The.Pirates.Of.The.Carribean.[Extended].2003.avi" will become "The Pirates Of The Carribean Extended (2003).avi"


Regex pattern explained:
(?P<title>[0-9A-Za-z', ]+) -->Matches all possible movie titles (one or more characters)
(?P<year>[1-2][0-9]{3}).*  -->Matches movie release years followed by 0 or more characters of any type (1 or 2 followed by 3 of 0-9)
|                          -->or...
(?P<noYear>.{3,30})        -->in the case of a movie that does not list the year, store the title in named group noYear

All of the above is encased in the first (unnamed) capturing group.

(?P<ftype>\.avi|\.mp4|\.mkv)$ --> all movies end with a filetype of avi, mp4, or mkv
