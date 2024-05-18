from uuid import UUID
def validar_uuid(uuid: str | UUID) -> str | None:
    if not uuid or not str:
        return None

    if  isinstance(uuid, UUID):
        uuid = uuid.__str__()

    uuid_formatado = uuid.replace('-', '').lower()

    if re.match('[^a-z0-9]', uuid_formatado):
        raise AttributeError('O UUID informado é inválido')

    if len(uuid_formatado) != 32:
        raise AttributeError('O UUID informado é inválido')
    return uuid_formatado