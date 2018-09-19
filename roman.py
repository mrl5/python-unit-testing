'''Convert to and from Roman numerals

This program is part of 'Dive Into Python 3', a free Python book for
experienced programmers.  Visit http://diveintopython3.org/ for the
latest version.
'''


class OutOfRangeError(ValueError):
    pass


class NotIntegerError(ValueError):
    pass


class InvalidRomanNumeralError(ValueError):
    pass


roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))


def to_roman(n):
    '''convert integer to Roman numeral'''
    # modified by mrl5
    if not isinstance(n, int):
        raise NotIntegerError('non-integers can not be converted')
    if not (0 < n < 4000):
        raise OutOfRangeError('number out of range (must be 1..3999)')
    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
            # show what's going on
            # print('subtracting {0} from input, adding {1} to output'.format(integer, numeral))
    return result


def from_roman(s):
    '''convert Roman numeral to integer'''
    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        while s[index: index + len(numeral)] == numeral:
            result += integer
            index += len(numeral)
            # show what's going on
            # print('found', numeral, 'of length', len(numeral), ', adding', integer)
    return result


# Copyright (c) 2009, Mark Pilgrim, All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS'
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
