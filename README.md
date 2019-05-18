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
├── processed_cipher.txt `file holder for preprocessed cipher`  
├── README.md  
├── solver.py `probalistic solver, works`  
├── token_count.py `n-letter token frequency counter`  
├── tokens `n-letter token frequency files are generated to this folder`  
└── translate_text4.py `preprocessing for text4 which has punctuations`

## How to?

### generating statistics

```bash
python token_counter.py -f path/to/file -l 2
```

counts words like ok, no, hi, at, of, in...

```bash
python ngram_counter.py -f path/to/file -n 1
```

counts n-grams frequencies with the specified n

for text4 where punctuations are also encrypted, run

```bash
python translate_text4.py
```

### solver

please see the comments in the file also for details

```bash
python solver.py
```

### check which letters are correctly decrypted

```bash
python check_in_dictionary_improved_sh
```
