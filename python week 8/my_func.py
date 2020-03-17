def convert_grade(grade):
    if(grade < 50): return('F')
    if(grade < 55): return('D')
    if(grade < 60): return('D+')
    if(grade < 65): return('C-')
    if(grade < 70): return('C')
    if(grade < 75): return('C+')
    if(grade < 80): return('B-')
    if(grade < 85): return('B')
    if(grade < 90): return('B+')
    if(grade < 95): return('A-')
    if(grade <= 100): return('A')
   
if __name__ == "__main__":
    
    grade = int(input())
    print(convert_grade(grade))    