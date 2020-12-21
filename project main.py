#HILL 암호화 하기
# 유니코드 한글 시작 : 44032, 끝 : 55199
BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28

# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ',
                'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ',
                 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ','ㅣ']

# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ',
                 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
                 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def convert(test_keyword):
    split_keyword_list = list(test_keyword)
    # print(split_keyword_list)

    result = list()
    for keyword in split_keyword_list:
        # 한글 여부 check 후 분리
        if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', keyword) is not None:
            char_code = ord(keyword) - BASE_CODE
            char1 = int(char_code / CHOSUNG)
            result.append(CHOSUNG_LIST[char1])
            # print('초성 : {}'.format(CHOSUNG_LIST[char1]))
            char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)
            result.append(JUNGSUNG_LIST[char2])
            # print('중성 : {}'.format(JUNGSUNG_LIST[char2]))
            char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))
            if char3 == 0:
                result.append(' ')
            else:
                result.append(JONGSUNG_LIST[char3])
            # print('종성 : {}'.format(JONGSUNG_LIST[char3]))
        else:
            result.append(keyword)

    return result

dic_1_1 = {"ㄱ": 0, "ㄲ": 1, "ㄴ": 2, "ㄷ": 3, "ㄸ": 4, "ㄹ": 5, "ㅁ": 6, "ㅂ": 7, "ㅃ": 8, "ㅅ": 9, "ㅆ": 10, "ㅇ": 11, "ㅈ": 12,
           "ㅉ": 13, "ㅊ": 14, "ㅋ": 15, "ㅌ": 16, "ㅍ": 17, "ㅎ": 18}
dic_1_2 = {"ㅏ": 19, "ㅐ": 20, "ㅑ": 21, "ㅒ": 22, "ㅓ": 23, "ㅔ": 24, "ㅕ": 25, "ㅖ": 26, "ㅗ": 27, "ㅘ": 28, "ㅙ": 29, "ㅚ": 30,
           "ㅛ": 31, "ㅜ": 32, "ㅝ": 33, "ㅞ": 34, "ㅟ": 35, "ㅠ": 36, "ㅡ": 37, "ㅢ": 38, "ㅣ": 39}
dic_1_3 = {"ㄱ": 40, "ㄲ": 41, "ㄳ": 42, "ㄴ": 43, "ㄵ": 44, "ㄶ": 45, "ㄷ": 46, "ㄹ": 47, "ㄺ": 48, "ㄻ": 49, "ㄼ": 50, "ㄽ": 51,
           "ㄾ": 52, "ㄿ": 53, "ㅀ": 54, "ㅁ": 55, "ㅂ": 56, "ㅄ": 57, "ㅅ": 58, "ㅆ": 59, "ㅇ": 60, "ㅈ": 61, "ㅊ": 62, "ㅋ": 63,
           "ㅌ": 64, "ㅍ": 65, "ㅎ": 66, " ": 67, "!": 68, "@": 69, "#": 70, }

dic_2 = {0: "AA", 1: "AB", 2: "AC", 3: "AD", 4: "AE", 5: "AF", 6: "AG", 7: "AH", 8: "AI", 9: "AJ", 10: "AK", 11: "AL",
         12: "AM", 13: "AN", 14: "AO", 15: "AP", 16: "AQ", 17: "AR", 18: "AS", 19: "BA", 20: "BB", 21: "BC", 22: "BD",
         23: "BE", 24: "BF", 25: "BG", 26: "BH", 27: "BI", 28: "BJ", 29: "BK", 30: "BL", 31: "BM", 32: "BN", 33: "BO",
         34: "BP", 35: "BQ", 36: "BR", 37: "BS", 38: "BT", 39: "BU", 40: "CA", 41: "CB", 42: "CC", 43: "CD", 44: "CE",
         45: "CF", 46: "CG", 47: "CH", 48: "CI", 49: "CJ", 50: "CK", 51: "CL", 52: "CN", 53: "CM", 54: "CO", 55: "CP",
         56: "CQ", 57: "CR", 58: "CS", 59: "CT", 60: "CU", 61: "CV", 62: "CW", 63: "CX", 64: "CY", 65: "CZ", 66: "DA",
         67: "DB", 68: "DC", 69: "DD", 70: "DE"}

dic_3 = {"AA": 0, "AB": 1, "AC": 2, "AD": 3, "AE": 4, "AF": 5, "AG": 6, "AH": 7, "AI": 8, "AJ": 9, "AK": 10, "AL": 11,
         "AM": 12, "AN": 13, "AO": 14, "AP": 15, "AQ": 16, "AR": 17, "AS": 18, "BA": 19, "BB": 20, "BC": 21, "BD": 22,
         "BE": 23, "BF": 24, "BG": 25, "BH": 26, "BI": 27, "BJ": 28, "BK": 29, "BL": 30, "BM": 31, "BN": 32, "BO": 33,
         "BP": 34, "BQ": 35, "BR": 36, "BS": 37, "BT": 38, "BU": 39, "CA": 40, "CB": 41, "CC": 42, "CD": 43, "CE": 44,
         "CF": 45, "CG": 46, "CH": 47, "CI": 48, "CJ": 49, "CK": 50, "CL": 51, "CN": 52, "CM": 53, "CO": 54, "CP": 55,
         "CQ": 56, "CR": 57, "CS": 58, "CT": 59, "CU": 60, "CV": 61, "CW": 62, "CX": 63, "CY": 64, "CZ": 65, "DA": 66,
         "DB": 67, "DC": 68, "DD": 69, "DE": 70}

dic_4 = {0: "ㄱ", 1: "ㄲ", 2: "ㄴ", 3: "ㄷ", 4: "ㄸ", 5: "ㄹ", 6: "ㅁ", 7: "ㅂ", 8: "ㅃ", 9: "ㅅ", 10: "ㅆ", 11: "ㅇ", 12: "ㅈ",
           13: "ㅉ", 14: "ㅊ", 15: "ㅋ", 16: "ㅌ", 17: "ㅍ", 18: "ㅎ", 19: "ㅏ", 20: "ㅐ", 21: "ㅑ", 22: "ㅒ", 23: "ㅓ", 24: "ㅔ",
           25: "ㅕ", 26: "ㅖ", 27: "ㅗ", 28: "ㅘ", 29: "ㅙ", 30: "ㅚ", 31: "ㅛ", 32: "ㅜ", 33: "ㅝ", 34: "ㅞ", 35: "ㅟ", 36: "ㅠ",
           37: "ㅡ", 38: "ㅢ", 39: "ㅣ", 40: "ㄱ", 41: "ㄲ", 42: "ㄳ", 43: "ㄴ", 44: "ㄵ", 45: "ㄶ", 46: "ㄷ", 47: "ㄹ", 48: "ㄺ",
           49: "ㄻ", 50: "ㄼ", 51: "ㄽ", 52: "ㄾ", 53: "ㄿ", 54: "ㅀ", 55: "ㅁ", 56: "ㅂ", 57: "ㅄ", 58: "ㅅ", 59: "ㅆ", 60: "ㅇ",
           61: "ㅈ", 62: "ㅊ", 63: "ㅋ", 64: "ㅌ", 65: "ㅍ", 66: "ㅎ", 67: " ", 68: "!", 69: "@", 70: "#"}

#문자 행렬의 수치화
import numpy as np
def word_cha_num(matrix_a):
    global e1,e2, w, matrix
    test_keyword = e1.get()
    test_keyword = test_keyword.replace(' ', '')
    w = len(test_keyword)
    word = list(convert(test_keyword))
    matrix = np.reshape(word, (w, 3))
    matrix_a = np.zeros([w,3])
    for i in range(0,w):
        matrix_a[i][0]=dic_1_1[matrix[i][0]]
        matrix_a[i][1]=dic_1_2[matrix[i][1]]
        matrix_a[i][2]=dic_1_3[matrix[i][2]]

    test_a = np.array([[6,4,13],[11,11,23],[6,5,8]], np.int)
    matrix_a = (np.matmul(test_a,matrix_a.T))%71

    result_open =list()
    for i in range(0,3):
        for j in range(0,w):
            result_open.append(dic_2[matrix_a[i][j]])

    return result_open

# 암호화된 문장을 공개 하는 부분
def open_process(result_open):
    result_open = ''.join(result_open)
    secret_code = result_open
    return secret_code

#행렬의 역행렬 과정
def matrix_process():
    test_a = np.array([[6,4,13],[11,11,23],[6,5,8]], np.int)
    key = np.array([[1,0,0],[0,1,0],[0,0,1]], np.int)
    b_0=test_a[0]                       #1열
    b_1=test_a[1]                       #2열
    b_2=test_a[2]                       #3열

    for i in range(1,1000):
        if (b_0[0]*i) % 71 == 1:
            result_1 = i
            break;

    d_0=b_0*result_1 % 71
    d_1=(b_1 - d_0*b_1[0]) % 71
    d_2=(b_2 - d_0*b_2[0]) % 71
    test_b=np.array([d_0,d_1,d_2])

    key[0] = key[0]*i %71
    key[1] = (key[1] - (key[0]*b_1[0])) % 71
    key[2] = (key[2] - (key[0]*b_2[0])) % 71

    for k in range(1,1000):
        if (d_1[1]*k) % 71 == 1:
            result_2 = k
            break;

    d_3=d_1*result_2 % 71
    d_4=(d_0 - d_3*d_0[1]) % 71
    d_5=(d_2 - d_3*d_2[1]) % 71
    test_c=np.array([d_4,d_3,d_5])

    key[1] = key[1]*result_2 %71
    key[0] = (key[0] - (key[1]*d_0[1])) % 71
    key[2] = (key[2] - (key[1]*d_2[1])) % 71

    for h in range(1,1000):
        if (d_5[2]*h) % 71 == 1:
            result_3 = h
            break;

    d_6=d_5*result_3 % 71
    d_7=(d_4 - d_6*d_4[2]) % 71
    d_8=(d_3 - d_6*d_3[2]) % 71
    test_d=np.array([d_7,d_8,d_6])

    key[2] = key[2]*h % 71
    key[0] = (key[0] - (key[2]*d_4[2])) % 71
    key[1] = (key[1] - (key[2]*d_3[2])) % 71
    return key

#복호화 과정
def num_cha_word(result_open,key):
    ww = len(result_open)
    ww = int(ww/3)
    result_open = np.reshape(result_open,(3,ww))
    result_close = np.zeros([3,w])
    for i in range(0,3):
        for j in range(0,w):
            result_close[i][j]=dic_3[result_open[i][j]]
    result_close = (np.matmul(key, result_close))%71
    hangul_com =list()
    for i in range(0,w):
        for j in range(0, 3):
            hangul_com.append(dic_4[result_close[j][i]])
    while ' 'in hangul_com:
       hangul_com.remove(' ')
    return hangul_com

#한글 자음 모음 결합
def hangul_com_process(hangul_com):
    from hangul_utils import join_jamos
    return join_jamos(hangul_com)

#암호화문장을 영어로 두 글자씩 쪼개서 리스트에 넣어준다.
def str_list_change(e2):
    word = e2.get()
    leng = len(word)
    word_2 = list()
    for i in range(0,leng):
        if(i<leng/2):
            word_2.append(word[i*2:(i+1)*2])
        else:
            break
    return word_2

#gui를 통한 출력 과정
from tkinter import *
window = Tk()
window.geometry("500x300+300+200")
def process_1():
    try:
        test_keyword = e1.get()
        test_keyword = test_keyword.replace(' ','')
        w = len(test_keyword)
        word = list(convert(test_keyword))
        matrix = np.reshape(word, (w, 3))
        result_open = word_cha_num(matrix.T)
        print(open_process(result_open))
    except:
        print("SYSTEM ERROR!")
def process_2():
    try:
        code_data = str_list_change(e2)
        hangul_com = num_cha_word(code_data,matrix_process())
        print(hangul_com_process(hangul_com))
    except:
        print("SYSTEM ERROR!")

Label(window, text='암호화').grid(row=0)
e1 = Entry(window)
e1.grid(row=0, column=1)
Label(window, text='복호화').grid(row=1)
e2 = Entry(window)
e2.grid(row=1, column=1)
Button(window, text='암호화', command=process_1).grid(row=3, column=1, sticky=W, pady=4)
Button(window, text='복호화', command=process_2).grid(row=4, column=1, sticky=W, pady=4)
window.mainloop()


