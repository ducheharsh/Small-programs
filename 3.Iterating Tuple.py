def get_data (aTuple):
    nums = ()
    words = ()
    for t in aTuple :
        nums += (t[0], )
        if t[1] not in words:
            words += (t[1], )
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return(min_n, max_n, unique_words)        

print(get_data(((21,"sam"),(44, "cool"),(69, "oops"))))

def get_guessed (aList):
    return

print(get_guessed([2,3,22,222]))