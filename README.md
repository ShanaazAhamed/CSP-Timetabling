# CSP: Timetabling

## Control Satisfaction Problem

There is a list of subjects, a set of possible
time slots for each subject and a set of rooms. Some subjects are compulsory while some are optional. Following are the constraints to satisfy.

```
SUB_1,o,Tu1,Tu2,F3,
SUB_2,o,M2,M3,Tu2,
.
.
.
SUB_13,c,W1,Th3,F1,
R1,R2,R3
```

### Constrains
- A given subjects can be assigned only to one of the possible time slots given for that 
subject
- A given subjects can be assigned only to one of the possible time slots given for that 
subject
- Two subjects cannot be assigned to the same room if they are assigned to the same time 
slot

### Backtracking algorithm

<p align="center">
<img src="img/ba-state-space-tree.webp" width="50%">
</p>
<p align="center">
<small>source: <a href="https://www.programiz.com/dsa/backtracking-algorithm">Programiz</a></small>
</p>

`Backtracking` is a general 
algorithmic strategy for solving computing problems that takes into consideration looking 
through all possible combinations.

## To run virtual environment


```
# macOS/Linux
# You may need to run sudo apt-get install python3-venv first
python3 -m venv .venv

# Windows
# You can also use py -3 -m venv .venv
python -m venv .venv
```

```
1. `ctrl` + `shift` + `p` and select Python Interpreter
2. Select the enter interpreter path
3. select `.venv/Scripts/python.exe`
```

## Input Command

```
python main.py Input.csv Output.csv
```

## Enjoy 🥳