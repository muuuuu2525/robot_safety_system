from glob import glob
import os
from setuptools import setup

package_name = 'robot_safety_system'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
         glob(os.path.join('launch', '*launch.py*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Taro Chiba',
    maintainer_email='s24c1008ae@s.chibakoudai.jp',
    description='Robot safety system.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensor = robot_safety_system.sensor_simulator:main',
            'brake = robot_safety_system.safety_brake:main',
        ],
    },
)
