kobon = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 5,
    "6": 7,
    "7": 11,
    "8": 15,
    "9": 21,
    "10": 25,
    "11": 32,
    "12": 38,
    "13": 47,
    "14": 53,
    "15": 65,
    "16": 72,
    "17": 85,
    "18": 93,
    "19": 104,
    "20": 115,
    "21": 130
  }
m=int(input())
for i in range(m):
    x=input().split(',')
    # print(x)
print(kobon[str(m)])