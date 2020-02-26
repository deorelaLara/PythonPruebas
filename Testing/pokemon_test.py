import unittest
from pokemon import getPokemon, Pokedex, Pokemon

class BiblioMock(Pokedex):
    def setPokemon(self, name):
        self.pokemon = Pokemon(name, 123, 'Fly')

        def Search(self, id):
            return self.pokemon

class TestRequest(unittest.TestCase):
    def test_pok(self):
        tests = (
            {'input': "12", 'expect_out': "butterfree", 'mock_json': {"name": "butterfree"}},
        )

        for tc in tests:
            biblio_mock = BiblioMock()
            biblio_mock.setPockemon(tc['expect_out'])

            actual = getPockemon(tc['input'], biblio_mock)
            self.assertEqual(tc['expect_out'], actual)


if __name__ == "__main__":
    unittest.main()