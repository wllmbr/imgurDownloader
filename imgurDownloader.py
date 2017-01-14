import urllib2
import re
import time

def makeImage(url):
	#Get the name of the image
	address = re.split(r"[\./]*",url)
	#print  address
	title = address[3]
	type = address[4]
	name = "%s.%s" % (title,type)
	
	#Open the URL
	url = "http://%s" % url
	page = urllib2.urlopen(url)
	data = page.read()
	
	
	with open(name,'wb') as file:
		file.write(data)
		
	return
	
def driver():
	sourceFile = raw_input("Name of file that contains targets: ")
	inputFile = open(sourceFile,'r')
	urlListing = []
	iff = ""
	for lines in inputFile:
		iff += lines
	fileList = iff.split("\n")
	for i in range(0,len(fileList)):
		if("hash" in fileList[i]):
			urlFileSplit = fileList[i].split("\"")
			urlFile = urlFileSplit[3]
			foundExt = False
			while(not(foundExt)):
				i+=1
				if("ext" in fileList[i]):
					extSplit = fileList[i].split("\"")
					ext = extSplit[3]
					url = "i.imgur.com/%s%s" % (urlFile,ext)
					urlListing.append(url)
					foundExt = True
					
	inputFile.close()
	print "Found %d targets. Starting download." % len(urlListing)
	for i in range(0,len(urlListing)):
		progress = i/len(urlListing)
		print "\tProgress: %.1f%%" % progress,
		makeImage(urlListing[i])
		time.sleep(0.1)
		
		
if __name__ == "__main__":
	driver()