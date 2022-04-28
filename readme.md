# Overview

experiment with different ways to parse and generate ast with optimal speed & memory. 
All of these below parse Python3.10 grammar. 

| module                   | total allocated size | time  | peak       |
|--------------------------|----------------------|-------|------------|
| pgen2                    | 369KiB               | 0.08s | 684KiB     |
| pegen + regex(tokenizer) | 1767KiB              | 0.32s | 2015KiB    |
| pegen                    | 1234KiB              | 0.38s | 2281.9KiB  |
| xonsh-ply                | 8240.6 KiB           | 0.65s | 10333.5KiB |
| parso                    | 3542.7 KiB           | 0.80s | 3690.2KiB  |
| treesitter               | 9137.0 KiB           | 1.56s | 9708.7KiB  |


seems like both are good. easpecially pgen2 interms of memory usage and performance. but we can use pegen2 
as it has a separate pypi package. We can expect some stability as Python may include more and more peg only changes

# Conclusions

## A. [xonsh-ply](https://www.dabeaz.com/ply/ply.html#ply_nn11)

- the existing parser is slow and uses more memory. 
- the ply codebase is a mess though rply is good and we can optimize with some care

## B. [pegen](https://github.com/we-like-parsers/pegen)

- It will be following the official parser, hence future proof
- generates AST which we can feed directly to the interpreter
- has big peak memory size but it gets released and will end up with optimal size
  - when regex is used to tokenize the peak memory is `2015KiB`
- I found a PR which intends to make use of pegen in place of ply
  - https://github.com/nucleic/enaml/pull/474/
  - https://github.com/jecki/DHParser - another interesting peg generator. 
    - includes test generation 
    - language server...

## C. pgen2

- it comes from lib2to3 package of CPython. but it will be removed in py3.13 or so ... not much future proof
  - but black-formatter has forked it and it may stick around sometime more. 
  we can refer these packages if we decided to base our parser on this
- but has very less memory usage and faster too for any of the tested tools here
- Links
  - https://github.com/pyga/awpa/tree/master/awpa
  - parso grammars

## D. parso
 
- it is a fork of pgen2
- does error recovery of sorts and hence the high memory usage
- we can pick some pieces from this project if we decided to use pgen2

## E. treesitter

- even with the python bindings it ended up using more memory. 
- seems like the memory is not freed as the peak memory is the same as total allocated.

# Step forward

1. implement the completion-context parser in `pgen2` and `pegen` and compare the
   1. development time
   2. performance
   3. memory usage


# Links

- https://www.dabeaz.com/ply/ply.html - good resource to dive into the world of parser generation