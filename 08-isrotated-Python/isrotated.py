# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	#Your code goes here
	if str1 == str2:
		return False
	if str1[0] in str2:
		start = str2.index(str1[0]) + 1

		for index in range(1, len(str1)):
			if start > len(str2) - 1:
				start = 0
			if str1[index] != str2[start]:
				return False
			start += 1
		return True
	else:
		return False