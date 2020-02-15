
import requests

import json



header = {"content-type": "application/json"}


api_url="https://api.jdoodle.com/v1/execute/"



class execute:
    def __init__(self,code,langauge,stdin):
        self.code=code
        self.stdin=stdin
        self.language=langauge
    
    def run(self):
        
        

        # code='''

        # ans=0
        # for i in range(10**10):
        #     ans+=1
        # print(ans)




        # '''
        
        program = {
            'script': self.code,
            'language': self.language,
            'stdin':self.stdin,
            'versionIndex': "0",
            'clientId': "c611922ce0d2e78065f2417285922322",
            'clientSecret':"1199aefb6f989dd2078566f6e249a29b2d21b52591c1b8017b9dc353be351bd0"
        }


        program=json.dumps(program)

        response = requests.post(api_url, data=program,headers=header)


        if response.status_code == 200:
                data= json.loads(response.content.decode('utf-8'))
        # print(data)

        return data