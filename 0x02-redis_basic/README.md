## 0x02-redis_basic

![image](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbF0TXEtRHxJdexE72U649qhLBxHVuT5WCODzeEsARShsb85HbJ-LlPUogeaPuHVeMct4&usqp=CAU)

## Resources

- [Redis commands](https://intranet.alxswe.com/rltoken/lQ8ANhVfxDTxDr2UDSyQRA)

- [Redis python client](https://intranet.alxswe.com/rltoken/imfgFhAZPlg7YMZ_tHvFZw)

- [How to Use Redis With Python](https://intranet.alxswe.com/rltoken/7SluvFvgckwVgsvrfOf1CQ)

- [Redis Crash Course Tutorial](https://intranet.alxswe.com/rltoken/hJVo3XwMMFFoApyX8zPXvA)

## Install Redis on Ubuntu 18.04
```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

## Use Redis in a container
- Redis server is stopped by default - when you are starting a container, you should start it with: service redis-server start

## Install Redis on ubuntu 22.04
- [Install Redis](https://linuxhint.com/install-configure-redis-ubuntu-22-04/)
