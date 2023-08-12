# 24-points-calculator

## Calculator

24 points calculator in python

* no limit on the size of numbers (even floats)
* check invalid input
* the goal can also be adjusted, not necessarily 24
* repetitive solutions and redundant parentheses are removed
* only works for 4 numbers' calculation

**Usage**: Run `calculator.py`. Input 4 numbers in four lines and solutions will be printed.

**Example**:

```
Number 1:3
Number 2:3
Number 3:7
Number 4:7
7*(3+(3/7))
1 solutions in total.


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

**Example**:

```
The four numbers are [3, 8, 5, 6]
If you think there is no solution, input 'No'.
Otherwise, input the expression with no spaces.
😚 Please input your answer:3*8*(6-5)
Correct!🤩 Do you want to see all the solutions? [y/n]
y
8*(6/(5-3))
8/(6-5)*3
8*3/(6-5)
8/((6-5)/3)
6/((5-3)/8)
3/((6-5)/8)
8*(3/(6-5))
8*6/(5-3)
8*(5-6/3)
8/(5-3)*6
8*(6-5)*3
8/((5-3)/6)
(6-5)*3*8
13 solutions in total.
```

```
The four numbers are [10, 9, 6, 10]
If you think there is no solution, input 'No'.
Otherwise, input the expression with no spaces.
😚 Please input your answer:No
Brilliant!😍 You are so smart.😚 
```

```
The four numbers are [5, 10, 6, 2]
If you think there is no solution, input 'No'.
Otherwise, input the expression with no spaces.
😚 Please input your answer:5+10+6+2
HAHA!😄 You lose.🤣👉🤡 
6*2*10/5
10/(5/2/6)
2*(6/(5/10))
10*(6/(5/2))
2*(10*6/5)
6/(5/2/10)
6/(5/10/2)
2*6/5*10
6*2*(10/5)
2/(5/6)*10
2*10/(5/6)
2*10/5*6
6*10*(2/5)
6*10*2/5
10/(5/6/2)
6*(10/(5/2))
2*(10+5)-6
6*10/(5/2)
2*(10/5)*6
(2+10/5)*6
2/(5/(6*10))
(5-2)*10-6
6/(5/(10*2))
2*10*(6/5)
2*(10/(5/6))
6*(2/(5/10))
2*6/(5/10)
6*(10*2/5)
2/(5/10/6)
10/(5/(6*2))
2*(6/5)*10
31 solutions in total.
```