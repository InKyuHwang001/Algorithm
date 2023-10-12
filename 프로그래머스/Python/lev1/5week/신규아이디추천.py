def solution(new_id):
    #12
    tmp = new_id.lower()
    a = ''
    for s in tmp:
        if s.isalpha() or s.isdigit() or s in ['-','_','.']:
            a += s
    #3
    while '..' in a:
        a = a.replace("..", ".")
    #4
    if a !='' and a[0] == ".":
        a = a[1:]
    if a !='' and a[-1] == ".":
        a = a[:-1]
    #5
    a = "a" if a == '' else a
    #6
    a = a[:15] if len(a) >= 16 else a
    if a[-1] == ".":
        a = a[:-1]
    #7
    a = a+a[-1]*(max(0, 3 - len(a)))
    return a