"""Module for tests related to tower."""
# pylint: disable-msg=C0103
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_hosts_file(File):
    """Test for the presence of a hosts file."""
    hosts_file = File('/etc/hosts')

    if not hosts_file.exists:
        raise AssertionError()

    if not hosts_file.user == 'root':
        raise AssertionError()

    if not hosts_file.group == 'root':
        raise AssertionError()


def test_ansible_is_installed(File):
    """Test for the presence of an Ansible executable."""
    ansible_file = File('/usr/bin/ansible')

    if not ansible_file.exists:
        raise AssertionError()


def test_tower_downloaded(File):
    """Test for the presence of a Tower download."""
    tower_directory = File('/opt/tower')

    if not tower_directory.exists:
        raise AssertionError()
