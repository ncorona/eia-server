# README #

Applicazione web che consente di effetutare l'emotion detection su un testo
fornito dall'utente, sviluppata durante la EIA summer school.


### What is this repository for? ###

L'applicazione web è composta da:

* una GUI con la quale l'utente inserisce la frase che vuole classificare e visualizza il risultato su un grafico a istogramma

* un server che espone le API REST invocate dalla GUI - invocando un servizio esterno per classificare il testo - e invia il risultato tramite messaggi OSC.


Il backend è stato sviluppato in Python e utilizza il servizio esterno Paralleldots (https://www.paralleldots.com/#) per effettuare la classificazione del testo fornito dall'utente.
Per l'utilizzo delle API fornite da Paralleldots è necessario disporre della api key.



### How do I get set up? ###

#### Configuration ####

Prima di avviare il server web è necessario impostare le seguenti variabili d'ambiente:

* __API_KEY__ access token per utilizzare il servizio remoto di classificazione

* __OSC_CLIENTS__ lista degli endpoint ai quali inviare i risultati dell'analisi


Le variabili d'ambiente possono essere impostate sulla macchina con il seguente comando:

```bash
export API_KEY=12345678
export OSC_CLIENTS=127.0.0.1:8000,192.168.1.2:5555
```

#### Dependencies ####

L'applicazione è stata sviluppata in Python.
Per poter creare correttamente il server è sufficiente installare le dipendenze riportate all'interno del file _requirements.txt_.
I moduli Python possono essere installati con il seguente comando:

```bash
pip install -r src/requirements.txt
```


#### Docker deployment ####

L'applicazione può essere eseguita anche all'interno di un container Docker utilizzando l'apposita immagine (che deve essere prima costruita e poi avviata):

```bash
docker build . -t ncorona/eia-server:latest

docker run -d --rm \
           -e API_KEY=12345678 \
           -e OSC_CLIENTS=192.168.1.2:5555 \
           -p 8080:8080 \
           ncorona/eia-server:latest
```

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines


### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact
