# Overview

experiment with different ways to parse and generate ast with optimal speed & memory. 
All of these below parse Python3.10 grammar. 

| module    | total allocated size | time  | peak       |
|-----------|----------------------|-------|------------|
| pgen2     | 369KiB               | 0.08s | 684KiB     |
| pegen     | 1234KiB              | 0.38s | 19655.9KiB |
| xonsh-ply | 8240.6 KiB           | 0.65s | 10333.5KiB |


seems like both are good. easpecially pgen2 interms of memory usage and performance. but we can use pegen2 
as it has a separate pypi package. We can expect some stability as Python may include more and more peg only changes

# Conclusions

## A. xonsh-ply

- the existing parser is slow and uses more memory. 
- the ply codebase is a mess though rply is good and we can optimize with some care

## B. pegen

- It will be following the official parser, hence future proof
- generates AST which we can feed directly to the interpreter
- has big peak memory size but it gets released and will end up with optimal size

## C. pgen2

- it comes from lib2to3 package of CPython. but it will be removed in py3.13 or so ... not much future proof
  - but black-formatter has forked it and it may stick around sometime more. 
  we can refer these packages if we decided to base our parser on this
- but has very less memory usage and faster too for any of the tested tools here
