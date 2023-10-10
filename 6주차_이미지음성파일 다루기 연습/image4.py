from PIL import Image

img = Image.open('C:\\Github\\ai-programming\\6주차_이미지음성파일 다루기 연습\\h.jpeg')



# 이미지 90도 회전
img_rotated = img.rotate(-90)

# 회전한 이미지 출력
img_rotated.show()


#4:3이미지를 회전시키니 반 시계 방향으로 돌고, 이미지가 1:1로 되고 빈부분은 검정으로 됨