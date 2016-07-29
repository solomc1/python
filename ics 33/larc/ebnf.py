Write an EBNF description for time in the format HH:MM, am/pm suffix is optional


non-zero-digit <= 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
hour <= 1 0 | 1 | 2   | non-zero-digit
minutes <= 0 | 1 | 2 | 3 | 4 | 5 non-zero-digit

time <= hour : minutes [a|p m]
------------


General Rule of Matching:
  Regular expressions match the most number of characters possible (called a
  greedy algorithm; there are patterns that match the fewest number of
  characters possible; we will discuss but we will not use those patterns).

Matching:
  Characters generally match themselves, except for the following...

Metacharacters
 .  Matches any single character exception (newline: \n)
 [] Matches one character specified in []; e.g., [aeiou]
 [^]    Matches one character NOT specified in [] after ^; e.g., [^aeiouy]
 -      Matches one character in range in []: e.g., [0-9] matches any digit

Patterns (like EBNF right-hand sides): R, Ra, Rb are regular expression patterns
 RaRb   Matches a sequence of Ra followed by Rb (like sequence in EBNF)
 Ra|Rb  Matches either alternative Ra or Rb (like alternative in EBNF)
 R? Matches regular expression R 0/1 time: R is optional (like [] in EBNF)
 R* Matches regular expression R 0 or more times (like {} in EBNF)
 R+ Matches regular expression R 1 or more times
 R{m}   Matches regular expression R exactly m times: e.g., R{5} = RRRRR
 R{m,n} Matches regular expression R at least m and at most n times:
          R{3,5} = RRR|RRRR|RRRRR = RRR[R][R]

 R??,R*?,R+?,R{m,n}? The postfix ? means match as few characters possible (not
the most, so not greedy). We will not use these patterns.

Parentheses/Parenthesized Patterns
 Parentheses are used for grouping, but also to specify remembered subpatterns
 By placing subpattern R in parentheses, the text matching R will be remembered
 (either by its number, starting at 1, or its name, if named) in a group, for
 use later in the pattern or when extracting information from the matched
 text.

 (R)         Matches R and delimits a group (1...) (remembers matched substring)
 (?P<name>R) Matches R and delimits group (remembering matched substring)
               using name for the group (it is still numbered as well); see
               (?P=name) and groupdict method below
 (?:R)       Matches R but does not delimit a group (not remembered)

 (?P=name)   Matches remembered group(substring) named name for backreferencing

 (?=R)       Matches R and delimits group, but does not consume input match
 (?!R)       Matches anything but R and does not consume input needed for match
               (hint: != means "not equal", ?!R means "not matching R)

Anchors (these don't match characters)
 ^  beginning of line
         (when not used in [], which means "match any other characters")
 $  end of line

Context
  - not in [] and not between two characters means - (itself)
 Special characters are treated as themselve in []
 Generally, if interpretting a character makes no sense one way, try to find
   another way to interpret it that fits the context

Escape Characters with Special Meanings
 \  Used before .|[]-?*+{}()^$\ (and others) to specify a special character
 \#     Backreferencing group # (numbered from 1, 2, ...): see (R) above
 \t tab
 \n newline
 \r carriage return
 \f formfeed
 \v vertical tab

 \d [0-9]           Digit
 \D [^0-9]          non-Digit
 \s [ \t\n\r\f\v]       White space
 \S [^ \t\n\r\f\v]      non-White space
 \w [a-zA-Z0-9_]        alphabetic (or underscore): Word character
 \W [^a-zA-Z0-9_]       non non alphabetic: non-Word character


Interesting Equivalences
 a(b|c)d  ==    a[bc]d      if b and c are single characters
 R{0,1}   ==    R?
 [ \t]*   == ( |\t)*        but is different from ( *|\t*)
