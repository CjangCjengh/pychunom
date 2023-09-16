from distutils.core import setup


setup(
    name = 'pychunom',
    packages = ['pychunom'],
    version = '0.1',
    license='MIT',
    description = 'Convert Quoc Ngu to Chu Nom',
    author = 'CjangCjengh',
    author_email = '126621566zz@gmail.com',
    url = 'https://github.com/CjangCjengh/pychunom/',
    download_url = 'https://github.com/CjangCjengh/pychunom/archive/master.zip',
    keywords = ['Vietnamese', 'Chunom'],
    install_requires=['opencc'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    package_data={
        'pychunom': [
            'dict/chunom.json', 'dict/chunom.ocd2'
        ]
    },
)
