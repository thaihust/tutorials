- Env:
```sh
apt-get install -y python python-pip
pip install requests
```

```sh
cat /etc/sysctl.conf | egrep -v "^$|^#"
vm.max_map_count=262144
```
