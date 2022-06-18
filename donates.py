import requests

def api(url, headers):

    resp = requests.get(url, headers=headers)
    a = resp.json()

    for i in a['content']:
        print( 'Никнейм: ' + i['clientName'] +
               '\nСума: ' + i['amount'] +
               '\nВалюта: ' + i['currency'] +
               '\nДата отправки: ' + i['createdAt'] +
               '\nКоментарий: ' + i['message'] +
               '\n\n'
               )

if __name__ == '__main__':
    url = 'https://donatello.to/api/v1/donates'
    headers = {'X-Token': 'token'}  # token from https://donatello.to/panel/doc-api
    api(url, headers)