## 제어문

- 코드의 실행 흐름을 제어하는 데 사용되는 구문
- 조건에 따라 블록을 실행하거나 반복적으로 코드를 실행

### 조건문
- 주어진 조건식을 평가하여 True인 경우에만 코드 블록을 실행하거나 건너뜀

```python
if 표현식:
    코드블록
elif 표현식:
    코드블록
else:
    코드블록
```
  
  - 복수 조건문
    <p>조건식을 동시에 검사하는 것이 아니라 순차적으로 비교</p>
  - 중첩 조건문
    <p>조건식의 중첩 역시 가능</p>
  

### 반복문
  - 주어진 코드 블록을 여러 번 반복해서 실행하는 구문
  - 특정 작업을 반복적으로 수행
  - 주어진 조건이 참인 경우 반복 수행
  
#### for문
  - 임의의 시퀀스의 항목들을 그 시퀀스에 들어있는 순서대로 반복
  - 기본 구조
  ```python
  for 변수 in iterable_object:
      코드블록
  ```
  - 반복문의 작동 원리
  ```python
  items = ['apple', 'banana', 'coconut']
  for item in items:
      print(item)
  """
  apple
  banana
  coconut
  """
  ```
  - 문자열 순회
  ```python
  country = 'Korea'
  for char in country:
      print(char)
  """
  K
  o
  r
  e
  a
  """
  ```
  - 인덱스로 순회
  ```python
  numbers = [4,6,10,-8,5]
  for i in range(len(numbers)):
      numbers[i] = numbers[i] * 2
  
  print(numbers)
  ```
#### while 문
  - 주어진 조건식이 True인 동안 코드를 반복해서 실행 == 조건식이 False가 될 때 까지 반복
  ```python
  a = 0
  while a < 3
      print(a)
      a += 1

  print('끝')
  """
  0
  1
  2
  """
  ```

### List comprehension
  - <p>간결하고 효율적인 리스트 생성 방법</p>

  1. list comprehension 구조
      ```python
      # 1~10 요소를 가지는 리스트 만들기
      new_list = [i for i in range (1,11)]
      print(new_list)
      ```

      ```python
      # if문 사용
      new_list = [i for i in range(10) if i % 2 == 1]

      # if else문 사용
      new_list2 = [i if i % 2 == 1 else str(i) for i in range(10)]
      ```

### enumerate
  - iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수
  ```python
  fruits = ['apple', 'banana', 'cherry']
  for index, fruit in enumerate(fruits):
      print(f'인덱스 {index}: {fruit}')
  """
  인덱스 0: apple
  인덱스 1: banana
  인덱스 2: cherry
  """
  ```
