**Key Concepts: Combinatorial Construction and Counting, Principle of Maximal Product for a Given Sum**

Hello, young mathematicians! Today, we're going to dive into a fun and fascinating problem from the world of Math Olympiads. Don't worry, it's not as scary as it sounds. In fact, it's just like a puzzle, and we're going to solve it together, step by step.

Imagine you're given a set of points on a flat surface, like dots on a piece of paper. Now, you're asked to connect these dots with lines. The question is: how many lines do you need to draw to make sure you can form a triangle? 

Let's start with a simpler version of the problem. 

**Problem 1:** You have 9 dots, and none of them line up in a straight line. You draw 21 lines connecting these dots. Can you guarantee that there's a triangle formed by these lines?

To solve this, we need to think about the situation where we have the most lines but no triangles. Imagine splitting the dots into two groups, let's say group A and group B. If each dot in group A is connected to every dot in group B, and no dot in the same group is connected, we can't form a triangle. That's because a triangle needs a base, which would be a line within the same group.

Let's say group A has $m$ dots and group B has $n$ dots. The maximum number of lines we can draw without forming a triangle is $m*n$.

Now, we know that $m + n = 9$ (because we have 9 dots in total). To maximize $m*n$, we need to make $m$ and $n$ as close as possible. This is a principle in mathematics: for a given sum, the smaller the difference, the larger the product.

Since $m$ and $n$ are integers and their sum is an odd number (9), the closest we can get them is 4 and 5. So, the maximum number of lines we can draw without forming a triangle is $4*5 = 20$.

But wait, we have 21 lines! That means we must have a triangle. So, the answer to Problem 1 is yes!

**Problem 2:** Now, let's make it a bit harder. You have 80 dots, and none of them line up in a straight line. How many lines do you need to draw to guarantee that you can form a triangle?

Using the same logic as before, we split the dots into two groups. This time, $m + n = 80$. To maximize $m * n$, we make $m$ and $n$ as close as possible, which is 40 each. So, the maximum number of lines we can draw without forming a triangle is $40*40 = 1600$.

Therefore, to guarantee a triangle, we need at least 1601 lines. 

And there you have it! You've just solved two Math Olympiad problems. Remember, math is like a puzzle, and every problem is an adventure. So, keep exploring, and have fun with your mathematical journey!