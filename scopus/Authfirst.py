#Import library
from pyscopus import Scopus
key = '1e499709c626679a80b27fc8a207ceb3'
scopus = Scopus(key)
def cari(nama):
    #search = scopus.search("KEY(interdisciplinary collaboration)", count=30)
    search_au = scopus.search_author("AUTHLASTNAME(scott)")
    #return print(search_df.head(10))
    return print(search_au)


