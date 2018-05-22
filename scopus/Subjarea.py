#import libary
from pyscopus import Scopus
key = '28afb89a9b06c53a126edd118d079c63'
scopus = Scopus(key)

def cari(nama): 
    #search = scopus.search("KEY(interdisciplinary collaboration)", count=30) 
    search_au = scopus.search_author("AUTHLASTNAME(scott)") 
    #return print(search_df.head(10)) 
    return print(search_au)
  
