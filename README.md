DTI_test
======================

Primeiramente, é válido destacar a escolha da linguagem de backend e do framework utilizados para desenvolver o teste. Optei pelo Python, tanto pela familiaridade com a ferramenta quanto pela facilidade de conceber a lógica, além da disponibilidade de bibliotecas para facilitar a resolução do problema, como a biblioteca de datas para converter datas de d/m/a em dias da semana.

Quanto à escolha do framework Flask em vez do Django, isso se deu pelo tamanho reduzido do projeto, o prazo curto e a ausência de uma estrutura complexa de banco de dados. O Flask foi uma escolha mais acertada devido à sua flexibilidade e capacidade de prototipagem rápida.

Para diminuir problemas de dependências, optei por utilizar Docker na implementação do backend. Assim, o projeto funcionará em qualquer sistema operacional e em qualquer máquina desde que o Docker esteja instalado. Para colocar o projeto no ar, basta executar o comando:

```
sudo docker compose up --build
```

Embora houvesse a opção de representar os poucos dados como constantes, decidi utilizar bancos de dados para facilitar a escalabilidade da aplicação no futuro.

No que diz respeito ao frontend, para agilizar o desenvolvimento, foi utilizada uma biblioteca de Forms do React para criar o formulário e verificar os dados antes de serem enviados para a API do backend.

Diferentemente do backend, onde a escolha foi livre, o frontend foi requisitado em React. Assim, não previ problemas significativos com dependências em relação ao stack de JavaScript. Para satisfazer as dependências do frontend, basta executar o comando:

```
npm i
```

Após isso:
```
npm start
```

Por fim, sobre as suposições feitas, assumi que não haveria gastos com deslocamento, uma vez que a pessoa poderia caminhar até o canil. Além disso, como não há informações sobre o meio de transporte a ser utilizado, estimar um valor total levando em conta o transporte seria uma aproximação.

Considero que esse projeto proporcionou uma boa oportunidade para aplicar conhecimentos na prática e desenvolver uma aplicação completa, apesar de sua relativa simplicidade.