import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_hosts_file(File):
    f = File('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_hosts_file(File):
    f = File('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_java_is_installed(File):
    java = File('/usr/lib/jvm/java-8-oracle')

    assert java.exists


def test_ansible_is_installed(File):
    f = File('/usr/bin/ansible')

    assert f.exists


def test_tower_downloaded(File):
    f = File('/tmp/ansible')

    assert f.exists
