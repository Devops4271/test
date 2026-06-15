---
- name: Install Jenkins on Ubuntu
  hosts: all
  become: yes


- name: Install Java (Jenkins prerequisite)
      apt:
        name: "{{ java_package }}"
        state: present

