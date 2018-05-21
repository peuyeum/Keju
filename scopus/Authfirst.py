#Import library
from pyscopus import Scopus
key = '1e499709c626679a80b27fc8a207ceb3'
scopus = Scopus(key)

#Test Search
search_df = scopus.search("KEY(interdisciplinary collaboration)", count=30)
#print (seaarch_df.head(10))

search_df = scopus.author("AUTHLASTNAME(scott)", count=2)
def cari(nama):
    return nama+"Pasti Bisa"  # untuk memanggil variable nama dengan menambah value pasti bisa

# Test Search Author

#Test Search Author