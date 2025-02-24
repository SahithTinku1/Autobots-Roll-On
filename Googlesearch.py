from googlesearch import search

def googlesearch(Query):
    Searches=search(Query,num_results=10)
    for i,res in enumerate(Searches,start=1):
        print(f'Result{i}:{res}')
Query=input(" what is the word you would like to search for?")
googlesearch(Query)