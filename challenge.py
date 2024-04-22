import sys

# builds a histogram for a given string
def get_histogram(s:str):
    return {c:sum([1 if b == c else 0 for b in s]) for c in s}  
    
def count_spells(searched:str, bowl:str):
    if len(searched) < 1 or len(searched) > len(bowl):
        return 0
    
    histo_searched = get_histogram(searched)
    histo_bowl = get_histogram(bowl)

    n_found = 0
    # the minimum: all chars from the searched term must be in the bowl (case sensitive)
    if set(histo_searched.keys()).issubset(set(histo_bowl.keys())):
        # ok, all searched chars are in the bowl! we then evaluate the amount of times each one of them occurs,
        # compared to the amount of times each one occurs in the searched term. this way we'll have a list
        # of how many times each of the chars of the search term present in the bowl can be used to build the search term 
        # - and then we take the smallest of these (i.e., the number of how many times the searched term can be built from the bowl chars)
        n_found = min(
                [histo_bowl[v]//histo_searched[v] for v in histo_searched.keys()]
            )
    return n_found

def count_pennymac_spells(bowl:str):
    return count_spells('PENNYMAC', bowl)

if __name__ == "__main__":
    # searched = 'PENNYMAC'
    # bowl = 'hP.E.N.Y.M.A.C.N.iltoxhYiltonPENNMACPENMMNYMACCAYNNEPhiltonnotlihn'

    # tests
    assert(count_spells('', '') == 0)
    assert(count_spells('', 'PENNYMAC') == 0)
    assert(count_spells('hilton', 'PENNYMAC') == 0)
    assert(count_spells('hilton', 'PhEiNlNtYoMnAC') == 1)
    assert(count_spells('PENNYMAC', 'PhEiNlNtYoMnAC') == 1)
    assert(count_spells('PENNYMAC', '') == 0)
    assert(count_spells('PENNYMAC', 'CAMYNNEP') == 1)
    assert(count_spells('PENNYMAC', 'CAMYNNE') == 0)
    assert(count_spells('PENNYMAC', 'CAMYNNEPxxxPENNYMAC') == 2)
    assert(count_spells('PENNYMAC', 'CoAoMoYoNoNoEoPoxoxoxoPoEoNoNoYoMoAoCo') == 2)
    assert(count_spells('PENNYMAC', 'CoAoMoYoNoNoEoPoxoxoxoPoEoNoNoYoMoAoCoPENNYMAC') == 3)

    bowl = sys.argv[1]
    print(count_pennymac_spells(bowl))