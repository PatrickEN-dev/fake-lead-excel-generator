from openpyxl import Workbook  # type: ignore
from faker import Faker  # type: ignore
import os
import random


language = (
    input(
        "Selecione o idioma (pt_br para Português, en_us para Inglês, es para Espanhol): "
    )
    .strip()
    .lower()
)
if language not in ["pt_br", "en_us", "es"]:
    print("Idioma inválido. Usando en_us como padrão.")
    language = "en_us"

# Inicializar instâncias Faker
fake_geral = Faker(language)
fake_brasil = Faker("pt_BR")
if language == "es":
    fake_es = Faker("es_ES")


def gerar_nome_arquivo(num_linhas, nome_base="dados_falsos", extensao="xlsx"):
    """
    Gera um nome de arquivo que inclui o idioma e evita sobrescritas.
    Exemplo: dados_falsos_es_100_linhas_1.xlsx
    """
    contador = 1
    while True:
        nome_arquivo = (
            f"{nome_base}_{language}_{num_linhas}_linhas_{contador}.{extensao}"
        )
        if not os.path.exists(nome_arquivo):
            return nome_arquivo
        contador += 1


def gerar_numero_celular_brasil():
    """
    Gera um número de celular brasileiro no formato:
    DDD (2 dígitos) + '9' + 8 dígitos, sem formatação.
    Exemplo: 14991336409
    """
    ddd = str(random.randint(11, 99))
    numero = "9" + "".join(str(random.randint(0, 9)) for _ in range(8))
    return ddd + numero


def gerar_numero_celular_eua():
    """
    Gera um número de celular dos EUA com 10 dígitos, garantindo
    que o primeiro dígito do código de área e do prefixo não sejam 0 ou 1.
    Exemplo: 4155552671
    """
    area_code = str(random.randint(2, 9)) + "".join(
        str(random.randint(0, 9)) for _ in range(2)
    )
    prefix = str(random.randint(2, 9)) + "".join(
        str(random.randint(0, 9)) for _ in range(2)
    )
    line_number = "".join(str(random.randint(0, 9)) for _ in range(4))
    return area_code + prefix + line_number


def gerar_numero_celular_espanhol():
    """
    Gera um número de celular espanhol com 9 dígitos,
    iniciando com 6 ou 7.
    Exemplo: 612345678
    """
    primeiro = random.choice(["6", "7"])
    restante = "".join(str(random.randint(0, 9)) for _ in range(8))
    return primeiro + restante


def gerar_nif_espanhol():
    """
    Gera um NIF espanhol (DNI) no formato 8 dígitos seguidos de uma letra.
    A letra é calculada a partir do número usando o algoritmo tradicional.
    """
    numero = random.randint(10000000, 99999999)
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    letra = letras[numero % 23]
    return f"{numero}{letra}"


def criar_excel(num_linhas):
    nome_arquivo = gerar_nome_arquivo(num_linhas)

    wb = Workbook()
    ws = wb.active
    ws.title = "Dados Falsos"

    if language == "pt_br":
        cabecalhos = [
            "Nome",
            "E-mail",
            "Telefone",
            "Nome do Produto",
            "SKU",
            "CPF/CNPJ",
            "Bairro",
            "Estado",
            "País",
            "CEP",
            "Origem do Cliente",
            "Site do Cliente",
            "Empresa",
        ]
    elif language == "en_us":
        cabecalhos = [
            "Name",
            "Email",
            "Phone Number",
            "Product Name",
            "SKU",
            "CPF/CNPJ",
            "Neighborhood",
            "State",
            "Country",
            "Postcode",
            "Customer Origin",
            "Customer Website",
            "Company",
        ]
    elif language == "es":
        cabecalhos = [
            "Nombre",
            "Correo electrónico",
            "Número de Móvil",
            "Nombre del Producto",
            "SKU",
            "NIF",
            "Barrio",
            "Estado",
            "País",
            "Código Postal",
            "Origen del Cliente",
            "Sitio Web del Cliente",
            "Empresa",
        ]

    ws.append(cabecalhos)

    for _ in range(num_linhas):
        if language == "pt_br":
            nome = fake_geral.name()
            email = fake_geral.email()
            telefone = gerar_numero_celular_brasil()
            nome_produto = (
                f"{fake_geral.word().capitalize()} {fake_geral.word().capitalize()}"
            )
            sku_produto = fake_geral.bothify(text="SKU-####-??").upper()
            cpf_cnpj = (
                fake_brasil.cpf() if random.random() < 0.5 else fake_brasil.cnpj()
            )
            bairro = fake_brasil.bairro()
            estado = fake_brasil.estado_sigla()
            pais = fake_brasil.country()
            cep = fake_brasil.postcode()
            origem_cliente = fake_geral.word()
            site_cliente = fake_geral.url()
            empresa = fake_geral.company()

            linha = [
                nome,
                email,
                telefone,
                nome_produto,
                sku_produto,
                cpf_cnpj,
                bairro,
                estado,
                pais,
                cep,
                origem_cliente,
                site_cliente,
                empresa,
            ]

        elif language == "en_us":
            nome = fake_geral.name()
            email = fake_geral.email()
            telefone = gerar_numero_celular_eua()
            nome_produto = (
                f"{fake_geral.word().capitalize()} {fake_geral.word().capitalize()}"
            )
            sku_produto = fake_geral.bothify(text="SKU-####-??").upper()
            cpf_cnpj = (
                fake_brasil.cpf() if random.random() < 0.5 else fake_brasil.cnpj()
            )
            # Usar neighborhood se disponível, caso contrário city()
            bairro = (
                fake_geral.neighborhood()
                if hasattr(fake_geral, "neighborhood")
                else fake_geral.city()
            )
            estado = fake_geral.state_abbr()
            pais = fake_brasil.country()
            if "Brasil" in pais:
                pais = pais.replace("Brasil", "Brazil")
            cep = fake_geral.postcode()
            origem_cliente = fake_geral.word()
            site_cliente = fake_geral.url()
            empresa = fake_geral.company()

            linha = [
                nome,
                email,
                telefone,
                nome_produto,
                sku_produto,
                cpf_cnpj,
                bairro,
                estado,
                pais,
                cep,
                origem_cliente,
                site_cliente,
                empresa,
            ]

        elif language == "es":
            nome = fake_es.name()
            email = fake_es.email()
            telefone = gerar_numero_celular_espanhol()
            nome_produto = (
                f"{fake_es.word().capitalize()} {fake_es.word().capitalize()}"
            )
            sku_produto = fake_es.bothify(text="SKU-####-??").upper()
            nif = gerar_nif_espanhol()
            # Para "barrio" usamos o nome de uma rua como exemplo
            bairro = fake_es.street_name()
            # Seleciona aleatoriamente uma comunidade/autonomía espanhola
            estados_es = [
                "Andalucía",
                "Aragón",
                "Asturias",
                "Baleares",
                "Canarias",
                "Cantabria",
                "Castilla y León",
                "Castilla-La Mancha",
                "Cataluña",
                "Extremadura",
                "Galicia",
                "La Rioja",
                "Madrid",
                "Murcia",
                "Navarra",
                "País Vasco",
                "Valencia",
            ]
            estado = random.choice(estados_es)
            pais = "España"
            cep = fake_es.postcode()
            origem_cliente = fake_es.word()
            site_cliente = fake_es.url()
            empresa = fake_es.company()

            linha = [
                nome,
                email,
                telefone,
                nome_produto,
                sku_produto,
                nif,
                bairro,
                estado,
                pais,
                cep,
                origem_cliente,
                site_cliente,
                empresa,
            ]

        ws.append(linha)

    wb.save(nome_arquivo)
    print(f"Arquivo Excel '{nome_arquivo}' criado com {num_linhas} linhas.")


if __name__ == "__main__":
    try:
        num_linhas = int(input("Digite o número de linhas a serem geradas: "))
    except ValueError:
        print("Por favor, insira um número válido.")
    else:
        criar_excel(num_linhas)
