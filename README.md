# Interview Preparation

## LeetCode Problems:

### Arrays & Strings

| Name |  Solution | Level | Notes |
|---|----------------|---|---|
[Boats to Save People](https://leetcode.com/problems/boats-to-save-people/)| [Link](https://github.com/dkarakay/interview/blob/main/leetcode/arrays-strings/boats_to_save_people.py) | Medium | Sort the list and check elements from the beginning and end
[Container with Most Water](https://leetcode.com/problems/container-with-most-water/)| [Link](https://github.com/dkarakay/interview/blob/main/leetcode/arrays-strings/container_with_most_water.py) | Medium | Finding max area by checking elements from two sides of array. max(temp,max_area). If height[left] < height [right] increase left
[Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)| [Link](https://github.com/dkarakay/interview/blob/main/leetcode/arrays-strings/find_first_and_last_position_of_element_in_sorted_array.py) | Medium | Write two functions one for finding first pos, other one is for finding last pos. Use binary search
[First Bad Version](https://leetcode.com/problems/first-bad-version/)| [Link](https://github.com/dkarakay/interview/blob/main/leetcode/arrays-strings/first_bad_version.py) | Easy | Sorted array find value just like binary search
[Longest Substring without Repeating Elements](https://leetcode.com/problems/longest-substring-without-repeating-elements/)|[Link](https://github.com/dkarakay/interview/blob/main/leetcode/arrays-strings/longest_substring_without_repeating_elements.py) | Medium | Use two pointers and dict
[Move Zeroes](https://leetcode.com/problems/move-zeroes/)|[Link](https://github.com/dkarakay/interview/blob/main/leetcode/arrays-strings/move_zeroes.py) | Easy | Two for loops; one of them is for overwriting all elements by non-zero elements, the other one is for adding zeroes

### Linked Lists

| Name |  Solution | Level | Notes |
|---|----------------|---|---|
[Add Two Numbers](https://leetcode.com/problems/add-two-numbers)| [Link](https://github.com/dkarakay/interview/blob/main/leetcode/linked/add_two_numbers.py)| Medium | Estimate depth, calculate number itself, sum them up, return -1. Use carry approach simple, easy. [My explanation on Leetcode](https://leetcode.com/problems/add-two-numbers/discuss/1472944/Python-3-or-Faster-than-90-or-Elegant-and-simple-approach)
[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)| [Link](https://github.com/dkarakay/interview/blob/main/leetcode/linked/linked_list_cycle.py)| Easy | Initialize two pointers, move one of them by 1, other one by 2. If there is a cycle, eventually those two pointers show the same value. Tortoise & Hare, Floyd's algorithm [My explanation on Leetcode](https://leetcode.com/problems/linked-list-cycle/discuss/1472834/python-3-tortoise-hare-easy)
[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)| [Link](https://github.com/dkarakay/interview/blob/main/leetcode/linked/merge_two_sorted_lists.py)| Easy | Compare two elements at the same time, add rest of them
[Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)| [Link](https://github.com/dkarakay/interview/blob/main/leetcode/linked-lists/reverse_linked_list.py)| Easy | Utilize iteration method to reverse linked list. Use three pointers prev,head and next and change head's next position to prev and update each element's place.

### Maps

| Name |  Solution | Level | Notes |
|---|----------------|---|---|
[4Sum II](https://leetcode.com/problems/4sum-ii/)| [Link](https://github.com/dkarakay/interview/blob/main/leetcode/maps/4sum_ii.py)| Medium | The first two elements' sum must equal to (-1) of last two elements' sum
[Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)| [Link](https://github.com/dkarakay/interview/blob/main/leetcode/maps/contains_duplicate.py) | Easy | Sets. [My explanation on Leetcode](https://leetcode.com/problems/contains-duplicate/discuss/1457561/python-one-line-solution-easy)
[Group Anagrams](https://leetcode.com/problems/group-anagrams/)| [Link](https://github.com/dkarakay/interview/blob/main/leetcode/maps/group_anagrams.py) | Medium | Sort strings and use them as keys
[LRU Cache](https://leetcode.com/problems/lru-cache/)| [Link](https://github.com/dkarakay/interview/blob/main/leetcode/maps/lru_cache.py) | Hard | Use Deque and Map to find solution
[Majority Element](https://leetcode.com/problems/majority-element/)| [Link](https://github.com/dkarakay/interview/blob/main/leetcode/maps/majority_element.py) | Easy | Count the occurrence of items solve the question
[Two Sum](https://leetcode.com/problems/two-sum/)| [Link](https://github.com/dkarakay/interview/blob/main/leetcode/maps/two_sum.py) | Medium | Use remaining  number as a key. If you need to have 9, check remaining values 7,5,3 for 2,4,6 respectively. If you find the same remaining value in your list, you are done.

### Math

| Name |  Solution | Level | Notes |
|---|----------------|---|---|
[Add Binary](https://leetcode.com/problems/add-binary/)| [Link](https://github.com/dkarakay/interview/blob/main/leetcode/math/add_binary.py) | Medium | Check binary rules
[Count Primes](https://leetcode.com/problems/count-primes/)| [Link](https://github.com/dkarakay/interview/blob/main/leetcode/math/count_primes.py) | Easy | Boolean array, iterate 2..sqrt(2) and set n*n
[Missing Number](https://leetcode.com/problems/missing-number/)|[Link](https://github.com/dkarakay/interview/blob/main/leetcode/math/missing_number.py)| Easy | (n * (n + 1))/ 2
[Robot Return to Origin](https://leetcode.com/problems/robot-return-to-origin/)| [Link](https://github.com/dkarakay/interview/blob/main/leetcode/math/robot_return_to_origin.py) | Easy | Calculate X & Y coordinate seperately
[Single Number](https://leetcode.com/problems/count-primes/)|[Link](https://github.com/dkarakay/interview/blob/main/leetcode/math/single_number.py) | Easy | Use sets, subtract 2*(set_version) from original one

## inzva

### Algorithm Training Beginner Set

| Problem & Solution  |
|---|
|[Ice Cream Yum Yum](https://github.com/dkarakay/interview/blob/main/inzva/algorithm-training-beginner-set/ice_cream_yum_yum.py)|
|[Harun & Sami](https://github.com/dkarakay/interview/blob/main/inzva/algorithm-training-beginner-set/harun_sami.py)|
|[Hopscotch](https://github.com/dkarakay/interview/blob/main/inzva/algorithm-training-beginner-set/hopscotch.py)|
|[Stringer Things](https://github.com/dkarakay/interview/blob/main/inzva/algorithm-training-beginner-set/stringer_things.py)|
|[Stickers](https://github.com/dkarakay/interview/blob/main/inzva/algorithm-training-beginner-set/stickers.py)|
|[Usain Bolt](https://github.com/dkarakay/interview/blob/main/inzva/algorithm-training-beginner-set/usain_bolt.py)|
|[The Pit](https://github.com/dkarakay/interview/blob/main/inzva/algorithm-training-beginner-set/the_pit.py)|

## Data Structures

| Name |  Example | Notes |
|---|----------------|---|
[Doubly Linked List](https://www.geeksforgeeks.org/data-structures/linked-list/doubly-linked-list/) | [Link](https://github.com/dkarakay/interview/blob/main/data-structures/doubly_linked_list.py) | Next and previous
[Singly Linked List](https://www.geeksforgeeks.org/data-structures/linked-list/singly-linked-list/) | [Link](https://github.com/dkarakay/interview/blob/main/data-structures/singly_linked_list.py) | Only next Insertion & Deletion O(1)

## Algorithms

| Name |  Example | Notes |
|---|----------------|---|
[Binary Search](https://en.wikipedia.org/wiki/Binary_search_algorithm) | [Link](https://github.com/dkarakay/interview/blob/main/algorithms/binary_search.py) | Must be sorted, Divide the array by 2 and iterate
[Sliding Window](https://www.geeksforgeeks.org/window-sliding-technique/) | [Link](https://github.com/dkarakay/interview/blob/main/algorithms/sliding_window.py) 
