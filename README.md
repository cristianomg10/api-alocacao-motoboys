# API para alocação de entregas para motoboys

## Introdução
Esta API foi desenvolvida para efeitos didáticos.
Não há mecanismos de otimização de rotas. Apenas alocação de entregas em locais próximos para entregadores disponíveis.

## Documentação
~~O domínio será gerando quando o Flask_Ngrok for executado.~~

~~A URL para acesso ao Web service é: http://webalunos.cacador.ifsc.edu.br:5000~~
A URL será fornecida no dia da utilização.

### Rota /otimiza/<n_entregadores>
#### Requisição
A rota a ser chamada é **/otimiza/<n_entregadores>**, utilizando o método **POST**.

**n_entregadores** se refere ao número de entregadores. Se não for passado, será utilizado por padrão o valor **2**

É esperado no corpo da requisição uma *string* formatada em JSON, como a seguir:

```json
[
   {
      "cep":"89504790",
      "rua":"manoel pedro driessen",
      "bairro":"municipios"
   },
   {
      "cep":"89504690",
      "rua":"fahdo tome",
      "bairro":"champagnat"
   },
   {
      "cep":"89504548",
      "rua":"argentina",
      "bairro":"reunidas"
   },
   {
      "cep":"89504539",
      "rua":"peru",
      "bairro":"reunidas"
   },
   {
      "cep":"89504711",
      "rua":"sao bento do sul",
      "bairro":"municipios"
   },
   {
      "cep":"89504536",
      "rua":"venezuela",
      "bairro":"reunidas"
   },
   {
      "cep":"89503366",
      "rua":"holanda",
      "bairro":"sorgatto"
   }
]
```

Desta string JSON, será utilizado para cálculo de proximidade apenas o **cep**.

#### Resposta

Como resposta, será retornado uma string JSON como a seguinte. No exemplo abaixo, temos os mesmos campos passados na requisição com mais uma chave chamada de "Motoboy", com o ID (numeração) respectivo ao Motoboy. 

```json
[
    {
        "cep": "89504790",
        "rua": "manoel pedro driessen",
        "bairro": "municipios",
        "motoboy": 0
    },
    {
        "cep": "89504790",
        "rua": "manoel pedro driessen",
        "bairro": "municipios",
        "motoboy": 0
    },
    {
        "cep": "89504690",
        "rua": "fahdo tome",
        "bairro": "champagnat",
        "motoboy": 0
    },
    {
        "cep": "89504548",
        "rua": "argentina",
        "bairro": "reunidas",
        "motoboy": 2
    },
    {
        "cep": "89504539",
        "rua": "peru",
        "bairro": "reunidas",
        "motoboy": 2
    },
    {
        "cep": "89504711",
        "rua": "sao bento do sul",
        "bairro": "municipios",
        "motoboy": 0
    },
    {
        "cep": "89504536",
        "rua": "venezuela",
        "bairro": "reunidas",
        "motoboy": 2
    },
    {
        "cep": "89503366",
        "rua": "holanda",
        "bairro": "sorgatto",
        "motoboy": 1
    }
]
```
