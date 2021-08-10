# Happy-Number-Checker
Function for checking if a number is a happy number or not
A happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit.

## Functions

is_happy checks if a number is a happy number, number must be positive integer.

digit_sum which adds the digits with the given power in the case of is_happy power is 2. 

## Memorisation

In order to speed up calculations happy and unhappy numbers there is a dicitionary which stores
values that have been encountered and whether they were happy numbers or not.
This can cause a MemoryError an large ranges.

### Comparison
Average of 4 done
NoMemorisation: 1 million numbers 0:00:05.963927, 10 Million numbers 0:01:12.349710
Memorisation: 1 Milltion Numbers 0:00:03.191423, 10 Million numbers 0:00:44.858039

## Optimisations
When doing happy numbers on base 10 when checking a number with 12 digits or less you only need
know the happy numbers from 1000 and below and the max digit sum is 972 = 9^2 * 12 .


Was also looking at looking at ways of keeping a rolling sum of digits in order to speed up calculations.
So far I've been able to do it so that 10 consecutive numbers can have a rolling sum
+ 11 -> 2
+ 12 -> 2 + 3 -> 5
However it must be reset after 9 as this causes a second digit to change.