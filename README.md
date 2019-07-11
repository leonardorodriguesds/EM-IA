# Estudos em IA
## Detecção de anomalias em grafos
Muito sem tem discutido nos últimos anos no ramo da Ciência da computação sobre detecção de anomalias. Esta que é uma importante tarefa, com grande peso em segurança, finanças e mesmo em saúde. A partir de padrões normativos e desvios, apesar de pequenas mas importantes, é possível detectar fraudes, invasores, entre outros. Inúmeras técnicas foram desenvolvidas nos últimos anos para detecção de outliers e anomalias em coleções de pontos não estruturados em planos multidimensionais. Entretanto, a relação entre os pontos, em seu determinado contexto, é tão importante quanto o desvio de seu determinado padrão normativo. E portanto, a utilização de grafos, que conseguem representar essas relações além de seus desvios, com grande facilidade, elevou o trabalho para detecção, bem como explora um novo espectro de análises importantes para este processo. Logo, a detecção de anomalias em dados estruturados como grafos ganhou um importante foco nos últimos anos.

## EM IA - UnB 2019/01
Na disciplina de Estudos em Inteligência Artificial da Universidade de Brasília, UnB, do primeiro semestre de 2019, estudamos motivações e técnicas para detecção de anomalias em dados representados como grafos. O primeiro artigo estudado, [Graph based anomaly detection and description: a survey](https://arxiv.org/abs/1404.4679), aborda os principais pontos sobre a motivações para detecção de anomalias em grafos. Nele o autor realça também as vantagens, e o amplo espectro de representação de correlações entre dados em grafos. Além disso, também são apresentados conceitos, bem como ideias para implementação de algoritmos de detecção. O artigo visa dá uma visão geral sobre o assunto, bem como discutir ideias. E por fim, o artigo é concluído com exemplos de aplicações destas técnicas, bem como também apresenta desafios para essa linha de pesquisa.
Nosso segundo artigo estudado foi [Anomaly detection in data represented as graphs](http://ailab.eecs.wsu.edu/subdue/papers/EberleIDA07.pdf). O artigo artigo apresenta 3 principais algoritmos para detecção de anomalias. Todos os 3 são baseados em buscas em largura, breadth-first search, e heurísticas de descrição de comprimento mínimo, Minimum Description Length (MDL). Além disso, o autor também introduz uma nova divisão de anomalias, nas quais são baseadas em qual tipo de desvio do padrão normativo ela apresenta. São elas: inserção, modificações e exclusões. E portanto, cada um dos algoritmos apresentadas é focada em um tipo de anomalias. Dentre eles, o principal estudado nesta disciplina é GBAD-MDL.

###### GBAD-MDL:
O primeiro algoritmo é nominado de GBAD-MDL, o qual nos propusemos a desenvolver nesta disciplina, e este é para anomalias de modificações, onde estruturas anomalas são baseadas em alterações de labels em suas arestas/nós, ou alterações de relações dentro do contexto dos dados. O algoritmo utiliza técnicas para descoberta de um padrão normativo, o qual melhor comprime o grafo, e esta estrutura é denominada como padrão normativo. Após isto, o grafo é comprimido utilizando este padrão normativo, e então estruturas que diferem desse padrão normativo são iteradas e por fim recebem uma pontuação, que seria sua classificação de anomalia. A heurística de classificação de anomalia é baseada no custo de modificações necessárias para transformar tal estrutura no padrão normativo. Por fim, baseado em um valor limitante, as estruturas que possuem uma classificação anómala acima desse limite são listadas como anomalias.
![GBAD-MDL para detecção de modificações](https://raw.githubusercontent.com/leonardorodriguesds/EM-IA/master/docs/images/GBAD-MDL.png)

## Dados para o projeto
Os dados utilizados para este projeto estão disponíveis em [Brazil's House of Deputies Reimbursements](https://www.kaggle.com/renatobmlr/brazilian-deputies-individual-analysis?scriptVersionId=6869320). Estes dados são um aglomerado de registros de gatos dos deputados brasileiros de 2013 até 2017. Para este projeto somente o arquivo **deputies_dataset.csv** é necessário. Dentre os dados contidos nele, os principais utilizados neste projeto são:
- bugged_date
- receipt_date
- deputy_id
- political_party
- state_code
- deputy_name
- receipt_social_security_number
- receipt_description
- establishment_name
- receipt_value

## O projeto
Este projeto busca implementar o algoritmo GBAD-MDL, utilizando dados dos gastos dos deputados brasileiros.

###### Dependências
- certifi==2019.3.9
- chardet==3.0.4
- cycler==0.10.0
- dataclasses==0.6
- decorator==4.4.0
- idna==2.8
- kiwisolver==1.1.0
- matplotlib==3.1.0
- networkx==2.3
- numpy==1.16.3
- pandas==0.24.2
- pyparsing==2.4.0
- python-dateutil==2.8.0
- pytz==2019.1
- requests==2.22.0
- six==1.12.0
- urllib3==1.25.3

###### Resultados
Neste primeiro momento, o projeto constroí um grafo para cada deputado. E anexa a ele cada recibo encontrado na tabela de dados. E por fim, é possível ainda visualizar este grafo gerado através da ferramenta **networkx**.
![Grafo de um deputado](https://raw.githubusercontent.com/leonardorodriguesds/EM-IA/master/docs/images/Figure_1.png)