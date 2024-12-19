# Desafio 1 - Construção de soluções

Analise a situação abaixo e proponha melhorias ou mudanças de estrutura. 
Não é para desenvolver ou "codar" a proposta/melhoria.

---

## Situação

Theo tem diversos processos de rotinas automatizados (RPA) que seguem algumas
regras:
- Cada rotina é um RPA_1.exe, RPA_2.exe, RPA_N.exe;
- Cada rotina deve ser rodado em um PC, um Notebook, maquina virtualizada, etc;
- Cada rotina tem duração variada, alguns duram 5 min, outros o dia todo;
- Existem rotinas que podem ser iniciadas e rodadas ao mesmo tempo em uma máquina sem criar problemas e processos que devem ser obrigatoriamente rodados sozinho na máquina para não dar problema;
- Cada rotina pode ser iniciada quando alguém solicita ao Theo ou de forma agendada, devem ser rodadas uma vez por dia/semana/mês em X horários;

Pedro atualmente faz este trabalho de organização/orquestração de forma manual,
algumas atividades dele incluem:
- Acessar cada computador, transferir o .exe atualizado e iniciar as rotinas;
- Gerencias as rotinas agendadas, iniciando-as manualmente em um computador no seu horário
- Monitorar quando uma rotina que rodam sozinhas terminam para colocar outras;
- Monitorar rotinas que travam, reiniciando-as ou parando a rotina e liberando o computador para outras;
- Rotinas podem dar erro/travar, necessitando monitoramento e ação manual de Theo para reativar ou liberar o computador onde a rotina estava rodando.

Com base nestas informações, sugira uma estrutura e melhorias onde os recursos humanos e de estrutura sejam mais bem utilizados.
Podem ser feitos desenhos explicando as estruturas e tecnologias envolvidas que sustentariam a sua solução/melhoria.
