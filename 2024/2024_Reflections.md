# 2024 Reflections

Waking up at 5am to code is *hard*. 

## Bruteforce 

*"Premature Optimization is the root of all evil" - Donald Knuth*

It's easy to get wrapped up in the "efficient" solution and opt for that even if it takes minutes longer to figure out the logic of. I've learned that for AOC, you often go for the most straightforward answer that you can just bash out (when the input and computation per thing is small).

This was particularly true for Part 2 of Day 2. I wasted *a lot* of time at 5am trying to come up with the "efficient" solution which would calculate in O(n) time and required working through little edge cases and lots of debugging etc. Eventually, I got so bogged down with the details that I got fed up and just wrote the bruteforce solution which runs in O(n^2) and has some relatively expensive operations (like array copying). This was so much quicker to come up with and write, and it ran in less than a second. After all, we're running 1000 lines where each line has *at most* 8 values! 

It was definitely a learning experience of the danger of premature optimisation. 

## Days 

### Day 1 

I didn't setup my blueprint in time, hence why `1.py` looks different to the others! This led to faffing around with input and losing a lot of time. Despite this, I did it pretty quickly since I've basically done Part 2 in various different leetcode problems. The problem itself was pretty easy.

### Day 2 

I messed up here because, instead of going for the easy bruteforce for Part 2, I went for a complicated approach which had a *lot* of edge-cases to handle. I ended up giving up and going for the bruteforce (which is what I should've done at the start!) 

Nice learning experience and I know how to tackle AOC problems better now. 

### Day 3 

Pretty good problem. Part 1 wasn't too hard, but Part 2 was a bit tricky because my regex wasn't up to scratch. As a result though, I had a fantastic learning experience and learned about greedy vs lazy regex. For example, `don't\(\).*do\(\)` was my original approach but this greedily consumed characters (including do()s!) until the last do(). I learned about how to make this lazy with `?`, which tells regex "consume as few characters as you can; always look for the next part of the pattern first". 

I also learned about Python's regex flags; by default, `.` does not consume newlines! I had to pass `re.DOTALL` which tells Python that `.` should cover all characters. Thanks to `zed0` for helping me out `:)`

### Day 4

