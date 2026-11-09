import sys, urllib.request as u
w = open(sys.argv[1], "wb")
for url in sys.argv[2:]:
    w.write(u.urlopen(url, timeout=120).read())
w.close()
