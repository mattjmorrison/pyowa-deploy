set :deploy_to, '/var/www/pyowa'
set :django_settings, 'base'

role :web, "198.61.232.149", {
  :user => 'root',
  :password => 'pyowa'
}
