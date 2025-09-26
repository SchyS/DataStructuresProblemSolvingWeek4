# Pick one question from timed_challenge.txt
# Paste the question as a comment below
"""
Return the first value that repeats in the collection.
Input: [1, 4, 3, 5, 3, 2, 1]
Output: 3
"""
# Set a timer for 30 minutes and complete the question!

def first_value(values):

    seen = set()

    for i in values:
        if i in seen:
            #Return i if it already exists in set
            return i
        seen.add(i)
    #If no values or not duplicate values, return None
    return None

#Test cases
my_list = [1, 4, 3, 5, 3, 2, 1]
print(first_value(my_list))

my_list_1 = [1, 4, 3, 5, 6, 7, 8]
print(first_value(my_list_1))

my_list_2 = []
print(first_value(my_list_2))

my_list_3 = ["Hello"]
print(first_value(my_list_3))
"""
What structure you chose and why?
For this timed challenge I chose to use a set. Originally I had used a list but realized I 
just needed to return a value and not store the entire list. Changing from a list to a set
results in a faster time complexity because when using a set each operation is in O(1) so 
the overall time complexity is O(n). If I were to use a list the time complexity would be
O(n^2) worst case because "if i in seen" would change from O(1) to O(n) where n is the length
of the list.

How the time limit shaped your decision?
The time limit did not really effect my decision. Originally I felt I was going to be more rushed
but I had initially wrote it in a list. After some reflection on the code I had time to change
it to a set which I thought would be better and still had plenty of time to spare. 

What trade-offs or compromises you made under time pressure?
The only trade-off or compromise I had was realizing that I was not as rushed or under as 
much of a time constraint then I had thought. Slowing down and taking my time to really think 
of the problem and how to best solve it allowed me to come up with a better solution in the end.
"""