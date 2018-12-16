import csv,sys,os 

project_dir = "/home/has/site1/mysite/" # переменая, в которой сохраняем путь до проекта джанго

sys.path.append(project_dir) # добавляем путь в переменную sys.path

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings' # подключаем настройки нашего проекта джанго

import django

django.setup() #добавляем текущие настройки джанго

from blog.models import Post  #подключаем из модели наш созданный класс Пост

file = csv.reader(open(os.path.join('data.csv')), delimiter=",") # счтываем файл, для чего указываем путь к файлу и параметром delimiter, указываем разделитель
	
#os.path.join(BASE_DIR, 'db.sqlite3')

#пишем цикл переборки строк
for row in file:
	if row[0] != 'created_date':  #пропускаем первую строку, т.к. там заголовки
		post = Post()
		# #post.author = row[0]
		post.created_date = row[0]
		post.title = row[1]
		post.text = row[2]
		post.save() #сохраняем






