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
    if a == list1[1] and a == list1[2] and a == list1[3] and a == list1[4]:
        return True
    else:
        return False

print(main([0, 0, 0, 0, 0]))