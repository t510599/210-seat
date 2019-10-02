# 210-seat

## Overview
A program to generate seat for a class. In order to meet everyone's need, it generates a random seat list, and is modified as requested by the student.
一個抽籤選座位程式。先生成一張隨機座位表，再根據所有人輸入的需求進行移動，以達到較為公平的結果。

## Environment
 * Node.js with mongodb installed
 * Python 3.X
 
## Run
 ```bash
cd web
npm install
npm start
```

### Export
`node export.js`

### Run requirements
```bash
cd ../cli
python seats.py run
```
Result will be saved in `seats.txt`.
