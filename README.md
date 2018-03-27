Mellophone
=========

[![Build Status](https://ci.corchestra.ru/buildStatus/icon?job=mellophoneansible/master)](https://ci.corchestra.ru/job/mellophoneansible/job/master/)

Installation of [Mellophone](https://corchestra.ru/wiki/index.php?title=Mellophone) platform in Tomcat. This role should be run after [CourseOrchestra.tomcat](https://galaxy.ansible.com/CourseOrchestra/tomcat/).

Requirements
------------

* Java 8
* Tomcat (provided by [CourseOrchestra.tomcat](https://galaxy.ansible.com/CourseOrchestra/tomcat/) role)


Role Variables
--------------

* mellophone_build: Mellophone build number
* mellophone_config_src: path to configuration file to be copied to server

Example Playbook
----------------

    - hosts: servers
      vars:
         oracle_java_version: 8
         oracle_java_version_update: 131
         mellophone_config_src: config.xml
      roles:
         - role: ansiblebit.oracle-java
         - role: CourseOrchestra.tomcat
         - role: CourseOrchestra.mellophone

License
-------

MIT

Author Information
------------------

https://corchestra.ru/en
