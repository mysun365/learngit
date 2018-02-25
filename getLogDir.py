#! coding=utf-8
import os,re,subprocess
#递归遍历要查找的目录路径
def gci(path):
    li = []
    list1 = []
    list2 = []
    #递归查找日志文件路径
    parents = os.listdir(path)
    for parent in parents:
        child = os.path.join(path,parent)
        if os.path.isdir(child):
            gci(child)
        else:
            #把结果放到一个列表中
            li.append(child)
    for i in li:
        #判断文件是否是以yyyy-MM-dd结尾的日志文件
        try:
            str1 = re.search(r"(.log.\d{4}-\d{1,2}-\d{1,2})",i)
            if str1:
                if i not in list1:
                    list1.append(i)
        except AttributeError:
            pass
    #取元组首个元素，即日志文件所在父目录
    for i in list1:
        if os.path.split(i)[0] not in list2:
            list2.append(os.path.split(i)[0])
    for i in list2:
       subprocess.Popen("find %s -mtime +3 -name \"*.log.*\" -exec rm -rf {} \\;" % i,shell=True)
       #print "find %s -mtime +3 -name \"*.log.*\" -exec rm -rf {} \\;" %i
gci("/hskj")
