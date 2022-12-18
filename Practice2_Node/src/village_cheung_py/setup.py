from setuptools import setup

package_name = 'village_cheung_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lio',
    maintainer_email='lio@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "cheung = village_cheung_py.cheung:main",
            "cheung_oop = village_cheung_py.cheung_oop:main"
        ],
    },
)
