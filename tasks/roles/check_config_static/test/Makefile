TOWER_VERSION_EXTRAS='-e "tower_package_name=ansible-tower" -e "tower_package_version=2.4.1" -e "tower_package_release=1"'
INVENTORY='../../../inventory'

all: test_default test_ha_fail test_external_db

test_default:
	# TODO: cd .. to ensure shipped inventory works and host_vars/group_vars works
	ansible-playbook -i ${INVENTORY} ${TOWER_VERSION_EXTRAS} default.yml

test_ha_fail:
	# TODO: Figure out a better way to test failure cases. We want to test that the task intended to fail is one that actually fails
	#ansible-playbook -i ${INVENTORY} ${TOWER_VERSION_EXTRAS} --tags add_secondary,check_config_static_ha_pg ha_fail.yml || (exit `echo 2-$$? | bc`)

test_external_db:
	ansible-playbook -i ${INVENTORY} ${TOWER_VERSION_EXTRAS} external_db.yml
