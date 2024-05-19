import unittest
from src.utils.validar_uuid import validar_uuid
from uuid import UUID
class TestUtils(unittest.TestCase):

    def test_validar_uuid(self):
        self.assertIsNone(validar_uuid(None))
        validar_uuid_string = validar_uuid('9142dc08-f6b6-48f6-8c19-2b0bb59a1713')
        self.assertIsInstance(validar_uuid_string, UUID)

        uuid_definido = UUID('9142dc08-f6b6-48f6-8c19-2b0bb59a1713')
        self.validar_uuid_tipo_uuid = validar_uuid(uuid_definido)
        self.assertIsInstance(uuid_definido, UUID)