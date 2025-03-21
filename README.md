## Introdução

&ensp;Esta atividade tem como objetivo validar o endpoint `getStudentsByInstitution` do `studentController`, que é responsável por filtrar e retornar os alunos de uma instituição específica. Através deste teste, busco assegurar que o sistema retorna os dados corretos e que a integração entre a camada de negócio e o controller está funcionando conforme o esperado.

---

## **Caso de Teste: Validação do Endpoint de Alunos por Instituição**

| **Item**             |  **Descrição**                                                                                                                                                  |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ID do Teste**      | TC01                                                                                                                                                           |
| **Objetivo**         | Garantir que a requisição GET para `/students/{id}` retorne corretamente os alunos pertencentes à instituição informada.                                        |
| **Pré-condição**     | - O servidor deve estar em execução e o endpoint `/students/{id}` deve estar disponível. <br> - Deve existir pelo menos uma instituição com `id` válido e alunos associados. |
| **Procedimento**     | 1. Enviar uma requisição GET para o endpoint, por exemplo: `http://localhost:3000/students/1`.<br> 2. Verificar o código de status da resposta.<br> 3. Validar se o corpo da resposta contém um JSON com uma lista de alunos e se os objetos possuem os campos esperados (ex.: `id`, `nome`, `curso`). |
| **Resultado Esperado** | A API deve retornar o status `200 OK` e, no corpo da resposta, um JSON com uma lista de alunos. Cada objeto de aluno deverá conter, ao menos, os campos `id`, `nome` e `curso`. |
| **Resultado Obtido**  | O teste retornou um JSON com todos os alunos da instituição escolhida.                                                                                                |
| **Pós-condição**     | O teste não deve alterar o estado do sistema, apenas realizar a consulta e a verificação dos dados retornados.                                                    |

---

## Como Executar o Teste?

1. **Preparação do Ambiente:**
   - Certifique-se de que o servidor Node.js esteja rodando corretamente.
   - Garanta que o endpoint `/students/{id}` esteja acessível.
2. **Instalação das Dependências:**
   - No terminal, execute:  
     ```sh
     pip install requests
     ```
3. **Execução do Teste:**
   - Execute o script de teste com o comando:  
     ```sh
     python test_get_students.py
     ```
4. **Verificação dos Resultados:**
   - Observe o terminal para verificar se o teste passou ou falhou, conforme as asserções definidas no código.

---

## **Conclusão do Teste**

&ensp;O teste demonstrou que o endpoint `getStudentsByInstitution` está operando conforme o esperado, retornando os dados corretos para uma instituição específica. A utilização do método `GET` com um `id` válido resultou em uma resposta com status `200 OK` e a lista de alunos no formato adequado. Caso algum dos dados esperados não seja retornado ou a API retorne um código de erro, o teste falhará, permitindo uma rápida identificação e correção do problema.