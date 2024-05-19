from uuid import UUID
import re


def validar_uuid(uuid: str | UUID | None) -> UUID | None:
    if not uuid:
        return None

    if isinstance(uuid, UUID):
        return uuid

    if not isinstance(uuid, str):
        raise AttributeError('O formato do uuid é inválido')

    uuid_formatado = uuid.replace('-', '').lower()

    if re.match('[^a-z0-9]', uuid_formatado):
        raise AttributeError('O UUID informado é inválido.')

    if len(uuid_formatado) != 32:
        raise AttributeError('O UUID informado é inválido.')
    return UUID(uuid_formatado)
