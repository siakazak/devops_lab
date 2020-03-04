import requests
import getpass
import os.path
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

        print('Logged in as', self.login, '\n')

    def get_repos(self, user):
        rj = requests.get('https://api.github.com/users/' +
                          user + '/repos', auth=(self.login, self.passwd)).json()
        print("%s's repos list(%d):" % (user, len(rj)))
        for i in range(len(rj)):
            print("%d:" % (i + 1), 'Name: %s' % rj[i]['name'], 'URL: %s' % rj[i]['svn_url'],
                  sep='\n')

    def get_repo(self, user, repo):
        r = requests.get('https://api.github.com/repos/%s/%s' % (user, repo),
                         auth=(self.login, self.passwd))
        rj = r.json()
        if r.status_code != 200:
            print("ERROR: user %s doesn't have a repo named '%s'" % (user, repo))
            exit(1)
        else:
            print("%s's [%s] - %s\n"
                  % (rj['owner']['login'], rj['name'], rj['html_url']))

    def get_branches(self, user, repo):
        rj = requests.get('https://api.github.com/repos/%s/%s/branches' % (user, repo),
                          auth=(self.login, self.passwd)).json()
        print('branches list (%s):' % len(rj))

        for i in range(len(rj)):
            print('%d:' % (i + 1))
            print('Name: %s' % rj[i]['name'])
            print('URL: https://github.com/%s/%s/tree/%s' %
                  (user, repo, rj[i]['name']))
        print()

    def get_labels(self, user, repo):
        rj = requests.get('https://api.github.com/repos/%s/%s/labels' % (user, repo),
                          auth=(self.login, self.passwd)).json()
        print('labels list (%s):' % len(rj))

        for i in range(len(rj)):
            print("'%s'" % rj[i]['name'])

        print()

    def get_pulls(self, user, repo):
        rj = requests.get('https://api.github.com/repos/%s/%s/pulls' % (user, repo),
                          auth=(self.login, self.passwd)).json()
        print('pull requests (%s):' % len(rj))

        for i in range(len(rj)):
            print('%d:' % (i + 1))
            print("Title:\t\t'%s'" % rj[i]['title'])
            print('Status:', rj[i]['state'], sep='\t\t')
            print('Created:', str(rj[i]['created_at']).replace('T', ' at ').replace('Z', ' '),
                  sep='\t')
            labels = ''
            for ll in rj[i]['labels']:
                labels += "'" + ll['name'] + "' "
            print('Labels:', labels, sep='\t\t')
        print()

    def get_time(self, user, repo):
        rj = requests.get('https://api.github.com/repos/' + user +
                          '/' + repo, auth=(self.login, self.passwd)).json()
        print('access info:')
        print('Created on:', str(rj['created_at']).replace(
            'T', ' at ').replace('Z', ''))
        print('Updated on:', str(rj['updated_at']).replace(
            'T', ' at ').replace('Z', ''))
        print('Pushed on:', str(rj['pushed_at']).replace(
            'T', ' at ').replace('Z', ''))
        print()

    def __str__(self):
        rj = requests.get('https://api.github.com/users/%s' % args.user,
                          auth=(self.login, self.passwd)).json()

        return 'user info:\nLogin: %s\nID: %d\nName: %s\nCompany: %s\nLocation: %s\n\
        Followers: %s\nEmail: %s\nCreated: %s\nURL: %s\n' \
        % (rj['login'], rj['id'], rj['name'], rj['company'], rj['location'],
            rj['followers'], rj['email'],
            rj['created_at'].replace('T', ' at ').replace('Z', ''), rj['html_url'])
