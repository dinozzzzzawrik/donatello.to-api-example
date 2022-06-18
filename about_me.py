import requests

def api(url, headers):

    resp = requests.get(url, headers=headers)
    a = resp.json()

    print('Nickname: ' + a['nickname'] +
          '\nURL page: ' + a['page'] +
          '\nActivity: ' + str(a['isActive']) +
          '\nPublic: ' + str(a['isPublic']) +
          '\nDonate total amount: ' + str(a['donates']['totalAmount']) +
          '\nDonate total count: ' + str(a['donates']['totalCount']) +
          '\nCreated at: ' + a['createdAt']
          )

if __name__ == '__main__':
    url = 'https://donatello.to/api/v1/me'
    headers = {'X-Token': 'token'}  # token from https://donatello.to/panel/doc-api
    api(url, headers)
