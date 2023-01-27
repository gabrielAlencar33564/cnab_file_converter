# Conversor de arquivo CNAB
Esse projeto, como o próprio nome já diz, tem como objetivo organizar os dados de um arquivo CNAB, armazena-los em um banco de dados e os retorna-los em formato de "card" numa list.

Para seu desenvolvimento, foi utilizado a linguagem `Python` com seu poderoso framework `Django`.

### Primeiramente...
1 - Copie a chave SSH clicando no botão "Code" logo acima.
2 - Após ter feito a copia da chave SSH, abra seu terminal e digite o comando: `git clone` (ainda não aperte enter), mais o clone da "chave SSH".

### Ao clonar o projeto...
3 - Abra o terminal dentro do projeto e execute o seguinte comando: `python -m venv .venv`. Isso fará com que seja criado um ambiente virtual para o projeto.
4 - Após o ambiente virtual ter sido criado, ele ainda não esta ativado, portanto, usaremos o seguinte comando no terminal para ativa-lo: `source .venv/bin/activate`. "OBS: no `Windows`o comando é um pouco diferente, sendo ele: `.venv/Scripts/activate`".
5 - Com o ambiente virtual ativado iremos instalar todas as dependências do projeto com o seguinte comando: `pip install -r requirements.txt`.

### Depois de ter instalado as dependẽncias...
6 - Deverá ser criado um arquivo `.env` na raiz do projeto. Nele será colocado todas as variáveis do seu aquivo vizinho `.env.example`.
7 - Após ter feito a copia das variávei do arquivo `.env.example`, preencha os valores nela (sem dar espaço) após a igualdade.

### Com o arquivo `.env` criado...
8 - Você deverá rodar as migrações do projeto com os seguintes comandos: `python manage.py makemigrations` e `python manage.py migrate`.
9 - Após rodar todas as migrações, rode o projeto no repósitorio local com o seguinte comando: `python manage.py runserver`.
