#!/bin/bash
# nginx
/bin/cp -rf /tmp/nginx-conf/nginx.conf /opt/nginx-conf/nginx.conf

# logstash
/bin/cp -rf /tmp/logstash-conf/* /opt/logstash-conf/

# kibana
/bin/cp -rf /tmp/kibana-conf/* /opt/kibana-conf/

# elasticsearch
