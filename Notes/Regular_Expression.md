# Regular Expression
- A regular expression is a string which contains
  - special symbol
  - Characters to find out
  - extract the information needed by us from the given data
- A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern
- Python has a built-in package called **re**, which can be used to work with Regular Expressions.
#### Regular Expression helps us
  - to search
  - to match
  - to find out
  - to split information as per our requirements 
#### RegEx Functions
- findall
  - returns a list containing all matches
- search:
  - Returns a Match object of the first occurrence if there is a Match anywhere in the string
- match:
  -  Returns a Match object of the beginning match if there is a Match in the string or return None
-  split
  - Returns a list where the string has been split at each match
- sub
  - Replaces one or many matches with a string
## Sequence Characters in Regular Expression
1. \d - any digit from 0 to 9
2. \D - any non- digit
3. \s - white space charcters e.g,: \t, \n, \r, \v, \f
4. \S - non-white space character
5. \w - any alpha-numeric character
6. \W - any non-alphanumeric character
7. \b - represents a space around words
8. \A - Matchers only at the start of the string
9. \Z - matches only at the end of the string

#### Characters represent more than one character to be matched in the string is called Quantifiers
1. + => represents 1 or more repetitions of the preceding regex
2. * => 0 or more repetitions of the preceding regex
3. ? => 0 or 1 repetitions of the preceding regex
4. {m} => exactly m occurrences
5. {m,n} => from m to n, default n to infinity, always goes for higher bound i.e, n and then m
#### Special Characters in regex:
1. \ => Escape special character
2. - => matches any character except new line
3. ^ => matches beginning of the string
4. $ => matches the ending of the string
5. [...] => Denotes set of possible characters. e.g:[6,p...t] matches any character from 6,p,r,s,t.
6. [^...] => Matches every character except typed characters inside the brackets.
7. (....) => matches the regular expression inside the parenthesis and the result can be captured
8. R|s => matches the regex either R regex or s regex
#### syntax:
- import re
- string = "   "
-  pattern = " "
-  re.findall(pattern,string)
