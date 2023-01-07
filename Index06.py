def main(s):
    """
    A string variable consisting of several characters is given. Add and return the first and last character.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    x=s[0]
    y=s[-1]
    s=x+y
    return s
print(main('1gucdudv1'))