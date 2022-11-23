# 🔨 INSTALAÇÃO DA APLICAÇÃO PARA DESENVOLVIMENTO

1. Realize a clonagem do repositório
```
git clone https://github.com/othiagosilva/myTrainer.git
```

2. Logo após, basta digitar o seguinte comando no terminal, para colocar o servidor no ar:
```
python manage.py runserver
```

Pronto, a aplicação estará rodando no endereço localhost:8000; basta acessá-lo para visualizá-la.

# CRIAÇÃO DE URL
Para criar URLs que redirecionam para as páginas necessárias, será necessário adicioná-la no arquivo 'urls.py' da pasta 'treinador'. <br><br>
![image](https://user-images.githubusercontent.com/66854577/203455499-b0475eaa-11ad-4035-86da-61344ddf2296.png)

Após entrar no arquivo, seguir o padrão que é observado. <br><br>
![image](https://user-images.githubusercontent.com/66854577/203455648-e7f9e926-8745-4e52-94fa-d16337063fb6.png)

Feito isso, será necessário ir no arquivo 'views.py', também dentro do diretório 'treinador' e criar a função que retorna a view.

Com todos os passos completos, tudo estará funcionando, basta adicionar o botão de navegação, no arquivo necessário, conforme exemplo: <br><br>
![image](https://user-images.githubusercontent.com/66854577/203455870-7ced3b23-8ebe-4bc6-b3e0-492192777efd.png)
