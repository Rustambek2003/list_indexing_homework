def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    i = 0
    a = list1[0]
    while i < len(list1):
        if a != list1[i]:
            return False
        else:
            i += 1
    return True
            
print(main([0, 0, 0, 0, 0]))