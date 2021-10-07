try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config={
    'description': 'ex47',
    'author': 'My Name',
    'url':'URL to get it at',
    'download_url': 'Where to download it',
    'author_email':'My Email',
    'version':'0.1',
    'install_requires':['nose'],
    'package':['ex47'],
    'scripts':[],
    'name':'projectname'
}  

setup(**config)