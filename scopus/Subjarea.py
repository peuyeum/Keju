#import libary
from pyscopus import Scopus
key = '28afb89a9b06c53a126edd118d079c63'
scopus = Scopus(key)

def cari(area): 
	search_df = scopus.search("SUBJAREA("+ area + ")", count=30)
	return search_df.head(10)
