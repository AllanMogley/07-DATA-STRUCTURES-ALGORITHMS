def brute_force(text, pattern):

    # get length of text and pttern
    # set looping varibles to zero
    # set a condition if no pattern found

    l1 = len(text)
    l2 = len(pattern)
    i = j = 0
    flag = False

    # iterate through index in i
    # cheack if there is a match in text/pattern index values
    # add result to count if thr condition is passed

    while i < l1:
        j = 0
        count = 0

        while j < l2:
            if i + j < l1 and text[i + j] == pattern:
                count += 1
            j += 1

        if count == l2:
            print('\nPattern occurs at index: ', i)
            flag = True

    if not flag:
        print('\nPattern is not at all present in the array!')



brute_force('acbcabccababcaacbcac','acbcac')

