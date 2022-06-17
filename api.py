#импорты
import requests
import json

def api(url, headers):
	
	#get запрос
	resp = requests.get(url, headers=headers)
	a = resp.json()

	#вывод данных
	print('Nickname: ' + a['nickname'])
	print('Publick ID: ' + a['pubId'])
	print('URL page: ' + a['page'])
	print('Activity: ' + str(a['isActive']))
	print('Public: ' + str(a['isPublic']))
	print('Donate total amount: ' + str(a['donates']['totalAmount']))
	print('Donate total count: ' + str(a['donates']['totalCount']))
	print('Cteated at: ' + a['createdAt'])

if __name__ == '__main__':

	#нужные переменные
	url ='https://donatello.to/api/v1/me'
	headers={'X-Token':'token'}  #token from https://donatello.to/panel/doc-api
	api(url, headers)
