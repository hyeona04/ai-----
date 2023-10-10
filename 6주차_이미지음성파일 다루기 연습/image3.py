from PIL import Image

img = Image.open('C:\\Github\\ai-programming\\6주차_이미지음성파일 다루기 연습\\h.jpeg')

# 이미지 자르기
img_cropped = img.crop((0,0,300,300))

# 잘라낸 이미지 출력
img_cropped.show()
