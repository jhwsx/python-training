import re
"""
假设QQ邮箱的规则如下:
- 结尾是 @qq.com
- @前面只能是数字
- 且长度为5-11位
- 且不能以0开头
"""


def check_email_valid(email):
    # if email.endswith('@qq.com') and email[:-7].isdigit() and 5 <= len(email[:-7]) <= 11 and email[0] != '0':
    if re.fullmatch(r'[1-9]\d{4,10}@qq\.com', email):
        return True
    return False


assert check_email_valid('392337950@qq.com')
assert check_email_valid('39233795012@qq.com')
# 不是 qq 邮箱
assert not check_email_valid('39233795012@163.com')
# @前面不全是数字
assert not check_email_valid('a9233795012@qq.com')
# 数字部分太短
assert not check_email_valid('12@qq.com')
# 数字部分太长
assert not check_email_valid('123456789012345@qq.com')
# 数字不是0打头
assert not check_email_valid('0123456789@qq.com')

"""
正则表达式一个字符串
正则表达式为要匹配的字符串制定了匹配规则
要匹配的字符串匹配正则表达式指定的规则
正常表达式里面的字符有普通字符和特殊字符(元字符)
    普通字符
      大多数字符为普通字符，它们只会和自身匹配
    特殊字符
      有些字符它们和自身并不匹配，而是匹配一些与众不同的东西或者影响正则表达式的其他部分（对其重复或改变含义）
      元字符：`.  ^  $  *  +  ?  { }  [ ]  \  |  ( )`
注意事项:
1. 是字符串匹配正则表达式，而不是正则表达式匹配字符串
2. 正则表达式要被匹配完全才算是一次成功的匹配
3. 贪婪模式指的是在匹配成功的前提下，尽可能多的匹配
4. 非贪婪模式指的是在匹配成功的前提下，尽可能少的匹配
5. 捕获分组会有子组产生，编号从1号开始，0组指的是整个正则表达式
   就算是做了捕获分组，在匹配时，也是一定需要也先考虑0组的（也就是
   说必须是0组匹配成功了，才能考虑各个子组匹配了什么）
"""
