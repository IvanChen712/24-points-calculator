# 24-points-calculator

## Calculator

24 points calculator in python

* no limit on the size of numbers (even floats)
* check invalid input
* the goal can also be adjusted, not necessarily 24
* repetitive solutions and redundant parentheses are removed
* only works for 4 numbers' calculation

**Usage**: Run `calculator.py`. Input 4 numbers in four lines and solutions will be printed.

**To be improved**

**Example**:

```
Number 1:3
Number 2:3
Number 3:7
Number 4:7
7*(3+(3/7))
1 solutions in total.
```
    
```
Number 1:3
Number 2:8
Number 3:4
Number 4:6
(8-6/3)*4
6/(3/(4+8))
(8+4)*6/3
(8/4+6)*3
3*4*(8-6)
6*((8+4)/3)
(4*3-8)*6
(8-6)*3*4
(4+8)/(3/6)
(8+4)*(6/3)
10 solutions in total.
```

## Game mode

Play 24-points game with the computer.

* detect invalid input
* give solutions
* based on `calculator.py`

**Usage**: Run `game_mode.py`. Input `No` or the expression to calculate 24 points.

**To be improved**

* add speed mode

**Example**:

```
The four numbers are [10, 8, 8, 13]
If you think there is no solution, input 'No'.
Otherwise, input the expression with no spaces.
😚 Please input your answer:6+6+6+6
You should use all and only use the numbers given.😅😅😅 
😚 Please input your answer:8,8,10,13
HAHA!😄 You lose.🤣👉🤡 
8/8+10+13
10+8/8+13
8*13-8*10
3 solutions in total.
```

```
The four numbers are [10, 9, 6, 10]
If you think there is no solution, input 'No'.
Otherwise, input the expression with no spaces.
😚 Please input your answer:No
Brilliant!😍 You are so smart.😚 
```

```
The four numbers are [8, 3, 8, 1]
If you think there is no solution, input 'No'.
Otherwise, input the expression with no spaces.
😚 Please input your answer:(3-1)*8+8
Correct!🤩 Do you want to see all the solutions? [y/n]
y
8*((1+8)/3)
(3-1)*8+8
(1+8)*8/3
(3+1)*8-8
(1+8)/(3/8)
8-8*(1-3)
(1+8)*(8/3)
8/(3/(1+8))
8 solutions in total.
```