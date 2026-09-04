# Gerenciador de Séries Favoritas

## Sobre o projeto

Este projeto é um programa desenvolvido como trabalho na disciplina de Raciocínio Computacional utilizando a linguagem **Python** para gerenciar uma lista de séries favoritas. A aplicação funciona por meio de um **menu interativo no terminal**, permitindo ao usuário cadastrar, consultar, alterar, remover e pesquisar séries.

O projeto foi desenvolvido com base no conceito de **CRUD**, utilizando arquivos **JSON** para armazenar os dados e funções específicas para organizar cada uma das operações.

## Principais características

- Sistema baseado em **CRUD**;
- Persistência dos dados simples em arquivos **JSON**;
- Funções separadas para cada ação do programa;
- Funções documentadas utilizando docstrings;
- Interface simples pelo terminal;
- Validação de algumas entradas fornecidas pelo usuário;
- Controle de séries concluídas e em andamento;
- Pesquisa de séries por parte do nome;
- Prevenção de cadastro duplicado;
- Registro de histórico das alterações realizadas nas séries;
- Exibição de estatísticas da lista.

## Operações CRUD

O sistema implementa as quatro operações principais de um CRUD.

### Create — Adicionar séries

A opção `ADD` permite cadastrar uma ou mais séries.

Durante o cadastro, o programa solicita:

- Nome da série;
- Quantidade de capítulos;
- Situação da série, indicando se foi concluída ou não;
- Serviço utilizado para assistir à série.

Cada série é armazenada como um conjunto de informações, incluindo também um campo para o histórico de alterações.

O programa verifica se a quantidade de capítulos informada é um número inteiro positivo e também verifica se uma série com o mesmo nome já existe, evitando que ela seja cadastrada novamente.

### Read — Listar séries

A opção `LIST` permite visualizar todas as séries favoritas cadastradas.

Para cada série são exibidos o nome, a quantidade de capítulos, o status de conclusão, o serviço utilizado e, quando existente, o histórico de alterações.

### Update — Atualizar séries

A opção `UPDATE` permite alterar informações de uma série existente.

O usuário pode modificar:

- Nome;
- Quantidade de capítulos;
- Status de conclusão;
- Serviço utilizado.

Antes da alteração, os valores anteriores são armazenados e uma nova entrada é adicionada ao histórico da série, contendo a data e os valores antigo e novo.

### Delete — Remover séries

A opção `DELETE` permite remover uma série da lista de favoritas.

O programa procura a série pelo nome e, quando encontrada, remove seu registro da lista principal e salva novamente os dados nos arquivos JSON.

## Persistência dos dados

Os dados são armazenados em arquivos no formato **JSON**, permitindo que as informações continuem disponíveis mesmo depois que o programa é encerrado.

O sistema utiliza três arquivos:

- `series_favoritas.json` — armazena todas as séries favoritas;
- `series_concluidas.json` — armazena as séries marcadas como concluídas;
- `series_andamento.json` — armazena as séries que ainda estão em andamento.

A função `salvar_series()` é responsável por gravar essas informações nos arquivos, enquanto `recuperar_series()` realiza a leitura dos arquivos. Caso um arquivo não exista ou contenha um JSON inválido, o programa retorna uma lista vazia.

## Pesquisa de séries

Além das operações CRUD, o programa possui a opção `SEARCH`.

Essa função permite informar um termo e procurar séries cujo nome contenha esse termo. A pesquisa não diferencia letras maiúsculas e minúsculas, facilitando a localização de uma série.

## Estatísticas

A opção `STATS` apresenta uma visão geral das séries cadastradas.

O programa mostra:

- A lista de séries concluídas;
- A quantidade de séries concluídas;
- A lista de séries em andamento;
- A quantidade de séries em andamento;
- A quantidade total de séries favoritas.

Essa funcionalidade utiliza os arquivos JSON correspondentes para apresentar essas informações.

## Histórico de alterações

Uma característica adicional do projeto é o **registro do histórico de atualizações**.

Quando uma série é modificada, o programa registra a data da alteração, os valores anteriores e os novos valores. Dessa forma, ao listar a série, também é possível visualizar as alterações realizadas anteriormente.


## Organização do código

O projeto é organizado em diferentes funções, cada uma responsável por uma tarefa específica. Entre elas estão:

- `salvar_series()` — salva os dados nos arquivos JSON;
- `recuperar_series()` — recupera os dados armazenados;
- `pesquisa_serie()` — procura uma série pelo nome;
- `adicionar_serie()` — realiza o cadastro;
- `listar_series()` — exibe as séries;
- `atualizar_serie()` — altera os dados;
- `deletar_serie()` — remove uma série;
- `estatisticas()` — apresenta as estatísticas;
- `pesquisar_termo()` — realiza pesquisas por nome;
- `verificador_serie_concluida()` — valida o status da série.

As funções possuem **docstrings** explicando seu objetivo e quando necessário, os parâmetros e valores retornados.

## Tecnologias e recursos utilizados

O projeto utiliza recursos da biblioteca padrão do Python, principalmente:

- `json` para leitura e gravação dos arquivos JSON;
- `datetime` para registrar a data das alterações;
- `re` para realizar a pesquisa por termos no nome das séries.



## Diário de Bordo de I.A
Consiste em outro arquivo explicando quais foram as **pincipais dificuldades** no desenvolvimento do projeto sua estrutura é:

* Primeira linha: Data em que a dúvida surgiu.
* Segunda linha: Qual foi a dúvida.
* Terceira linha: Prompt enviado a I.A para resolver.
* Quarta linha: Qual foi a resposta que obtive da I.A ao enviar o prompt.
* Quinta linha: O que eu aprendi com a resposta.

## Conclusão

O Gerenciador de Séries Favoritas é uma aplicação simples de terminal que reúne conceitos importantes de programação, como **CRUD, funções, estruturas de dados, validação de entradas, manipulação de arquivos e persistência de dados em JSON**.

Além do cadastro básico, o sistema possui recursos adicionais, como **pesquisa, estatísticas, separação entre séries concluídas e em andamento e histórico de alterações**, tornando o projeto mais completo para o objetivo proposto.

**Partes do texto tiveram intervenção de I.A para proporcionar um melhor entendimento.**




