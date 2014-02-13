set :deploy_to, '/var/www/pyowa'

role :web, "198.61.232.149", {
  :user => 'root',
  :password => 'pyowa'
}
