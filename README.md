

# Criação do Ambiente Python
virtualenv -p python3 env
source env/bin/activate

# Instalação das dependências python no virtualenv (standalone)
pip install -r requirements.txt


# Executndo o mapreduce do contador de palavras em todos os livros dentro de tmp/books
### executando o MrJob com o runner local "-r local" dizemos ao MrJob para rodar multithread "localmente", sem hadoop
python mjob_mr_word_counter.py tmp/books/*.txt -r local >> mapreduce_word_count.txt

### executando o MrJob com o runner Hadoop "-r hadoop" dizemos ao MrJob para rodar com hadoop via streaming
python mjob_mr_word_counter.py tmp/books/*.txt -r hadoop >> mapreduce_word_count.txt

### executando o MrJob sem o parâmetro runner "-r" dizemos ao MrJob para rodar em python puro sem multithread
python mjob_mr_word_counter.py tmp/books/*.txt >> mapreduce_word_count.txt

*Nota:* além de local e Hadoop o MrJob suporta os runners EMR Amazon e Dataproc do Google

Terminada a execução, teremos então o resultado no arquivo mapreduce_word_count.txt




# Referências

### Haddop MapReduce in Python
https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/


### "Pythonic" Hadoop

Special attention to Mr. Job

https://www.thomashenson.com/hadoop-python-example/


### Hadoop Sreaming
https://www.tutorialspoint.com/pg/hadoop/hadoop_streaming.htm


### Arg Parse
https://stackoverflow.com/questions/40001892/reading-named-command-arguments

