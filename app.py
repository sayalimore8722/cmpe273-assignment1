import sys
from flask import Flask
from github import Github
import base64

app = Flask(__name__)

@app.route('/v1/<filename>')
def home(filename):
      g = Github(login_or_token="f8cfc35809d225b1c375a6b888e837f020ffdbd1")
      for repo in g.get_user().get_repos():
	s=format(app.config.get('github_path'))
	termstr1=s.rsplit('/',1)
	
	if repo.name==termstr1[1]:
 	 return base64.b64decode(repo.get_file_contents(filename).content)
	

if __name__ == '__main__':
    app.config['github_path'] = sys.argv[1]
    app.run(debug=True,host='0.0.0.0')




