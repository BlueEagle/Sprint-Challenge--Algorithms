#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n^3)
This is O of n cubed since the statement in the while loop has to run until it has met that factor of the input.

b) O(n log n)
This is two loops, which both require looping through the input n. The second loop will grow exponentially closer to n with each iteration.

c) O(n)
This recursive function will grow linearly with the input.

## Exercise II

NOTES-----------------
stories = n
eggs = 3
if thrown_floor >= f:
eggs -= 1

---

Reducing the number of dropped eggs may not be possible as that may not be a variable under our control.

I can change the floor f to be higher, so the amount of broken eggs is reduced.

If given the amount of stories of the building, I would set floor f to the highest story possible.

Without knowing the amount of stories, it may be safe to assume there is at least one, if there is a place to drop an egg from.

floor f = 1 # or stories[-1], if this exists.
while(eggs_are_being_thrown):
if last_floor_dropped_from > floor:
floor = last_floor_dropped_from

This is O(n).
