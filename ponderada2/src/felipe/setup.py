from setuptools import setup

package_name = 'felipe'

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
    maintainer='felipe-campos',
    maintainer_email='felipe-campos@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robo-gazebo = felipe.robo_gazebo: main',
            'draw-circle = felipe.draw_circle: main',
            'pose-subscriber = felipe.pose_subscriber: main',
            'turtle-controller = felipe.turtle_controller: main',
            'roda-gazebo = felipe.gazebo: main'
        ],
    },
)
