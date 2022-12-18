from setuptools import setup

package_name = 'village_chen'

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
            "chen_node = village_chen.chen_termial:main",
            "chen_pub_node = village_chen.chen_pub:main",
            "wang_sub_node = village_chen.wang_sub:main"
        ],
    },
)
