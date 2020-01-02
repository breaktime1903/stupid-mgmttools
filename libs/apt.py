import os,sys

class aptset():
    def install(package_name,args):
        os.system('apt install '+package_name+' --yes '+args)
    def clean():
        os.system('apt autoremove -y && apt autoclean -y')
    def remove(package_name,args):
        os.system('apt remove '+package_name+' --yes '+args)
    def fix():
        os.system('apt install --fix-missing')


