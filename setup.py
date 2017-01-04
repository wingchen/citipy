from setuptools import setup, find_packages

setup(
    name='citipy',
    version='0.0.5',
    packages=find_packages(),

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
