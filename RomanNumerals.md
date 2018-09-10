# Roman numerals rules (from [DiveIntoPython3])

## The rules for Roman numerals \[[1]\]

>In Roman numerals, there are seven characters that are repeated and combined in various ways to represent numbers.
>- I = 1
>- V = 5
>- X = 10
>- L = 50
>- C = 100
>- D = 500
>- M = 1000

>The following are some general rules for constructing Roman numerals
>- Sometimes characters are additive. I is 1, II is 2, and III is 3. VI is 6 (literally, “5 and 1”), VII is 7, and VIII is 8.
>- The tens characters (I, X, C, and M) can be repeated up to three times. At 4, you need to subtract from the next highest fives character. You can't represent 4 as IIII; instead, it is represented as IV (“1 less than 5”). 40 is written as XL (“10 less than 50”), 41 as XLI, 42 as XLII, 43 as XLIII, and then 44 as XLIV (“10 less than 50, then 1 less than 5”).
>- Sometimes characters are… the opposite of additive. By putting certain characters before others, you subtract from the final value. For example, at 9, you need to subtract from the next highest tens character: 8 is VIII, but 9 is IX (“1 less than 10”), not VIIII (since the I character can not be repeated four times). 90 is XC, 900 is CM.
>- The fives characters can not be repeated. 10 is always represented as X, never as VV. 100 is always C, never LL.
>- Roman numerals are read left to right, so the order of characters matters very much. DC is 600; CD is a completely different number (400, “100 less than 500”). CI is 101; IC is not even a valid Roman numeral (because you can't subtract 1 directly from 100; you would need to write it as XCIX, “10 less than 100, then 1 less than 10”).


## Interesting observations \[[2]\]

>The rules for Roman numerals lead to a number of interesting observations:
>- There is only one correct way to represent a particular number as a Roman numeral.
>- The converse is also true: if a string of characters is a valid Roman numeral, it represents only one number (that is, it can only be interpreted one way).
>- There is a limited range of numbers that can be expressed as Roman numerals, specifically 1 through 3999. The Romans did have several ways of expressing larger numbers, for instance by having a bar over a numeral to represent that its normal value should be multiplied by 1000. For the purposes of this chapter, let’s stipulate that Roman numerals go from 1 to 3999.
>- There is no way to represent 0 in Roman numerals.
>- There is no way to represent negative numbers in Roman numerals.
>- There is no way to represent fractions or non-integer numbers in Roman numerals.

[DiveIntoPython3]: http://www.diveintopython3.net/
[1]: http://www.diveintopython3.net/regular-expressions.html#romannumerals
[2]: http://www.diveintopython3.net/unit-testing.html#divingin