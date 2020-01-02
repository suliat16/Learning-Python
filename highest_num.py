def highest_num_div3(l):
    """Given a list of numbers, returns the highest number divisible by 3.
    Note: There is an edge case that this code fails.
    Requires: input is a non-empty list with digits from 0-9"""
    import itertools
    def sort_list(slist):
        new_list = []
        length = len(slist)
        for i in range(length):
            if not new_list:
                new_list.append(slist[i])
                continue
            for j in range(len(new_list)):
                if slist[i] > new_list[j]:
                    new_list.insert(j, slist[i])
                    break
                elif j == (len(new_list)- 1):
                    new_list.append(slist[i])
                else:
                    continue
        return new_list

    def list_to_num(numlist):
        length = len(numlist)
        new_string= ""
        for i in range(length):
            num =  str(numlist[i])
            new_string = new_string + num
        new_num = int(new_string)
        return new_num

    def heap_permutation(num):
        def _heap_permutation(num, size):
            if (size == 1):
                # I dont understand why this next line fixed my issue- that bit was stack exchange witchcraft. 
                num = num[:]
                yield num
            else: 
                for i in range(size):
                    for perm in _heap_permutation(num, size-1):
                        yield perm
                    if size%2 ==1:
                        num[0], num[size-1] = num[size-1], num[0]
                    else: 
                        num[i], num[size-1] = num[size-1], num[i]

        size = len(num)
        new_list = []
        for value in _heap_permutation(num, size):
            new_list.append(value)
        return new_list

    def list_output(thelist):
        sorted_list = sort_list(thelist)
        length= len(thelist)
        for i in range(length):
            front_list = sorted_list[:i]
            end_list = sorted_list[i:]
            end_list_perm = heap_permutation(end_list)
            sorted_perm = [front_list + value for value in end_list_perm]
            for value in sorted_perm:
                code = list_to_num(value)
                if code % 3 ==0:
                    return code

    def output(thelist):
        first_try = list_output(thelist)
        if first_try is not None:
            return first_try
        else:
            length = len(thelist)
            if length == 1:
                return 0
            for i in range(length-1,0,-1):
                for value in itertools.combinations(thelist, i):
                    next_try = list_output(value)
                    if next_try is not None:
                        return next_try
                if i == 1:
                    return 0
    return output(l)
