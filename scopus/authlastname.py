from pyscopus import Scopus
key = '50312b4710a276ec9670642f0f455259'
scopus = Scopus(key)
def pencarian(nama):
    search_df = scopus.search("AUTHLASTNAME("+nama+")", count=10)
    return search_df.head(10)