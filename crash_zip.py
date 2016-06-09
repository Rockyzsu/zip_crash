__author__ = 'rocky'
import zipfile
filename="sample.zip"
dictFile="pwdict.txt"
password=open(dictFile,'r')
for p in password:
    zf=zipfile.ZipFile(filename)
    p=p.strip('\n')
    print p
    try:
        zf.extractall("./sample",pwd=p)
        print "crash. Password is %s" %p
        exit(0)
    except:
        pass

print "No found password"
