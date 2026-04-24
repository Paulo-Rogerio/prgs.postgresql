#!/usr/bin/env bash

ansible --version
ansible-playbook -i inventory.ini cluster.yml
