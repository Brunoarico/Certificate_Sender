# Configuração do ambiente (Linux Ubuntu):

## Primeiro instalar o pdflatex:
sudo apt-get install pdflatex

## E suas respectiva extensão:
sudo apt-get install texlive-fonts-recommended

## Liberar o acesso de apps menos seguros a sua conta do google:
https://myaccount.google.com/security#activity

# Funcionamento do programa:
Existem três diretórios importantes:
 - listname: onde se coloca um arquivo com extensão ".csv" com três colunas contendo, respectivamente, nome, RG e email de quem ira receber os certificados.
 - template: onde se encontra o arquivo latex template que origina os certificados
 - imagens: onde se encontram as imagens de header e footer usadas no certificado.

# Para o caso de modificação do template original:

O arquivo latex template deve usar variáveis especiais para os locais onde o Nome e o RG da pessoa devem ser inseridos.
No local onde se deseja inserir o nome da pessoa deve-se usar a variável $VarName e para o local onde será inserido o RG
usa-se a variável $VarRG.
Para editar o conteúdo do arquivo template observar nele as tags de edição.

# Arquivo names.csv:
Nele é onde constam os dados para os quais o emails serão mandados.

# Execução do programa

Na execução do programa ele solicitará para o usuário o nome de um diretorio o qual ele usara para criar os arquivos tex e pdf,
na sequência solicitará que o usuario insira o email que sera usado para o envio dos emails com o certificado e então sua senha de login no serviço de email.
Por momento o programa aceita apenas contas de email gmail.
Uma vez feito isso os certificados serão enviados para os destinatários.
