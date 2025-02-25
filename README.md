# 🚀 Gerador de Leads Falsos para CRM

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Repositório com script Python para gerar dados fictícios de leads realistas para testes em CRMs. Desenvolvido com foco em informações do contexto brasileiro.

## 📋 Sumário

- [Funcionalidades](#-funcionalidades)
- [Requisitos](#-requisitos)
- [Como Usar](#-como-usar)
- [Estrutura dos Dados](#-estrutura-dos-dados)
- [Contribuição](#-contribuição)

## 🎯 Funcionalidades

- **Geração de Excel Dinâmico**

  - Cria arquivos `.xlsx` com número de linhas personalizável
  - Nome de arquivo único com timestamp para evitar sobrescritas

- **Dados Gerados** 📊
  - `Nome completo` com gênero aleatório
  - `E-mail` corporativo/Personalizado
  - `Telefone` com DDD válido
  - `Produto` com nome composto (2 palavras)
  - `Produto SKU` no formato adequado
  - `CPF/CNPJ` válidos e formatados
  - `Cidade` baseada na tabela
  - `Endereço completo` (Bairro, Estado, País, CEP)
  - `Origem do Cliente` com palavra aleatória
  - `Site do Cliente` URL
  - `Empresa` Nomes falsos de empresas

## 📦 Requisitos

- Python 3.7+
- Dependências:
  ```bash
  pip install openpyxl faker
  ```

## 🛠 Como Usar

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/fake-data-generator.git
   ```

2. Acesse o diretório:

   ```bash
   cd fake-data-generator
   ```

3. Execute o script:

   ```bash
   python create_tables.py
   ```

4. Insira o número de leads desejado quando solicitado:

   ```python
   [+] Quantas linhas de dados falsos você deseja gerar? 1000
   ```

5. O arquivo será gerado no formato:
   ```bash
   fake_data_en_1000_lines.xlsx
   ```

## 🗂 Estrutura dos Dados

| Coluna            | Tipo de Dado | Exemplo                              |
| ----------------- | ------------ | ------------------------------------ |
| Name              | String       | Maria Oliveira                       |
| Email             | String       | maria.oliveira@email.com             |
| Phone Number      | String       | (11) 98765-4321                      |
| Product Name      | String       | Software Empresarial                 |
| Product SKU       | String       | SKU-8161-VT                          |
| CPF/CNPJ          | String       | 123.456.789-09 ou 12.345.678/0001-90 |
| Cidade            | String       | Botucatu                             |
| Bairro            | String       | Moema                                |
| Estado            | String       | São Paulo                            |
| País              | String       | Brasil                               |
| CEP               | String       | 04094-050                            |
| Origem do Cliente | String       | Facebook Ads                         |
| Site do Cliente   | String       | https://www.exemplo.com              |
| Empresa           | String       | Exemplo Corp                         |

## 🤝 Contribuição

Contribuições são bem-vindas! Siga esses passos:

1. Faça um Fork do projeto
2. Crie sua Branch:
   ```bash
   git checkout -b feature/nova-feature
   ```
3. Commit suas mudanças:
   ```bash
   git commit -m 'Adiciona nova funcionalidade'
   ```
4. Push para a Branch:
   ```bash
   git push origin feature/nova-feature
   ```
5. Abra um Pull Request

**Nota:** Para relatar problemas ou sugerir melhorias, [abra uma issue](https://github.com/PatrickEN-dev/fake-lead-excel-generator/issues).

---

⌨️ com ❤️ por [Patrick] - ✉️ [patrickendev25@gmail.com]
