import os
from fabric.api import *
from fabric.operations import get, put
from fabric.contrib.console import confirm
from fabric.contrib.project import rsync_project
from fab_settings import SUDOER_USER


env.roledefs = {
    'jellyrisk': ['jellyrisk@jellyrisk.com'],
    'sudoer': ['%s@jellyrisk.com' % SUDOER_USER]
    }
env.hosts = ['jellyrisk.com']
env['project_name'] = 'jellyrisk'
env['project_path'] = "/home/" + env['project_name'] + "/www/" + env['project_name'] + "/"
env['python_path'] = "/home/" + env['project_name']+ "/.virtualenvs/" + env['project_name'] + "/bin/python"
env['pip_path'] = "/home/" + env['project_name'] + "/.virtualenvs/" + env['project_name'] + "/bin/pip"
env['project_media_dir'] = '/var/www/jellyrisk/media/'


@roles('jellyrisk')
def git_status():
    with cd(env['project_path']):
        run('git fetch && git status') 


@roles('jellyrisk')
def pushpull():
    local("git push origin master")
    with settings(user='jellyrisk'):
        with cd(env['project_path']):
            run('git pull') 


@roles('sudoer')
def reloadapp():
    sudo('supervisorctl restart jellyrisk', shell=False)
    sudo('service nginx reload', shell=False) 


@roles('jellyrisk')
def release(run_migrate=True, static=True):
    pushpull()
    run('%s install -r %spip-requirements.txt' % 
        (env['pip_path'], env['project_path']))
    with cd(env['project_path']):
        if run_migrate:
            migrate()
        if static:
            _run_manage('collectstatic --noinput')
    reloadapp()


@roles('jellyrisk')
def migrate():
    with cd(env['project_path']):
        _run_manage('migrate')


@roles('jellyrisk')
def pulldb():
    filename = 'mysql_dumped.sql'
    dump_file = '%s' % filename
    run(_dump_mysql_data(dump_file))
    get(dump_file, '.')
    run('rm %s' % dump_file)
    if confirm("Load dumped remote data into local DB?"):
        local('mysql --defaults-file=".mysqldump_cnf" %s < %s' % (env['project_name'], filename))
            

def _run_manage(command):
    run("%s ./manage.py %s" % (env['python_path'], command))

def _dump_mysql_data(file_path):
    return 'mysqldump --defaults-file="/home/jellyrisk/.mysqldump_cnf" --single-transaction jellyrisk > %s' % file_path

@roles('jellyrisk')
def syncmedia():
    get(env['project_media_dir'], local_path=".")
