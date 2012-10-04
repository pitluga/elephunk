import unittest
from elephunk.database import DatabaseClients

class DatabaseClientsTest(unittest.TestCase):

    def test_client_returns_requested_database_connection(self):
        def asserting_client_factory(config):
            self.assertEquals(config['host'], 'localhost')
            self.assertEquals(config['port'], 5432)
            self.assertEquals(config['user'], 'user')
            self.assertEquals(config['password'], 'password')
            self.assertEquals(config['database'], 'postgres')

        config = {'localhost': 'psql://user:password@localhost:5432'}
        database_clients = DatabaseClients(config, asserting_client_factory)
        database_clients.client('localhost', 'postgres')

    def test_client_allows_minimal_config(self):
        def asserting_client_factory(config):
            self.assertFalse('user' in config)
            self.assertFalse('password' in config)
            self.assertFalse('port' in config)

        database_clients = DatabaseClients({'localhost': 'psql://localhost'}, asserting_client_factory)
        database_clients.client('localhost', 'postgres')

    def test_client_returns_the_same_for_each_call(self):
        database_clients = DatabaseClients({'localhost': 'psql://user:password@localhost:5432'})
        first = database_clients.client('localhost', 'postgres')
        self.assertIs(first, database_clients.client('localhost', 'postgres'))

    def test_server_names_returns_all_the_names_sorted(self):
        database_clients = DatabaseClients({'somehost': 'psql://somehost', 'localhost': 'psql://localhost'})
        self.assertEquals(['localhost', 'somehost'], database_clients.server_names())
