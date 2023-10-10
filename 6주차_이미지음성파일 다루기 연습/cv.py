from PIL import Image
import numpy as np
import cv2

# 이미지 크기 설정
width, height = 500, 500

# 흰색 화면으로 초기화된 NumPy 배열 생성
numpy_image = 255 * np.ones((height, width, 3), dtype=np.uint8)

# NumPy 배열을 이미지로 변환
image = Image.fromarray(numpy_image)

# 이미지를 파일로 저장
image.save('C:\\Github\\ai-programming\\6주차_이미지음성파일 다루기 연습\\f.jpg')

# 이미지 표시 (선택 사항)
image.show()



# 이미지 읽기
image = cv2.imread('C:\\Github\\ai-programming\\6주차_이미지음성파일 다루기 연습\\f.jpg')

# 이미지 표시
cv2.imshow('Example Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
