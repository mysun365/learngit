# github的使用

## 配置sshkey

生成key:ssh -keygen -t rsa -C "邮箱地址"，一路回车

cd ~/.ssh (用户目录下的.ssh文件夹)

复制id_rsa.pub公钥内容github网站中

## 配置多个sshkey

cd ~/.ssh

vim config

添加 Host/HostName/User/IdentityFile

Host github.com

HostName github.com

User mysun365

IdentityFile /root/.ssh/id_rsa



## 常用操做

git status 查看当前状态

git add 推送到工作区

git commit -m "注释"

git push 推送到远程

git pull 拉取到本地



## 如何创建分支

git checkout -b fengzhi 创建分支

git branch 查看分支

git branch -a  查看所有本地和远程分支

git push --set-upstream origin 分支名称   //从本地创建远程分支





## 项目分支操作

#### 删除本地分支

1、切换到master分支

2、git branch -d 分支 //注意：仅仅删除本地分支，远程分支没有删除



#### 删除远程分支

git branch -r -d origin/分支

git push origin :分支  //注意origin后需要加一个空格



## git合并分支操作

分支之间相互独立，互不影响

那当前分支如何与要合并的分支进行合并呢？

git merge 要合并的分支名称



### 合并分支的冲突问题



master分支与其他分支在某个文件某行中出现冲突

git merge 要合并分支时，提示合并分支引起冲突

> fatal: Exiting because of an unresolved conflict.

> 文件内容：
>
> test
> test
> sdfsdf
> xinghui
> <<<<<<< HEAD
>
> this is cont
>
> this is xx branch content
>
> > > >xx





## 项目的版本操作

### 版本回退



git reset --hard HEAD^

^表示上一个版本

回退到指定版本：

git reflog 得到版本号

git reset --hard 版本号

