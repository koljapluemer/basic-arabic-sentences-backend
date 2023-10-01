## So how did use this?

1. Activate the django app, navigate to `/admin`, add/edit all MainSentence and SentenceVariances, in English
2. Go to home url to get a list of sentences, copy
3. Paste into ChatGPT with the following prompt:

```
You are my Egyptian Colloquial Arabic teacher. For each of the following sentences, please add the translation in Misry after a ";". Make sure to use colloquial Arabic that would be understood in Egypt!!:

Please use a code block so I can easily copy the respons:
```

4. save response as `autotranslation1.txt`
5. run `0_...py`, now the translations are saved to the db
6. run `1_...py`, which extracts all the words, and saves them and them stemmed as `Word` objects
7. Go to `/words` and copy this list
8. Feed to ChatGPT with the following prompt
```
Here is a list of Egyptian Arabic vocabs. Please add to each line a ; followed by the 3-5 most common translations. Use a codeblock for formatting:
```
9. Save as `word-translation1.txt`
10. Run `3_...`, the words now have their translations saved as well
11. Use the same `/words` list to copy again
12. Feed to ChatGPT again, this time with the prompt:
```
User
You are my Misry teacher from Cairo. 

Here is a list of Egyptian Arabic vocabs. For each one, find three different concordances. Put each concordance in one line. For each line, include the Egyptian Arabic script and then, after a ; the English translation. Use a codeblock so I can copy easily.
```

*This takes about a million years*
13. Save response as `concordances1.txt`
14. Run `4_...py`. We now have a lot of concordance objects.

...probably missing cloze deletion, yes/no questions or something else to do with concordances. Shall probably check lit?

