import requests

baseurl = "https://core.labplatform.vmware.com"

def updateacount():

    #Login
    encoded_string = {'base64encodestring'}   #modify this line with the actual base64encode string
    loginurl = baseurl+"/api/login"
    headers = {
        "Authorization": f"Basic {encoded_string}"
    }
    loginreq = requests.post(url=loginurl, headers=headers)

    # Fetch unverfied accounts, filter using @ascendcloudsolutions.com, change the verify status to True and use PUT to make changes
    accountsurl = baseurl+'/api/admin/accounts?tenant=acs-labs&accountVerified=False&limit=100'
    neetokhdr = {
        'Cookie': loginreq.headers['Set-Cookie']
    }
    accountsreq = requests.get(url=accountsurl, headers=neetokhdr)
    for i in accountsreq.json()['data']:
        if '@ascendcloudsolutions.com' in i['username']:
            i['accountVerified']=True
            updateaccurl = baseurl+f'/api/admin/accounts?tenant=acs-labs&username={i['username']}'
            updatereq = requests.put(url=updateaccurl, headers=neetokhdr, json=i)
            print(updatereq.json())



if __name__ == '__main__':
    updateacount()
