def love_language(partner, weeks):
    '''
    According to Gary Chapman, marriage counselor and the author of "The Five Love Languages" books, there are five major ways to express our love towards someone: words of affirmation, quality time, gifts, acts of service, and physical touch. These are called the love languages. Usually, everyone has a main language: the one that he/she "speaks" and understands best. In a relationship, it's import to find your partner's main love language, so that you get along better with each other.

Your task

Unfortunately, your relationship got worse lately... After a long discussion with your partner, you agreed to give yourself a few weeks to improve it, otherwise you split up...

You will be given a partner instance, and n weeks. The partner has a .response method, and the responses may be: "positive" or "neutral". You can try to get a response once a day, thus you have n * 7 tries in total to find the main love language of your partner!

The love languages are: "words", "acts", "gifts", "time", "touch" (available predefined as LOVE_LANGUAGES)

Note: your partner may (and will) sometimes give a positive response to any love language ("false positive"), but the main one has a much higher possibility. On the other hand, you may get a neutral response even for the main language, but with a low possibility ("false negative").

There will be 50 tests. Although it's difficult to fail, in case you get unlucky, just run the tests again. After all, a few weeks may not be enough...

Examples

main love language: "words"

partner.response("words")  -->  "positive"
partner.response("acts")   -->  "neutral"
partner.response("words")  -->  "positive"
partner.response("time")   -->  "neutral"
partner.response("acts")   -->  "positive"    # false positive
partner.response("gifts")  -->  "neutral"
partner.response("words")  -->  "neutral"     # false negative
etc.
    '''
    
    print(f'Weeks: {weeks}')
    print(LOVE_LANGUAGES)
    
    # Convert weeks to days
    # Create LL_count list
    # While days > 0 (reduce days by 1 each loop)
    # Go through LOVE_LANGUAGES once each day, add response (0 or 1) to LL_count at same index
    # Return language at same index as max of LL_count
    
    days = weeks * 7
    LL_count = [0,0,0,0,0]
    LL_dict = {} # For debugging
    for language in LOVE_LANGUAGES:
        LL_dict[language] = 0
    i = 0
    
    while days > 0:
        days -= 1
        LL_dict[LOVE_LANGUAGES[i]] += 1
        if partner.response(LOVE_LANGUAGES[i]) == "positive":
            LL_count[i] += 1

        if i < len(LOVE_LANGUAGES)-1:
            i += 1
        elif i >= len(LOVE_LANGUAGES)-1:
            i = 0

    # Debugging
    print(f'LL_count: {LL_count}')
    print(f'LL_dict: {LL_dict}')
    print(f'Returning: {LOVE_LANGUAGES[LL_count.index(max(LL_count))]}')
    
    return LOVE_LANGUAGES[LL_count.index(max(LL_count))]