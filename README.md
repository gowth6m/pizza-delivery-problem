# Pizza Delivery Problem (PolyAI)

After a long deferment, the mayor of Z-city has allowed pizzerias to be opened in town. Pizzerias used to be unlawful because of health reasons (according to the mayor). The city is big, and suddenly there are pizzerias everywhere.

We can imagine the city like a matrix with ​N​x​N squares, where every square represents one block of the city. Every pizzeria only delivers pizza to the nearby blocks. Specifically, every pizzeria delivers pizza to every block that is at most ​R ​blocks away from block the pizzeria's location. Distance is determined by the minimum number of blocks that the delivery guy must take if he is going East/West or North/South (moving diagonally is forbidden in Z-city). For example, let's say that ​N​=5 and a pizzeria is located at the block (3, 3). It can deliver to a 2 block distance at most. The following map shows where the given pizzeria delivers pizzas.

```
00X00
0XXX0 
XXXXX 
0XXX0 
00X00
```

Mr. Little Z loves pizza, so he wants to move to the block where he can have the greatest selection of pizzas (the block that has the maximum number of pizzerias delivering to it).

Help Mr. Little Z find that maximum. In other words, if he moves to the block with the greatest selection of pizzas, how many pizzerias will be able to deliver to his block?

## INPUT:

The first line of the standard input contains the two numbers ​N and ​M​, and both numbers are on the interval [1, 10000]. The number ​N represents the dimension of the city in blocks (the city has ​N​x​N blocks). ​M is the number of pizzerias in the city. The following ​M lines contain information about each pizzeria, given by the three numbers ​X,​ ​Y​, ​R​. The numbers ​X and ​Y represent the block where the pizzeria is located, (1 <= ​X​, ​Y <= ​N​) and the number ​R represents the maximum distance that the given pizzeria's delivery guy will travel to deliver pizza (1 <= ​R​ <= 100).

## OUTPUT:

Write one number to the standard output that represents the number of pizzerias that deliver pizzas to the block with the greatest selection of pizzas.

## How to run (use python 3):
```console
python3 main.py < input.txt
```
