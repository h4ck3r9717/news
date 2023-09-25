from app import create_app
from flask_script import Manager, Server

#creating app instance
app = create_app('production')

manager = Manager(app)
manager.add_command('server', Server)
def test():
    '''
    Running the unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()