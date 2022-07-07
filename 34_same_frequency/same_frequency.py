def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    counter1 = {}
    counter2 = {}
    for i in str(num1)
        counter1[i] = counter1.get(i, 0) + 1
    for j in str(num2)
        counter2[j] = counter2.get(j, 0) + 1
    return counter1 == counter2