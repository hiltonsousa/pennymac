# pennymac

## Table of Contents

Problem description:

> You have a bowl of letters (Alphabet soup).
> Please write a method that outputs how many times you would be able to spell PENNYMAC from the letters in the bowl.
> If you are unable to spell it, please return 0

---

Assumptions: 

1. both search term and bowl are strings
2. both search term and bowl are treated as case-sensitive
3. every char from the bowl only can be used once

The solution is based on calculating character frequencies for the search term and the bowl.
Given these histograms, it's possible to build the search term at least once if:

1. Every char of the search term must be present in the bowl, and 
2. the amount of times it occurs in the bowl must be greater or equal to the amount of times it occur in the search term 

Knowing that, it's simple to calculate how many times the search term can be formed: we divide the frequency of each char in the bowl by the frequency of the same char in the search term and build an array out of these values. The smallest item will represent the maximum times the search term can be formed from the bowl's chars