# The mathematical term symmetric difference (△) of two sets is the set of elements which are in either of the two sets but not in both.
# For example, for sets A = {1, 2, 3} and B = {2, 3, 4}, A △ B = {1, 4}.
# Symmetric difference is a binary operation, which means it operates on only two elements. So to evaluate an expression involving
# symmetric differences among three elements (A △ B △ C), you must complete one operation at a time. Thus, for sets A and B previously,
# and C = {2, 3}, A △ B △ C = (A △ B) △ C = {1, 4} △ {2, 3} = {1, 2, 3, 4}.

# Create a function that takes two or more sets and returns a set of their symmetric difference. The returned set must contain only
# unique values (no duplicates).


def find_symmetric_difference(*sets):
    # Import doubly-ended queue
    from collections import deque
    # set_collection is a deque list of sets
    set_collection = deque(sets)
    # Exclude the last index to avoid indexing error when performing symmetric difference
    for x in range(len(set_collection) - 1):
        # Copy the resulting set
        symmetric_difference = (set_collection[0] ^ set_collection[1]).copy()
        # Remove the first 2 sets after symmetric operation
        for i in range(2):
            set_collection.popleft()
        # Add the resulting set as the first set into deque
        set_collection.appendleft(symmetric_difference)
    return set_collection[0]
