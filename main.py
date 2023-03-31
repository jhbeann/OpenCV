import cv2

## 영상 이미지 읽기
scr = cv2.imread('images/picture01.jpg')

## 영상 처리 알고리즘 구현##
dst1 = cv2.cvtColor(scr, cv2.COLOR_RGB2GRAY)
dst2 = scr.copy()
_ , dst2 = cv2.threshold(dst2, 127, 255, cv2.THRESH_BINARY) 
## 영상 디스플레이
cv2.imshow('scr', scr)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
## 메인
cv2.waitKey(0)
cv2.destroyAllwindows()

