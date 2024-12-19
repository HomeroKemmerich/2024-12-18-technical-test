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

## Proposta

> **Acessar cada computador, transferir o .exe atualizado e iniciar as rotinas / Gerencias as rotinas agendadas, iniciando-as manualmente em um computador no seu horário**
> 
> O acesso individual de computadores é um processo desnecessário. Os arquivos .exe podem ser salvos no computador de destino e atualizados conforme a atualização dos programas. é possível inclusive, automatizar o processo destas com a criação de um script de atualização que busca a versão mais recente do programa em um repositório interno e substitui as versões anteriores na máquina 
> As rotinas podem ser executadas de forma automatizada de algumas formas:
> - Rotinas de inicialização do sistema podem ser executadas automaticamente na inicialização do computador utilizando scripts .bat
> - Rotinas de natureza temporal (rodam a cada x tempo ou em determinado horário), podem ser executada utilizando o Task Scheduler do Windows

> **Monitorar quando uma rotina que rodam sozinhas terminam para colocar outras / Monitorar rotinas que travam, reiniciando-as ou parando a rotina e liberando o computador para outras**
> 
> Tarefas sequenciais podem ser organizadas utilizando arquivos de script, para que quando uma acabe, outra possa iniciar, sem que o andamento da anterior seja prejudicado. O arquivo pode incluir tratamentos para o caso de falha de uma das tarefas, incluindo uma nova tentativa ou parando sua execução.

> **Rotinas podem dar erro/travar, necessitando monitoramento e ação manual de Theo para reativar ou liberar o computador onde a rotina estava rodando**
> 
> Configurações do sistema operacional armazenam logs de eventos das tarefas realizadas. É possível criar ações baseadas nesses logs, por ecemplo, o disparo de e-mails no caso de uma tarefa que exija lliberação para sua continuidade.
