import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'GreyMatters_Bot'

#Ex https://MS-DZULQURNAIN:ghp_147bkkabcdefgh@github.com/MS-DZULQURNAIN/FILE-SHARING
os.system("git clone https://GITHUB-USERNAME:token@github.com/GITHUB-USERNAME/YOUR-REPO-NAME okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 main.py &")
