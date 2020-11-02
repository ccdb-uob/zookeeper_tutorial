from kazoo.client import KazooClient

import yaml

import logging

logging.basicConfig()

with open('config.yaml') as f:
    config = yaml.load(f)

cluster_ip = list(config['hosts'].keys())[0]

zk = KazooClient(hosts=f'{cluster_ip}:2181')

zk.start()


@zk.DataWatch("/app/leader")
def watch_node(data, stat):
    print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))


input("wait to quit:\n")
