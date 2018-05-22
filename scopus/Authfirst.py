#Import library
from pyscopus import Scopus
#key = '50312b4710a276ec9670642f0f455259'
key = '1e499709c626679a80b27fc8a207ceb3'
scopus = Scopus(key)
def cari(nama):
    search_df = scopus.search("AUTHFIRST("+nama+")", count=10)
    return search_df.head(10)

