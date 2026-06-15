---
- name: Install Jenkins on Ubuntu
  hosts: all
  become: yes
  vars:
    java_package: openjdk-17-jdk

