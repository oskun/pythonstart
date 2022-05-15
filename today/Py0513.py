import cv2

rgb_img = cv2.imread("C:/Users/kun/Pictures/Camera Roll/wallhaven-j5ql2m.jpg")
print(rgb_img.shape)
# cv2.imshow("origin image", imutils.resize(rgb_img, 800))
# cv2.waitKey(10000)

name = "赵飞"
print("name %s" % name)
# 电影
movie = '大侦探pkq'
print(movie)

age = 2
school = True
message = '乔治说：我今年{}睡了{}'.format(age, school)
print(message)
input("请输入")
