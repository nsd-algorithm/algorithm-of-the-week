s_str = list(input())
t_str = list(input())

while(len(s_str) != len(t_str)):
    if(t_str[-1] == 'A'):
        t_str.pop()
    else:
        t_str.pop()
        t_str.reverse()
if(s_str == t_str):
    print(1)
else:
    print(0)
