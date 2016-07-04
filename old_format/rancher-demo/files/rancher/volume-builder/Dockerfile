FROM centos:latest
# make directories
RUN mkdir -p /tmp/nginx-conf && mkdir -p /tmp/logstash-config && mkdir -p /tmp/kibana-conf && mkdir -p /tmp/elasticsearch-data

# nginx
COPY files/nginx-conf/nginx.conf /tmp/nginx-conf/nginx.conf
COPY files/gluster-launcher.sh /tmp/gluster-launcher.sh

# logstash
COPY files/logstash-conf/* /tmp/logstash-conf/

# kibana
COPY files/kibana-conf/* /tmp/kibana-conf/

# elasticsearch

# final
RUN chmod a+x /tmp/gluster-launcher.sh
