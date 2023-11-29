# Allow the holberton user to log in and open files without error messages

# Ensure the holberton user exists
user { 'holberton':
  ensure     => 'present',
  managehome => true,
  home       => '/home/holberton',
  shell      => '/bin/bash',
}
# Increase hard file limit for Holberton user.
exec { 'increase-hard-file-limit':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

# Increase soft file limit for Holberton user.
exec { 'increase-soft-file-limit':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

