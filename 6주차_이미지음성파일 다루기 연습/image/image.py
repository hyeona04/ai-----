from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open('C:\\Github\\ai-programming\\6주차_이미지음성파일 다루기 연습\\f.jpg')

img_np = np.array(img) ## 행렬로 변환된 이미지
plt.imshow(img_np) ## 행렬 이미지를 다시 이미지로 변경해 디스플레이
plt.show() ## 이미지 인터프린터에 출력
img.show()

# 이미지 파일명
print(img.filename)
# 이미지 형식
print(img.format)
# 이미지 크기
print(img.size)
# 이미지 너비
print(img.width)
# 이미지 높이
print(img.height)
# 이미지의 색상 모드
print(img.mode)


