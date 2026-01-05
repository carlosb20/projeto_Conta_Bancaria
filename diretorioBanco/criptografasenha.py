import bcrypt

def criptografa(senha: str) -> bytes:
    senha_bytes = senha.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_senha = bcrypt.hashpw(senha_bytes, salt)
    return hash_senha


def verifica_senha(senha: str, hash_senha: bytes) -> bool:
    return bcrypt.checkpw(senha.encode('utf-8'), hash_senha)






