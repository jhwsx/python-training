"""
假设QQ邮箱的规则如下:
- 结尾是 @qq.com
- @前面只能是数字
- 且长度为5-11位
- 且不能以0开头
"""


def check_email_valid(email):
    if email.endswith('@qq.com') and email[:-7].isdigit() and 5 <= len(email[:-7]) <= 11 and email[0] != '0':
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
