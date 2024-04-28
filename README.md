DTI_test
======================

Primeiramente, acho válido destacar a escolha da linguagem de backend e o framekwork usado para desenvolver o teste. A linguagem escolhida foi o Python, tanto por razões de familiaridade com a ferramenta quanto pela facilidade de conceber a lógica e biblioteca disponíveis para facilitar a resolução do problema, como a biblioteca de datas por exemplo(para converter datas d/m/y em dias da semana). 

Dito isso, é relecante ser dito a razão por trás da escolha do framework Flask ao invés de Django. Bom como, essencialmente, o projeto a ser implementado era pequeno, o prazo era curto e não havia uma estrutura complexa de banco de dados ou sequer a necessidade de um. O Flask seria uma escoha mais acertada, tendo em vista sua flexibilidade e rápida prototipagem.

Em segundo lugar, na implementação do backend, tentando diminuir o problema de dependências optei por usar Docker. Logo, o projeto, em tese, funcionará em qualquer OS e em qualquer máquina desde que possua Docker instalado. Para colocar o projeto no ar basta rodar o comando:

```
sudo docker compose up --build
```

Ainda acerca do backend, não havia necessida, já que como eram poucos dados eles poderiam ser representados como constantes, mas mesmo assim, decidi usar bancos de dados, pois facilitaria escalabilidade da aplicação

Agora, quanto ao frontend, para facilitar e acelerar o desenvolvimento foi usada usada uma biblioteca de Forms do React para criar o formulário e verifcar os dados antes de serem enviados para a API do backend.

Além disso, diferentement do backend, o frontend foi requisitado que fosse feito em React, então assumi que em relação ao stack de JavaScript não haveria problemas de dependências. Para satisfazer as dependências do frontend basta rodar o comando:

```
npm i
```

Por último, sobre as suposições feitas, assumi que não haveriam gastos de deslocamento, posto que a pessoa poderia andar até o canil. Além disso, como não ha informações sobre o meio tranposrte que seria usado, estimar um valor total levando em conta o transporte seria uma aproximação.