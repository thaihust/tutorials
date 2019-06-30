```sh
cat /etc/sysctl.conf | egrep -v "^$|^#"
vm.max_map_count=262144
```
