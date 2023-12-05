**Knowledge points**: Combinatorial counting, Graph theory

Hello young mathematicians! Today, we are going to dive into a fun problem from the world of combinatorics. Combinatorics is a branch of mathematics that deals with counting, arrangement, and combination. It's like playing with Lego blocks, but with numbers and rules. 

Our problem today involves a group of 15 politicians, each of whom has 6 political enemies. We are asked to find out how many "odd committees" can be formed. An "odd committee" is a group of 3 politicians where either all three are friends or all three are enemies. Sounds like a tricky situation, doesn't it? But don't worry, we'll break it down together.

Let's imagine this situation as a game of connecting dots. Each politician is a dot. If two politicians are enemies, we connect them with a red line. If they are friends, we connect them with a green line. Now, any three politicians form a triangle. If all three sides of the triangle are the same color (either all red or all green), we have an "odd committee". 

To solve this problem, we'll use the concept of "same-color angles". 

First, let's calculate the total number of triangles. We have 15 politicians and we need to choose 3 to form a triangle. So, the total number of triangles is $C_{15}^3$.

Next, let's count the same-color angles from the perspective of each politician. Each politician has 6 enemies, which means 6 red lines. We can choose any two of these red lines to form a red angle. The number of red angles for each politician is $C_6^2$. Similarly, each politician has 8 friends, which means 8 green lines. The number of green angles for each politician is $C_8^2$. So, each politician has $C_6^2 + C_8^2$ same-color angles. With 15 politicians, we have $15*(C_6^2 + C_8^2)$ same-color angles.

Now, let's count the same-color angles from the perspective of triangles. Each same-color triangle has 3 same-color angles. Each different-color triangle has 1 same-color angle. If we have $x$ same-color triangles, we have $C_{15}^3 - x$ different-color triangles. The total number of same-color angles is $3*x + (C_{15}^3 - x)$.

Since the number of same-color angles should be the same from both perspectives, we can set up the following equation:

$15 * (C_6^2 + C_8^2) = 3 * x + (C_{15}^3 - x)$

Solving this equation, we find that x = 95. So, there are 95 "odd committees".

Alternatively, we can solve this problem using the concept of "different-color angles". Each politician has 6 red lines and 8 green lines. We can choose one red line and one green line to form a different-color angle. So, each politician has $6 * 8$ different-color angles. With 15 politicians, we have $15 * 6 * 8$ different-color angles. Each different-color triangle has 2 different-color angles. So, the number of different-color triangles is $15 * 6 * 8 / 2$. The number of same-color triangles is the total number of triangles minus the number of different-color triangles, which is $C_{15}^3 - 15 * 6 * 8 / 2 = 95$.

So, either way, we find that there are 95 "odd committees". Isn't it amazing how different approaches lead to the same answer? That's the beauty of mathematics!