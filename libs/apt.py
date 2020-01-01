import os,sys

class aptset():
    def install(package_name):
        os.system('apt install'+package_name+'-y')
    def clean():
        os.system('apt autoremove -y && apt autoclean -y')
