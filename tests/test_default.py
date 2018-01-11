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

    assert f.user == 'root'
    assert f.group == 'root'


def test_ansible_is_installed(File):
    f = File('/usr/bin/ansible')

    assert f.exists


def test_tower_downloaded(File):
    f = File('/tmp/ansible')

    assert f.exists
