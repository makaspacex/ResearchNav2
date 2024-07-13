from setuptools import find_packages, setup
import glob

package_name = 'car_urdf'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/' + package_name + '/description',glob.glob(f"description/*")),
        ('share/' + package_name + '/launch', glob.glob('launch/*')),
        ('share/' + package_name + '/rviz', glob.glob('rviz/*')),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='makafly',
    maintainer_email='izhangxm@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
