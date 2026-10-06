class Aluno:
    def __init__(self, nome, curso):    
        self.nome = nome
        self.curso = curso
        
    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"Curso: {self.curso}")

aluno = Aluno(
    nome="Luiz",
    curso="Inteligência Artificial"
)

aluno.apresentar()