from abc import ABC, abstractmethod

class OrdemServico(ABC):
    def __init__(self, id, equipamento, descricao, prioridade, tempo_estimado):
        self.id = id
        self.equipamento = equipamento
        self.descricao = descricao
        self.tempo_estimado = tempo_estimado
        
        self._status = "Pendente" 
        self.prioridade = prioridade 

    @property
    def prioridade(self):
        return self._prioridade

    @prioridade.setter
    def prioridade(self, valor):
        if 1 <= valor <= 5:
            self._prioridade = valor
        else:
            raise ValueError("A prioridade tem de ser entre 1 e 5.")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, novo_status):
        if novo_status == "Concluída" and self._status != "Em execução":
            raise ValueError("Erro: Não se pode concluir uma ordem que não está em execução.")
        
        if novo_status in ["Pendente", "Em execução", "Concluída"]:
            self._status = novo_status
        else:
            raise ValueError("Status inválido.")

    @abstractmethod
    def calcular_custo(self):
        pass


class ManutencaoPreventiva(OrdemServico):
    def calcular_custo(self):
        return self.tempo_estimado * 2.00


class ManutencaoCorretiva(OrdemServico):
    def calcular_custo(self):
        return (self.tempo_estimado * 3.50) + 150.00


ordem1 = ManutencaoPreventiva(id=1, equipamento="Torno Mecânico", descricao="Lubrificação", prioridade=2, tempo_estimado=60)
ordem2 = ManutencaoCorretiva(id=2, equipamento="Motor Principal", descricao="Substituição de peça", prioridade=5, tempo_estimado=120)

lista_de_ordens = [ordem1, ordem2]

for ordem in lista_de_ordens:
    custo = ordem.calcular_custo()
    print(f"Ordem {ordem.id} ({ordem.equipamento}) - Custo: R$ {custo:.2f}")

# Teste do Desafio Adicional
print("\nTestar o bloqueio de status:")
ordem1.status = "Em execução" 
print(f"Status atualizado para: {ordem1.status}")

try:
    ordem2.status = "Concluída" 
except ValueError as e:
    print(f"Bloqueio funcionou! Mensagem: {e}")