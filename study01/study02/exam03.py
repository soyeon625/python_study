english_score = 100
print(english_score)
'''
변수의 이름은 직관적인 것을 사용합니다.
애플에서는 가이드에 변수명을 아무리 길더라도 정확한 단어의 조합으로 
제작하길 권장합니다.
score보다는 english_score가 직관적입니다.(권장)
eng_score로 사용하는 것이 일반적입니다.(짧게 사용하는 것을 즐겨합니다.)
'''
name = '김혜진' #변수의 선언과 동시에 값을 초기화 합니다.
age = '25' #숫자를 따옴표나 쌍따옴표로 감싸면 문자가 됩니다.
gender = '여성'
mbti = 'ENFP' #변수명은 소문자를 사용합니다.
#변수명이 2개 이상의 단어로 작성할 시에는 _를 사용하여 연결합니다.
#max_speed, car_color

print('나의 이름은'+' 박소연'+' 입니다') #문자열과 문자열의 결합은 +기호로 합니다.
print('나이는 '+'25'+'세 입니다')
print('성별은 '+'여성'+'입니다')
print('MBTI는 '+'INFJ'+'입니다')
print('') # 한 줄 띄우기
print('나의 이름은' + name + ' 입니다') #문자열과 문자열의 결합은 +기호로 합니다.
print('나이는 ' + age + '세 입니다')
print('성별은 ' + gender + '입니다')
print('MBTI는 ' + mbti + '입니다')

name2 = '신짱구' #김혜진 -> 신짱구 값을 변경 (변수는 값이 변할 수 있습니다.)
age2 = '5'
gender2 = '남성'
mbti2 = 'enfp'

print('나의 이름은' + name2 + ' 입니다') #문자열과 문자열의 결합은 +기호로 합니다.
print('나이는 ' + age2 + '세 입니다')
print('성별은 ' + gender2 + '입니다')
print('MBTI는 ' + mbti2 + '입니다')

