import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_webapp_copies(host):
    showcase = host.file('/opt/tomcat/webapps/showcase.war')
    assert showcase.exists
    assert showcase.is_symlink


def test_service(host):
    tomcat = host.service('tomcat')
    assert tomcat.is_running


def test_curl_output(host):
    cmd = 'curl -o -I -L -s -w "%{http_code}\n" http://localhost:8080/showcase'
    assert host.check_output(cmd) == '200'
    cmd = 'curl -L http://localhost:8080/showcase'
    assert host.check_output(cmd).find(u'userdata') > -1
