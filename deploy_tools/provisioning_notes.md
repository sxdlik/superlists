配置新网站
=======================

## 需要的包

* **nginx**
* **Python3**
* **virtualenv + pip**
* **Git**

以 **Ubuntu** 为例：

    sudo apt install nginx
    suod apt install python3-venv

## Nginx 虚拟主机

* 参考 **nginx.template.conf** 
* 把 **SITENAME** 替换成所需的域名，例如 **superlist-test.cr**

## Systemd 服务

* 参考 **gunicorn-systemd.template.service**
* 把 **SITENAME** 替换成所需的域名，例如 **superlists-test.cr**

## 文件夹结构

假设有用户帐户，家目录为 **/hone/username**

    /home/username
    L____ sites
        L____ SITENAME
            L____ database
            L____ source
            L____ static
            L____ virtualenv