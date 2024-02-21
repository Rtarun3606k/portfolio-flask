
c = ['body color',
'font',
'font style',
'card color bg',
'project card color',
'project card font',
'project card button color',
'project card font color',
'certi color',
'certi font ',
'certi font color',
'adout bg color ',
'about font color',
'contact bg',
]
new_c=[]
for i in c:
    b=i.replace(' ','_')
    new_c.append(b)
# print(new_c)
for i in new_c:
    print(i)
    print()