s = 'Dec 24, 2017'
s1 = s.split(', ')[0].split(' ')
s1.append(s.split(', ')[1])
s1[0],s1[1] = s1[1],s1[0]
print('-'.join(s1))
