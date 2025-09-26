from collections import deque

"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""


def has_duplicates(product_ids):

    seen = set()

    for i in product_ids:
        if i in seen:
            return True
        seen.add(i)
    return False

#Example Usage
example_input = [1, 2, 3]
print(has_duplicates(example_input))

example2_input = [1, 2, 3, 2, 3]
print(has_duplicates(example2_input))

"""
(1) Why this data structure fits the task  
This data structure fits the task because it only stores unique values is faster to check through.


(2) what operations are performed and their expected runtime
For each loop, adding an element and checking elements in the set are 
performed when looking through the set and its runtime is O(n) for these tasks.
"""

"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    def __init__(self):
        self.tasks = deque()

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added {task}")

    def remove_oldest_task(self):
        if self.tasks:
            return self.tasks.popleft()
        else:
            print("List is Empty")
            return None

#Example Usage
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
print("Removed:", task_queue.remove_oldest_task()) # "Email follow-up"

"""
(1) Why this data structure fits the task  
A queue fits this task because we are mostly working with the front.

(2) what operations are performed and their expected runtime
Adding a value using append, the runtime is O(1) 
and removing a value using popleft, the runtime is O(1).
Meaning overall, it would be O(n).
"""


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:

    def __init__(self):
        self.my_set = set()
        
    def add(self, value):
        self.my_set.add(value)


    def get_unique_count(self):
        return len(self.my_set)

#Example Usage
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
print(tracker.get_unique_count()) #2

"""
(1) Why this data structure fits the task  
Using a set works because we are only looking at unique values. 

(2) what operations are performed and their expected runtime
Adding values using add and printing the number of unique values. 
Both run in O(1) time. 
"""