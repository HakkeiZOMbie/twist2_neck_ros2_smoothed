from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'twist2_neck_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        ('share/' + package_name, 
            ['package.xml', 'config.json', 'camera_config.yaml']
        ),
        ( 
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py'),
        )
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Tomico-DEV',
    maintainer_email='humansbadrobotsgood@gmail.com',
    description='Package for TWIST2 Neck XR teleoperation. Contains drivers and launchfile.',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'neck_node = twist2_neck_ros2.neck_node:main'
        ],
    },
)
