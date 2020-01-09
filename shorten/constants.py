import string

ERROR_MESSAGE_1 = '존재하지 않은 페이지입니다.'
ERROR_MESSAGE_2 = '현재 사용가능한 링크가 없습니다.'

CHAR_LIST = string.ascii_letters + string.digits
LIST_LENGTH = 61

CHAR_DICT = {}
for i in range(LIST_LENGTH):
    CHAR_DICT[CHAR_LIST[i]] = i

DATA_MAX = 218340105584896


