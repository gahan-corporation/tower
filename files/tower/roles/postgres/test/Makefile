INVENTORY ?= 'inventory'

.PHONY: test_postgres_default \
	test_postgres_credentials_change \
	requirements

all: test_postgres_default \
	test_postgres_credentials_change

LOG_DIR=./logs

clean:
	rm -f $(LOG_DIR)/*.log

# Log all ansible test invocations
test_%: export ANSIBLE_LOG_PATH=$(LOG_DIR)/$@.log

requirements:
	ansible-galaxy install -r requirements.yml -p ./roles --force

test_postgres_default: export INVENTORY=inventory
test_postgres_default:
	ansible-playbook -i ${INVENTORY} ${EXTRAS} --skip-tags="packages_ubuntu_apt_install_tower,packages_el_yum_install_tower" test_default.yml

test_postgres_credentials_change: export INVENTORY=inventory_credentials_change
test_postgres_credentials_change:
	ansible-playbook -i ${INVENTORY} ${EXTRAS} --skip-tags="packages_ubuntu_apt_install_tower,packages_el_yum_install_tower" test_credentials_change.yml

test_postgres_no_password: export INVENTORY=inventory_no_password
test_postgres_no_password:
	ansible-playbook -i ${INVENTORY} ${EXTRAS} --skip-tags="packages_ubuntu_apt_install_tower,packages_el_yum_install_tower" test_no_password.yml
