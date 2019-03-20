# This program is used creat a new template page for the blog using jekyll.

import time

print('Please give the name to the new page...')

name = input()

file_name = time.strftime('%Y-%m-%d-'+name+'.md',time.localtime())

print(file_name)

with open('_posts/'+file_name,'w') as MD_file:
	MD_file.write('---\n')
	MD_file.write('layout: \n')
	MD_file.write('title: "'+name+'"\n')
	MD_file.write('date: '+time.strftime('%Y-%m-%d %H:%M:%S +0800',time.localtime())+'\n')
	MD_file.write('tags: [untagged]\n')
	MD_file.write('categories: [uncategorized]\n')
	MD_file.write('description: No description\n')
	MD_file.write('---\n\n')