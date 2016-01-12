#!/usr/bin/env python

input = [
    "HauteLook is a member-only shopping website",
    "offering flash sales and limited-time",
    "sale events with",
    "top brands in women's and",
    "men's fashion."
]

max_length = 16

expected = [
    "HauteLook is a",
    "member-only",
    "shopping website",
    "offering flash",
    "sales and",
    "limited-time",
    "sale events with",
    "top brands in",
    "women's and",
    "men's fashion."
]

def rewrap_lines(input, max_length):
    # answer here:
    return []

if __name__ == "__main__":
    print("Telegram Problem...")

    answer = rewrap_lines(input, max_length)    
    print("Answer: %s" % answer)    

    assert(len(answer) > 0)
    for i in range(0, len(expected)):
        print('line [%i] answer: [%s], expected [%s]' % (i, answer[i], expected[i]))
        assert(answer[i] == expected[i])
        
    print("SUCCESS!")
