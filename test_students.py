import requests

def test_get_students_by_institution():
    institution_id = 1
    url = f"http://localhost:3000/students/{institution_id}"
    
    response = requests.get(url)
    
    assert response.status_code == 200, (
        f"Status code obtido {response.status_code}"
    )
    
    students = response.json()
    assert isinstance(students, list), "A resposta deveria ser uma lista de alunos"
    
    for student in students:
        assert isinstance(student, dict), "Cada aluno deveria ser um objeto do tipo dict"
        assert "id" in student, "Campo 'id' não encontrado no objeto aluno"
        assert "nome" in student, "Campo 'nome' não encontrado no objeto aluno"
    
    print("Teste executado com sucesso: os alunos foram retornados conforme esperado.")

if __name__ == "__main__":
    test_get_students_by_institution()
