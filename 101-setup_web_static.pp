# Installs nginx

file { 'index.html':
  path    => '/data/web_static/releases/test/index.html',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => 'hello holberton!'
}

package { 'nginx':
  provider => gem
}
