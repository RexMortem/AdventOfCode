# 2024 Reflections

Waking up at 5am to code is *hard*. 

## Bruteforce 

*"Premature Optimization is the root of all evil" - Donald Knuth*

It's easy to get wrapped up in the "efficient" solution and opt for that even if it takes minutes longer to figure out the logic of. I've learned that for AOC, you often go for the most straightforward answer that you can just bash out. 

This was particularly true for Part 2 of Day 2. I wasted *a lot* of time at 5am trying to come up with the "efficient" solution which would calculate in O(n) time and required working through little edge cases and lots of debugging etc. Eventually, I got so bogged down with the details that I got fed up and just wrote the bruteforce solution which runs in O(n^2) and has some relatively expensive operations (like array copying). This was so much quicker to come up with and write, and it ran in less than a second. After all, we're running 1000 lines where each line has *at most* 8 values! 

It was definitely a learning experience of the danger of premature optimisation. 