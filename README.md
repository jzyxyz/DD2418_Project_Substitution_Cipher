# Substitution Cipher Solver

This is the mini-project for course DD2418 at KTH.  
Authors:  
Zhongyuan Jin, zjin@kth.se  
Abgeiba Yaroslava Isunza Navarro, ayin@kth.se

## project structure

.  
├── check_in_dictionary_improved.py `a script to find word boundary/ correct words in a text`  
├── cipher `cipher texts`  
├── decipher.py `deterministic solver, not working good`  
├── english `knowledge about english language`  
├── ngram_count.py `ngram frequency counter`  
├── ngrams `ngrams frequency files are generated to this folder`  
├── ngram_score.py `language model builder`  
├── README.md  
├── solver.py `probalistic solver, works`  
├── token_count.py `n-letter token frequency counter`  
├── tokens `n-letter token frequency files are generated to this folder`  
└── translate_text4.py `preprocessing for files with punctuations`

## How to?

### preprocessing

> Spaces are present, NERs exist.

```bash
python token_counter.py -f path/to/file -l 2
```

counts words like ok, no, hi, at, of, in...

> Spaces are removed, Punctuations are encrypted

```bash
python ngram_counter.py -f path/to/file -n 1
```

### solver

```bash
python solver.py
```
