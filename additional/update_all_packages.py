import subprocess
import pkg_resources
import time


'''
Initially installed only - {'setuptools', 'pip'}

python -m pip install --upgrade {package_name}
python -m pip uninstall {package_name}

requests       ['certifi-2019.11.28', 'chardet-3.0.4', 'idna-2.8', 'requests-2.22.0', 'urllib3-1.25.8']
matplotlib     ['cycler-0.10.0', 'kiwisolver-1.1.0', 'matplotlib-3.1.3', 'pyparsing-2.4.6', 'python-dateutil-2.8.1', 'six-1.14.0']
xlwings        ['comtypes-1.1.7', 'pywin32-227', 'xlwings-0.18.0']
beautifulsoup4 ['beautifulsoup4-4.8.2', 'soupsieve-1.9.5']
Django         ['Django-3.0.3', 'asgiref-3.2.3', 'pytz-2019.3', 'sqlparse-0.3.0']
openpyxl       ['et-xmlfile-1.0.1', 'jdcal-1.4.1', 'openpyxl-3.0.3']
'''

begin_time = time.time()
installed_packages = {'pip', 'xlwings', 'urllib3', 'pyTelegramBotAPI', 'Django', 'PyPDF2', 'Brotli', 
                      'requests', 'numpy', 'setuptools', 'beautifulsoup4', 'matplotlib', 'openpyxl', 
                      'rarfile', 'certifi', 'altgraph', 'chardet'}

iterator = 1
for package_name in installed_packages:  # Install/upgrade packages from list
    print(f"-----> № = {iterator} | {package_name} <-----\n")
    subprocess.call(f"python -m pip install --upgrade {package_name} --user", shell=True)
    iterator += 1
    
'''
for package_obj in pkg_resources.working_set:  # Upgrade all installed packages
    package_name = " ".join(str(package_obj).split()[:-1])
    installed_packages.add(package_name)
    print(f"-----> № = {iterator} | {package_name} <-----\n")
    subprocess.call(f"python -m pip install --upgrade {package_name} --user", shell=True)
    iterator += 1
'''

print("<----->")
end_time = time.time()
print("Whole time = {:.2f} s.".format(end_time - begin_time))
print(f"installed_packages = {installed_packages}")
print("<----->")
