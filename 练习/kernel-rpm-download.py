# encoding = utf-8
__author__ = "Ang Li"

import os
import time

import requests


class PackegeDownload(object):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # 根路径
    kernel_list_file = os.path.join(BASE_DIR,'kernel-use.list') # rpm 包列表
    #kernel_list_file = os.path.join(BASE_DIR,'test_list') # rpm 包列表
    download_url = "http://debuginfo.centos.org/7/x86_64/" # 下载url
    #download_url = "http://10.159.63.219/CentOS-Yum/centos/7/os/x86_64/extras/Packages/" # 下载url
    coding = 'utf-8'

    def __init__(self):
        self.total_quantity = 100
        self.already_down = 0
        self.ok_status = 0
        self.fail_status = 0
        self.log_file = os.path.join(self.BASE_DIR, "package_download.log")  # 下载日志
        self.download_dir = os.path.join(self.BASE_DIR, 'downloads')

        if not os.path.exists(self.download_dir):
            os.mkdir(self.download_dir)

        for index,line in enumerate(open(self.kernel_list_file,'r')):
            self.total_quantity += 1

    def format_float(self,num):
        return '{:.2f}'.format(num)

    def download_file(self, package_path, package_url):
        self.package_path = package_path
        self.package_url = package_url

        headers = {'Proxy-Connection': 'keep-alive'}
        r = requests.get(self.package_url, stream=True, headers=headers)
        length = float(r.headers['content-length'])
        with open(self.package_path,'wb') as f:
            count = 0
            count_tmp = 0
            time1 = time.time()
            for chunk in r.iter_content(chunk_size=512):
                if chunk:
                    f.write(chunk)
                    count += len(chunk)
                    if time.time() - time1 > 1:
                        p = count / length * 100
                        speed = (count - count_tmp) / 1024 / 1024 / 2
                        count_tmp = count
                        print(self.package_name + ': ' + self.format_float(p) + '%' + ' Speed: ' + self.format_float(speed) + 'M/S')
                        time1 = time.time()

    def run(self):
        with open(self.kernel_list_file,'r') as f:
            for line in f:
                package_list = line.split()
                self.package_name = package_list[0] # 包名
                package_size = package_list[3] # 包大小
                package_url = self.download_url + self.package_name # 包url

                with open(self.log_file,'a+', encoding=self.coding) as log:
                    self.last_downs = self.total_quantity - self.already_down
                    print("开始下载 %s, \n总量: %s, 已下载: %s, 剩余: %s\n" % (
                    self.package_name, self.total_quantity, self.already_down, self.last_downs))
                    log.write("%s 开始下载 %s, 大小为 %s \n" % (time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),
                                                        self.package_name, package_size))

                package_path = os.path.join(self.download_dir, self.package_name)
                download = requests.get(package_url)

                self.download_file(package_path, package_url)
                self.already_down += 1

d1 = PackegeDownload()
d1.run()

# H:\python-stu\练习\kernel-rpm-download.py