def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counter = {}
    for number in nums:
        counter[number] = counter.get(number, 0) + 1
    biggestNumber = max(counter.values())
    for (number, times) in counter.items():
        if times == biggestNumber:
            return number