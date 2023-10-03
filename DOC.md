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


15. Start creating exercises from concordances by getting the list from `/concordances` and feed it to ChatGPT:

```
You are my Egyptian Arabic teacher. I will now give you a list of sentences in Misry. Please create a question with one wrong and one right answer for every sentence, in English. Answer in a code block in the following format:

Original sentence ; question in english ; correct answer ; wrong answer

```

However, I had to correct several times, like:

```
you are still using very simple "not negation"  "negation" format. Please ask for the content in the sentence in a less predicatable way. Avoid!!! one answer being "yes, X is Y" and the other "no X is not Y"
```

and 

```
you are giving the EXACT same answer. please avoid!!! the word "not" or any kind of simple negation in the wrong answer
```

And the engine is confused everytime the original concordance is a question, so probably skip integrating everything containing ؟ 

Also, the engine started making up sentences after a point, but I guess base logic catches that.

16. I tried generating cloze deletion w/ chatGPT but it's hopeless