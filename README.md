Tower Installation
==================
[![Build Status](https://travis-ci.org/gahan-corporation/tower.svg?branch=master)](https://travis-ci.org/gahan-corporation/tower)

Installs the latest version of Ansible Tower onto an Ubuntu 16.04 target.

Requirements
------------

The `molecule` Python library is required for testing.

Role Variables
--------------

None.

Dependencies
------------

```yaml
role: gahan-corporation.postgresql
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - { role: gahan-corporation.tower }
```

License
-------

GPL-3.0

Author Information
------------------

Authored by A. H. Laughlin for the [Gahan Corporation](https://gahan-corporation.com).
