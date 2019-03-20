# This program is used to endocde an image to base64 and insert it into one Markdown file.
# Filename cannot include " " (or Space).

import base64
import time

name = 'F'
pic_count = 1

while name == 'F':

	print("Which image do you pick?")

	pic_route = input().strip()
	name = 'T'

	route = pic_route.split('/')
	pic_name = route[-1]
	folder = pic_route.strip(pic_name)

	pic_name = pic_name.split('.')
	pic_extension = pic_name[-1]

	file_name = time.strftime('%Y%m%d',time.localtime())

	if (pic_extension == 'jpg')|(pic_extension == 'jpeg'):
		pic_type = 'jpeg'
	elif pic_extension == 'png':
		pic_type = 'png'
	else:
		print('Please check the extension of the image. Press "q" to quit.')
		name = 'F'
		if input() == 'q':
			print('Thanks fos using!')
			quit()

with open(pic_route,'rb') as pic_file:
	pic_base64 = base64.b64encode(pic_file.read())
with open(folder+file_name+'.md','w') as MD_file:
	MD_file.write('\n[pic_'+'%02d'%pic_count+']:data:image/'+pic_type+';base64,')
with open(folder+file_name+'.md','ab') as MD_file:
	MD_file.write(pic_base64)
with open(folder+file_name+'.md','a') as MD_file:
	MD_file.write('\n')

while 1 :

	print('Add another image? Press "y" to continue.[n]')
	signal = input()

	if (signal == 'yes')|(signal == 'y'):

		pic_count = pic_count+1
		name = 'F'

		while name == 'F':
			print("Which image do you pick?")
			pic_route = input().strip()
			name = 'T'
			pic_name = pic_route.split('.')
			pic_extension = pic_name[-1]

			if (pic_extension == 'jpg')|(pic_extension == 'jpeg'):
				pic_type = 'jpeg'
			elif pic_extension == 'png':
				pic_type = 'png'
			else:
				print('Please check the extension of the image. Press "q" to quit.')
				name = 'F'
				if input() == 'q':
					with open(folder+file_name+'.md','r+') as MD_file:
						content=MD_file.read()
						MD_file.seek(0,0)
						for i in range(1,pic_count):
							MD_file.write('\n![][pic_'+'%02d'%i+']\n')
						MD_file.write(content)
					print('Thanks fos using!')
					quit()

		with open(pic_route,'rb') as pic_file:
			pic_base64 = base64.b64encode(pic_file.read())
		with open(folder+file_name+'.md','a') as MD_file:
			MD_file.write('\n[pic_'+'%02d'%pic_count+']:data:image/'+pic_type+';base64,')
		with open(folder+file_name+'.md','ab') as MD_file:
			MD_file.write(pic_base64)
		with open(folder+file_name+'.md','a') as MD_file:
			MD_file.write('\n')
	else:
		with open(folder+file_name+'.md','r+') as MD_file:
			content=MD_file.read()
			MD_file.seek(0,0)
			for i in range(1,pic_count+1):
				MD_file.write('\n![][pic_'+'%02d'%i+']\n')
			MD_file.write('\n')
			MD_file.write(content)
		print('Thanks fos using!')
		quit()

