All the texts in this directory have been encrypted using a
substitution cipher, i.e. the letters (and possibly the punctuation
marks as well) have been permuted.

For instance: the line "this is some text" can be encrypted into "gkyx
yx xush ghjg", using the substitution

t->g, h->k, i->y, s->x, o->u, m->s, e->h, x->j

The challenge is to write a program that, given the ciphertext, can
decrypt the ciphertext and uncover the cleartext. NOTE that usually
one can understand the text even if only a few letters have been
deciphered correctly, but the challenge is to have the program
correctly and automatically decipher EVERY LETTER.

In this directory, you will find some examples of ciphertext, but you
should also generate more samples for testing and development.

Text 1 and 2 is are excerpts from English books. Only [a-zA-Z] are
encrypted. Encryption is caps-independent (i.e. if 'a' is encrypted to
'x', then 'A' is encrypted to 'X'). All spaces and punctuation marks
are untouched. These are the simplest examples, although you will
probably find text1 simpler than text2.

Text 3 is an English newspaper text, tricky because there are many
names.  Only [a-zA-Z] are encrypted. Encryption is caps-independent
(i.e. if 'a' is encrypted to 'x', then 'A' is encrypted to 'X'). All
spaces and punctuation marks are untouched.

Text 4 (in English) has been lowercased before encryption, all spaces
have been removed, and the punctuation marks have also been encrypted. 
(Numbers are untouched).

