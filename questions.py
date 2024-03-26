# Question 1
def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices
    of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.
    You can return the answer in any order.
    Args:
    nums (List[int]): List of integers.
    target (int): Target sum.

    Returns:
    List[int]: Indices of the two numbers that add up to the target.
    """
    numset = set(nums)
    for i,x in enumerate(nums):
        y = target - x
        if y in numset and y != x:
            j = nums.index(y, i+1)
            ret = [i,j]
            return ret
    # if we get here, the answer must be a duplicate because each test case is guaranteed to have one correct answer
    val = target // 2
    ret = [i for i,x in enumerate(nums) if x == val]
    return ret

# Question 2
def is_valid_parenthesis(s):
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    An input string is valid if:
    1. Open brackets are closed by the same type of brackets.
    2. Open brackets are closed in the correct order.

    Args:
    s (str): Input string.

    Returns:
    bool: True if the string is valid, False otherwise.
    """
    openers = '([{'
    opener_for = {
            ')':'(',
            ']':'[',
            '}':'{'
    }
    opens = []
    for c in s:
        if c in openers:
            opens.append(c)
        else:
            if len(opens) == 0:
                return False
            elif opens[-1] == opener_for[c]:
                opens.pop()
            else:
                return False
    return True
