# Pythagorean Triples
A research by @frainmaster.

![](https://github.com/frainmaster/mathematics/blob/master/pythagorean%20triples/1.jpeg)

Pythagorean Triples
- is a combination 3 integers, a, b and c where `a^2 + b^2 = c^2`
- it completes the sides of a right-angle triangle

In this program, any triples which are multiples of a smaller triples (such as `6, 8, 10` is the multiple of `3, 4, 5`) is not being
printed. This means that this program only show the lowest form of a triple because, well, from `3, 4, 5` you can multiply them and get
`6, 8 ,10`, `9, 12, 15` and so on.

# 
### Program
1. The program will prompt user to print a number, `x`. This number will be used to traverse `a` and `b` from 0 to it. So, the triples that
is going to be created will have its `a` and `b` below `x`.
![](https://github.com/frainmaster/mathematics/blob/master/pythagorean%20triples/2.PNG)

2. After the number input, the program will right away output the list of possible triples.
![](https://github.com/frainmaster/mathematics/blob/master/pythagorean%20triples/3.PNG)

# 
### Misc

How do I get to check whether a set of 3 numbers is a pythagorean triple?
> If you check the python code at the line where it reads `if (h - int(h) == 0):`, this condition approves whether the hypotenuse generated
by the 2 initial integers, `a` and `b`, is an integer.

How do I detect if a pythagorean triple is a multiple of a smaller triple?
> If we observe the triples `3, 4, 5` and `6, 8, 10`, the only similarity between them is the ratio of `a:b:c`. Thus, I initialized a
list `eg` which stores the ratio of the triples. If a ratio already existed in the list, so it's proceeding triples will not be generated.

Why do I do this?
> In Mathematics, any findings at all, whether it have a significant impact to the study itself or not, must be recorded because a problem
as small as this can be very helpful for further research or studies.

> Last 8 years I have been working this on paper, limiting my ability to get triples just up to 100. With this program, I can generate
triples up to 10000 in seconds. Thus, it is something to me :ok_woman:
