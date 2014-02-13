set :deploy_to, '/var/www/pyowa'
set :django_settings, 'production'

role :web, "198.61.231.106", {
  :user => 'root',
  :password => 'test'
}
