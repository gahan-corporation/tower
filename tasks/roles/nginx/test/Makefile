.PHONY: test_httpd_password_change \
	test_httpd_no_password_change \
	requirements

all: test_httpd_password_change test_httpd_no_password

LOG_DIR=./logs

clean:
	rm -f $(LOG_DIR)/*.log

# Log all ansible test invocations
test_%: export ANSIBLE_LOG_PATH=$(LOG_DIR)/$@.log

requirements:
	ansible-galaxy install -r requirements.yml -p roles/ --force

test_httpd_password_change: export INVENTORY=inventory_password_change
test_httpd_password_change:
	ansible-playbook -i ${INVENTORY} ${EXTRAS} test_password_change.yml

test_httpd_no_password: export INVENTORY=inventory_no_password
test_httpd_no_password:
	ansible-playbook -i ${INVENTORY} ${EXTRAS} test_no_password.yml
