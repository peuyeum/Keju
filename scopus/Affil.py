#proses import library pyscopus dari app
from pyscopus import Scopus
key = '1e499709c626679a80b27fc8a207ceb3'
scopus = Scopus(key)

#Test Pencarian
def cari(name):
	search = scopus.search("AFFIL("+name+")", count=10)
	return search.head(10)