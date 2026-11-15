"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

import random  # needed for the random dataset


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Linear search examines each element sequentially.
    # In the worst case it looks at every item - O(n) time.
    for index, value in enumerate(lst):
        if value == target:          # Found the target; return its position.
            return index
    return -1                       # Target not present after examining all items.



def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    low = 0
    high = len(lst) - 1

    # Each loop cuts the remaining range in half - O(log n) time.
    while low <= high:
        mid = (low + high) // 2          # Middle index of current range.
        mid_val = lst[mid]

        if mid_val == target:            # Target found.
            return mid
        elif mid_val < target:           # Target must be in the right half.
            low = mid + 1
        else:                            # Target must be in the left half.
            high = mid - 1

    return -1                             # Target not found default -1 



def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    small_dataset = [3, 8, 15, 23, 42]

    # Test searches for an existing value
    existing_val = 23
    lin_idx = linear_search(small_dataset, existing_val)
    bin_idx = binary_search(small_dataset, existing_val)
    print(f"Searching for existing value {existing_val}:")
    print(f"  Linear Search - index {lin_idx} (found)" if lin_idx != -1 else "  Linear Search - not found")
    print(f"  Binary Search - index {bin_idx} (found)" if bin_idx != -1 else "  Binary Search - not found")

    # Test searches for a missing value
    missing_val = 7
    lin_idx = linear_search(small_dataset, missing_val)
    bin_idx = binary_search(small_dataset, missing_val)
    print(f"\nSearching for missing value {missing_val}:")
    print(f"  Linear Search - {'not found' if lin_idx == -1 else f'index {lin_idx} (incorrect)'}")
    print(f"  Binary Search - {'not found' if bin_idx == -1 else f'index {bin_idx} (incorrect)'}")

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    # 1. Random sorted dataset with 50 elements (mirrors the small dataset size but is larger)
    random.seed(0)                          # make the result reproducible
    large_dataset = sorted(random.sample(range(1, 101), 50))
    print(f"Dataset (50 sorted random numbers): {large_dataset}")

    # 2. Search for an existing value (choose one from roughly the middle of the list)
    middle_index = len(large_dataset) // 2   # programmatic “half” of the list
    existing_large = large_dataset[middle_index]
    lin_idx = linear_search(large_dataset, existing_large)
    bin_idx = binary_search(large_dataset, existing_large)
    print(f"\nSearching for existing value {existing_large}:")
    print(f"  Linear Search - index {lin_idx}")
    print(f"  Binary Search - index {bin_idx}")
    # Comment: Even with only 50 items, linear search may need to look at many entries,
    # while binary search finishes in a handful of comparisons.

    # 3. Search for a missing value (pick a number guaranteed not to be in the list)
    missing_large = 101                     # outside the range used for sampling
    lin_idx = linear_search(large_dataset, missing_large)
    bin_idx = binary_search(large_dataset, missing_large)
    print(f"\nSearching for missing value {missing_large}:")
    print(f"  Linear Search - {'not found' if lin_idx == -1 else f'index {lin_idx} (incorrect)'}")
    print(f"  Binary Search - {'not found' if bin_idx == -1 else f'index {bin_idx} (incorrect)'}")
    # Comment: Binary search’s advantage is evident even on a modestly sized list.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: Empty list
    empty_list = []
    print("\nEdge case - empty list:")
    print("  Linear Search -", linear_search(empty_list, 10))
    print("  Binary Search -", binary_search(empty_list, 10))
    # Both return -1 because there is nothing to search.

    # Edge case 2: Single-element list (target present)
    single_present = [42]
    print("\nEdge case - single-element list, value present (42):")
    print("  Linear Search -", linear_search(single_present, 42))
    print("  Binary Search -", binary_search(single_present, 42))
    # Both return index 0; binary search works with low == high.

    # Edge case 4: Value at first position
    first_pos = [5, 12, 19, 27]
    print("\nEdge case - value at first position (5):")
    print("  Linear Search -", linear_search(first_pos, 5))
    print("  Binary Search -", binary_search(first_pos, 5))

    # --------------------------------------------------------------
    # Real‑world contact‑list scenario
    # --------------------------------------------------------------
    #
    # Imagine a phone’s address book. If contacts are stored in the order
    # you entered them (unsorted), you can only perform a linear search.
    # Sorting the list once lets you use binary search, which is far faster
    # for repeated look‑ups. The code below measures the number of
    # examined elements for each approach to illustrate the preparation
    # vs. speed trade‑off.

    contacts_unsorted = [
        "Zoe Patel", "Aaron Smith", "Mia Chen", "Liam O'Neil",
        "Emily Davis", "Noah Brown", "Olivia Wilson", "Ethan Garcia",
        "Sophia Martinez", "Lucas Kim"
    ]
    target_name = "Emily Davis"

    # ---- Linear search on the unsorted phonebook ----
    lin_steps = 0
    for i, name in enumerate(contacts_unsorted):
        lin_steps += 1
        if name == target_name:
            lin_index = i
            break
    else:
        lin_index = -1

    # ---- Sort the contacts (pre‑search preparation) ----
    contacts_sorted = sorted(contacts_unsorted)

    # ---- Binary search on the sorted phonebook ----
    low, high, bin_steps = 0, len(contacts_sorted) - 1, 0
    while low <= high:
        bin_steps += 1
        mid = (low + high) // 2
        if contacts_sorted[mid] == target_name:
            bin_index = mid
            break
        elif contacts_sorted[mid] < target_name:
            low = mid + 1
        else:
            high = mid - 1
    else:
        bin_index = -1

    print("\n--- Real‑World Contact Search Scenario ---")
    print(f"Unsorted contacts: {contacts_unsorted}")
    print(f"Target name: '{target_name}'")
    print(f"Linear search -> index {lin_index}, steps examined = {lin_steps}")
    print(f"Sorted contacts:   {contacts_sorted}")
    print(f"Binary search -> index {bin_index}, steps examined = {bin_steps}")



if __name__ == "__main__":
    main()