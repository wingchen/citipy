from setuptools import setup, find_packages

setup(
    name='citipy',
    version='0.0.1',
    packages=find_packages(),
    scripts=['citipy.py'],

    install_requires=['kdtree>=0.12'],

    package_data={
        '': ['*.csv']
    },

    author='Winston Chen',
    author_email='darwing.chen@gmail.com',
    description='Look for nearest city with geo coordinates.',
    license='MIT',
    keywords=['world cities', 'cities', 'city'],
    url='https://github.com/wingchen/citipy',
)