import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')
curl_cmd = 'curl -o -I -L -s -w "%{http_code}\n" '


def test_webapp_copies(host):
    mellophone = host.file('/opt/tomcat/webapps/mellophone.war')
    assert mellophone.exists
    assert mellophone.is_symlink


def test_service(host):
    tomcat = host.service('tomcat')
    assert tomcat.is_running


def test_mellophone_greeting(host):
    cmd = curl_cmd + 'http://localhost:8080/mellophone'
    assert host.check_output(cmd) == '200'
    cmd = "curl -L 'http://localhost:8080/mellophone'"
    assert host.check_output(cmd).find(u'Mellophone') > -1


def test_mellophone_works(host):
    cmd = curl_cmd + "'localhost:8080/mellophone/checkcredentials" \
                     "?pwd=kulkov&login=kulkov'"
    assert host.check_output(cmd) == '200'
    cmd = curl_cmd + "'localhost:8080/mellophone/checkcredentials" \
                     "?pwd=kulkov&login=kulkov2'"
    assert host.check_output(cmd) == '403'
