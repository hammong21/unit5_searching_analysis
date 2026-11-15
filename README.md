# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.


## My Reflection

During this assignment I deepened my understanding of algorithmic complexity and learned how to implement two fundamental searching techniques in Python. Writing linear search reinforced the idea of scanning each element sequentially and its linear time cost. Building binary search required managing low, high, and mid indices to achieve logarithmic performance and added the insight that sorting the data once can dramatically speed up repeated lookups. I also practiced adding clear explanatory comments and integrating a realistic example of searching contacts on a phone to illustrate the impact of data organization.

The main challenge was fitting the real‑world contact scenario into the existing TODO sections without breaking the script. I solved this by treating the contact lookup as part of the large dataset block, using the same search functions and counting the steps each algorithm examined. Ensuring that edge cases such as empty lists and single‑element lists behaved correctly required extra testing and careful handling of index boundaries.

Linear search is appropriate when data are unsorted, when a single scan is sufficient, or when the collection cannot be indexed efficiently, such as streaming logs. Binary search should be used when the dataset is sorted and supports random access, because the initial sorting effort is amortized over many queries, providing much faster retrieval in large static collections like contact lists, music libraries, or product inventories. The tradeoff is preparation time versus query speed.