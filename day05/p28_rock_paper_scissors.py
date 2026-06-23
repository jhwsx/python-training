"""
石头剪刀布
"""
d = {'石头': 0, '剪刀': 1, '布': 2}
s = {'石头', '剪刀', '布'}
person_str = input('请出拳: ')
computer_str = s.pop()
person = d.get(person_str, 0)
computer = d[computer_str]
print(f'电脑出拳: {computer_str}, 你出拳: {person_str}')
if person - computer in (-1, 2):
    print('你赢了')
elif person == computer:
    print('打平了')
else:
    print('电脑赢了')
