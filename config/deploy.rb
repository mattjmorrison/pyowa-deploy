set :application, 'pyowa'
set :scm, :git
set :repo_url, 'git@github.com:mattjmorrison/pyowa.git'
set :django_project_dir, 'pyowa'
set :django_settings_dir, 'pyowa/settings'
set :wsgi_path, 'pyowa'
set :pip_requirements, 'requirements.txt'
set :compilemessages, true

set :deploy_to, '/var/www/pyowa'

role :web, "198.61.232.149"
set :user, 'root'
set :password, 'pyowa'
