# builds a histogram for a given string
def get_histogram(s):
    return {c:sum([1 if b == c else 0 for b in s]) for c in s}  
    
searched = 'PENNYMAC'
bowl = 'hP.E.N.Y.M.A.C.N.iltoxhYiltonPENNMACPENMMNYMACCAYNNEPhiltonnotlihn'

histo_searched = get_histogram(searched)
histo_bowl = get_histogram(bowl)

print(histo_searched)
print(histo_bowl)

n_found = 0
# the minimum: all chars from the searched term must be in the bowl
if set(histo_searched.keys()).issubset(set(histo_bowl.keys())):
    # ok, all searched chars are in the bowl! we then evaluate the amount of times each one of them occurs,
    # compared to the amount of times each one occurs in the searched term. this way we'll have a list
    # of how many times each of the chars of the search term present in the bowl can be used to build the search term 
    # - and then we take the smallest of these (i.e., the number of how many times the searched term can be built from the bowl chars)
    n_found = min(
            [histo_bowl[v]//histo_searched[v] for v in histo_searched.keys()]
        )

print(n_found)