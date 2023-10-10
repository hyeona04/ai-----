from PIL import Image
from PIL import ImageFilter

img = Image.open('C:\\Github\\ai-programming\\6주차_이미지음성파일 다루기 연습\\h.jpeg')

# RGB로 표현된 컬러 이미지를 흑백으로 변경
img_gray = img.convert("L")

# 흑백으로 변환된 이미지 출력
img_gray.show()

# 1 (1비트 픽셀, 흑백, 바이트당 1픽셀로 저장)
# L (8비트 픽셀, 흑백)
# P (8비트 픽셀, 색상 팔레트를 사용하여 다른 모드에 매핑됨)
# RGB (3x8비트 픽셀, 트루 컬러)
# RGBA (4x8비트 픽셀, 투명 마스크가 있는 트루 컬러)
# CMYK (4x8비트 픽셀, 색상 분리)
# YCbCr (3x8비트 픽셀, 컬러 비디오 형식)
# LAB (3x8비트 픽셀, Lab 색 공간)
# HSV (3x8비트 픽셀, 색조, 채도, 값 색 공간)
# I (32비트 부호 있는 정수 픽셀)
# F (32비트 부동 소수점 픽셀)

# Blur 효과를 줄 때 가장 많이 사용하는 가우시안 블러 --> 숫자를 크게 할 수록 흐려짐
img_blur = img.filter(ImageFilter.GaussianBlur(10))

# 이미지 출력
img_blur.show()

#이미지의 엣지를 더 강조하고 싶을때
img_edge = img.filter(ImageFilter.EDGE_ENHANCE)

img_edge.show()

#이미지 컨투어
img_contour = img.filter(ImageFilter.CONTOUR)
img_contour.show()

#이미지 디테일
img_detail = img.filter(ImageFilter.DETAIL)
img_detail.show()
