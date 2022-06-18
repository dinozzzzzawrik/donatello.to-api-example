import requests

def api(url, headers):

    resp = requests.get(url, headers=headers)
    a = resp.json()

    for i in a['clients']:
        print('Name: ' + str(i['clientName']) +
              '\nTotal amount: ' + str(i['totalAmount']) +
              '\n\n'
              )

if __name__ == '__main__':
    url = 'https://donatello.to/api/v1/clients'
    headers = {'X-Token': 'token'}  # token from https://donatello.to/panel/doc-api
    api(url, headers)