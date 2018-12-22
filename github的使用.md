# github的使用

## 配置sshkey

生成key:ssh -keygen -t rsa -C "邮箱地址"，一路回车

cd ~/.ssh (用户目录下的.ssh文件夹)

复制id_rsa.pub公钥内容github网站中

## 配置多个sshkey

cd ~/.ssh

vim config

添加 Host/HostName/User/IdentityFile

