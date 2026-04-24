#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

import psycopg2


def run_module():
    module_args = dict(
        host=dict(type='str', required=True),
        port=dict(type='int', required=True),
        user=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        database=dict(type='str', required=True),
    )

    result = dict(
        changed=False,
        version=""
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    try:
        conn = psycopg2.connect(
            host=module.params['host'],
            port=module.params['port'],
            user=module.params['user'],
            password=module.params['password'],
            dbname=module.params['database']
        )

        cursor = conn.cursor()
        cursor.execute("SELECT version();")

        version = cursor.fetchone()[0]

        result["version"] = version

        cursor.close()
        conn.close()

        module.exit_json(**result)

    except Exception as e:
        module.fail_json(msg=str(e), **result)


def main():
    run_module()


if __name__ == '__main__':
    main()