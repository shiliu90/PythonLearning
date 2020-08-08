#  git

## 安装

### mac

1. 查看是否安装

108

   ```git
   shi@shideimac ~ % git --version
   git version 2.24.2 (Apple Git-127) 如果有说明已经安装，没有则下载安装
   shi@shideimac ~ % which git  查看目录
   /usr/bin/git
   ```

1.1 附 mac 终端 推荐 Iterm2 

   ```git
   shi@shideimac / % brew cask install iterm2
   直接安装
   ```

## 新建文件夹 用来 git 管理
   cd Desktop/    就是进入到Desktop 目录
   cd ..   返回
   pwd       查看当前路径
   mkdir /user/用户名/要建立的文件夹名字
   ls     显示当前目录的内容





## 新电脑的操作

1. 新建目录（用于保存线上的文件夹和文件）

![image-20200808193948368](/Users/shi/Library/Application Support/typora-user-images/image-20200808193948368.png)

2. 克隆 线上文件

   git clone + 自己github库地址

   ```git
   git clone https://github.com/shiliu90/PythonLearning.git
   ```

   ![image-20200808194132043](/Users/shi/Library/Application Support/typora-user-images/image-20200808194132043.png)

3. ```git
   cd PythonLearning     --> 进入文件夹
   ```

4. ```git
   cat 文件名.格式         --> 打开某个文
   ```

5. ```git
   git log               --> 版本信息
   ```
   
6. ```git
   git branch           --> 查看当前的分支有多少   master 主分支
   ```

   ![image-20200808194644974](/Users/shi/Library/Application Support/typora-user-images/image-20200808194644974.png)

7. ```git
   git checkout dev(分支名)   --> 切换到分支
   ```

8. ```git
   提交代码
   git add .        -->  添加当前文件夹下所有的 文件
   
   git commit -m "提示的版本信息" 
   
   git push origin master    --> 推送到主支   又分支 git push origin dev --> 推到分支
   
   
   第2天到单位
   与上面推到的主，分支同步 如果是主支
   git pull origin master
   如果是分支
   git checkout dev
   git pull origin dev
   
   
   ....
   ```

