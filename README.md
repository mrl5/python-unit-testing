# [Unit Testing]
Examples from chapter 9 of [Dive Into Python 3] by [Mark Pilgrim]

>Unit testing is an important part of an overall testing-centric development strategy. If you write unit tests, it is important to write them early and to keep them updated as code and requirements change. Many people advocate writing tests before they write the code they’re testing (...) unit tests are beneficial no matter when you write them.

>A test case should be able to
>- run completely by itself, without any human input. Unit testing is about automation.
>- determine by itself whether the function it is testing has passed or failed, without a human interpreting the results.
>- run in isolation, separate from any other test cases (even if they test the same functions). Each test case is an island

>A unit test actually has three return values:
- **pass**: means that the test passed — the code did what you expected.
- **fail**: test case executed the code but the result was not what you expected.
- **error**: means that the code didn't even execute properly.

## TL;DR - the Test
`python3 romantest.py`

## Introduction to the task 1
>Let’s start mapping out what a roman.py module should do. It will have two main functions, `to_roman()` and `from_roman()`. The `to_roman()` function should take an integer from 1 to 3999 and return the Roman numeral representation as a string

### Task 1
>Write a test case that checks whether the `to_roman()` function does what you want it to. You read that right: you’re going to write code that tests code that you haven’t written yet.

## Introduction to the task 2
>Converting a string from a Roman numeral to an integer.

### Task 2
Write a test case that checks whether the `from_roman()` function does what you want it to.

## End notes
>It is theoretically possible that `to_roman()` has a bug that produces the wrong Roman numeral for some particular set of inputs, and that `from_roman()` has a reciprocal bug that produces the same wrong integer values for exactly that set of Roman numerals that `to_roman()` generated incorrectly.

>Depending on your application and your requirements, this possibility may bother you; if so, write more comprehensive test cases until it doesn't bother you.


[Unit Testing]: http://www.diveintopython3.net/unit-testing.html
[Dive Into Python 3]: http://www.diveintopython3.net/
[Mark Pilgrim]: https://github.com/diveintomark

