def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a>0 and a%2!=0:
        return "positive odd number"
    if a>0 and a%2==0:
        return "positive even number"
    if a<0 and a%2!=0:
        return "negative odd number"
    if a<0 and a%2==0:
        return "negative even number"
    return  "the number is zero"
print(main(12))
print(main(13))
print(main(-12))
print(main(-13))
print(main(0))