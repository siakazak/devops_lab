import requests
import getpass
from os import path


class GithubUser:

    def __init__(self):
        if path.exists("./pr-stats.login"):
            with open('./pr-stats.login', "r") as outfile:
                self.login = outfile.read()
        else:
            self.login = input('GitHub Login: ')
            if input('Remember login? y/N: ') == 'y':
                with open('./pr-stats.login', "w") as outfile:
                    outfile.write(self.login)
                print('Login stored in ./pr-stats.login')
                print('In order to change it just remove the file')
        self.passwd = getpass.getpass(prompt='Password: ', stream=None)

        while requests.get('https://api.github.com/user',
                           auth=(self.login, self.passwd)).status_code != 200:
            print('Invalid password - try again')
            self.passwd = getpass.getpass(prompt='Password:', stream=None)

        self.user = self.login
        self.repo = None
        self.commits = False
        print('Logged in as', self.login, '\n')

    def get_repos(self):
        rj = requests.get('https://api.github.com/users/%s/repos?page=1&per_page=100' % self.user,
                          auth=(self.login, self.passwd)).json()
        print("%s's repos list(%d):" % (self.user, len(rj)))
        for i in range(len(rj)):
            print("%d:" % (i + 1), 'Name: %s' % rj[i]['name'], 'URL: %s' % rj[i]['svn_url'],
                  sep='\n')

    def get_repo(self):
        r = requests.get('https://api.github.com/repos/%s/%s' % (self.user, self.repo),
                         auth=(self.login, self.passwd))
        rj = r.json()
        if r.status_code != 200:
            print("ERROR: user %s doesn't have a repo named '%s'" %
                  (self.user, self.repo))
            exit(1)
        else:
            print("%s's [%s] - %s\n"
                  % (rj['owner']['login'], rj['name'], rj['html_url']))

    def get_branches(self):
        rj = requests.get('https://api.github.com/repos/%s/%s/branches?page=1&per_page=100'
                          % (self.user, self.repo), auth=(self.login, self.passwd)).json()
        print('branches list (%s):' % len(rj))

        for i in range(len(rj)):
            print('%d:' % (i + 1))
            print('Name: %s' % rj[i]['name'])
            print('URL: https://github.com/%s/%s/tree/%s' %
                  (self.user, self.repo, rj[i]['name']))
        print()

    def get_labels(self):
        rj = requests.get('https://api.github.com/repos/%s/%s/labels' % (self.user, self.repo),
                          auth=(self.login, self.passwd)).json()
        print('labels list (%s):' % len(rj))

        for i in range(len(rj)):
            print("'%s'" % rj[i]['name'])

        print()

    def get_pulls(self):
        rj = requests.get('https://api.github.com/repos/%s/%s/pulls?page=1&per_page=100'
                          % (self.user, self.repo), auth=(self.login, self.passwd)).json()
        print('pull requests (%s):' % len(rj))

        for i in range(len(rj)):
            print('%d:' % (i + 1))
            print("Title: '%s'" % rj[i]['title'])
            print('Status:', rj[i]['state'])
            print('Created:', str(rj[i]['created_at']).replace(
                'T', ' at ').replace('Z', ' '))
            labels = ''
            for ll in rj[i]['labels']:
                labels += "'" + ll['name'] + "' "
            print('Labels:', labels)
            print('URL:', rj[i]['html_url'])
            if self.commits:
                commits = rj[i]['commits_url']
                rcj = requests.get(commits, auth=(
                    self.login, self.passwd)).json()
                print('Commits (%d):' % len(rcj))
                print()
                for cc in range(len(rcj)):
                    print('%d:' % (cc + 1))
                    print('\tCommitter: ', rcj[cc][
                          'commit']['committer']['name'])
                    print('\tDate: ', rcj[cc]['commit']['committer']['date'].replace('T', ' at ')
                          .replace('Z', ''))
                    print('\tMessage: ', "'%s'" % rcj[cc]['commit']['message'])
                    print('\tComments: ', rcj[cc]['commit']['comment_count'])
                    print('\tURL: ', rcj[cc]['html_url'])
            print()

    def get_time(self):
        rj = requests.get('https://api.github.com/repos/%s/%s' % (self.user, self.repo),
                          auth=(self.login, self.passwd)).json()
        print('access info:')
        print('Created on:', str(rj['created_at']).replace(
            'T', ' at ').replace('Z', ''))
        print('Updated on:', str(rj['updated_at']).replace(
            'T', ' at ').replace('Z', ''))
        print('Pushed on:', str(rj['pushed_at']).replace(
            'T', ' at ').replace('Z', ''))
        print()

    def __str__(self):
        rj = requests.get('https://api.github.com/users/%s' % self.user,
                          auth=(self.login, self.passwd)).json()

        return 'user info:\nLogin: %s\nID: %d\nName: %s\nCompany: %s\nLocation: %s\
        \nFollowers: %s\nEmail: %s\nCreated: %s\nURL: %s\n' \
        % (rj['login'], rj['id'], rj['name'], rj['company'], rj['location'],
            rj['followers'], rj['email'],
            rj['created_at'].replace('T', ' at ').replace('Z', ''), rj['html_url'])
