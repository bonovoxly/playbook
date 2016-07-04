# ec2_vpc_route_table_issue_test

This playbooks tests the ```ec2_vpc_route_table``` module bug.  When an NAT instance is used as a default gateway for subnets and is then deleted, it leaves black hole route.  As of 02/20/2016, the [ec2_vpc_route fix](https://github.com/ansible/ansible-modules-extras/pull/1511) will not add the route; it will only delete the black hole route, even if you are specifying a new NAT instance as a route. If you run it a second time, it will add the new route. However, if ```routes_to_delete``` is run first:

~~~python
{% raw %}
if changed:
    for route in routes_to_delete:
        try:
            vpc_conn.delete_route(route_table.id,
                                  route.destination_cidr_block,
                                  dry_run=check_mode)
        except EC2ResponseError as e:
            if e.error_code == 'DryRunOperation':
                pass

    for route_spec in route_specs_to_create:
        try:
            vpc_conn.create_route(route_table.id,
                                  dry_run=check_mode,
                                  **route_spec)
        except EC2ResponseError as e:
            if e.error_code == 'DryRunOperation':
                pass
{% endraw %}
~~~

The new NAT will be created in one play.
