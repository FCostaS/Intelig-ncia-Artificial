import random
import math

# Função objetivo
def function(x):
    y = 1 + x*(2 - x)
    return y

# Espaço de Busca
SearchSpace = [-3, 3]

# Parâmetros do PSO
N = 5                   # Quantidade de Partículas
iterations = 3          # Número de Iterações
w = 0.7                 # Constante de inercia
c1 = 0.2                # Constante Cognativa
c2 = 0.6                # Constante Social
f_init = -float("inf")  # Valor inicial

class Particle:
    def __init__(self, SearchSpace):
        self.X = []                      # Posição da Partícula
        self.V = []                      # Velocidade da Partícula
        self.pbest = []                  # Melhor Posição da Partícula
        self.fitness_pbest = f_init      # Valor inicial para melhor posição
        self.fitness_X = f_init          # -/-

        # Gerando posição e velocidade aleatórias
        self.X = random.uniform(SearchSpace[0], SearchSpace[1])
        self.V = random.uniform(0, 1)

    # Método para atualizar o melhor valor local
    def evaluate(self,function):
        self.fitness_X = function(self.X)
        if self.fitness_X > self.fitness_pbest:
            self.pbest = self.X                  # Atualizando melhor local
            self.fitness_pbest = self.fitness_X  # Atualizando fitness do melhor local

    # Método para ativar a velocidade da partícula
    def update_velocity(self,gbest):
        r1 = random.uniform(0,1)
        r2 = random.uniform(0,1)
        self.V = w*self.V + c1*r1*(self.pbest - self.X) + c2*r2*(gbest - self.X)

    # Método para atualizar a posição da partícula
    def update_position(self):
        self.X = self.X + self.V

    def printSwarm(self):
        print(str(self.V))

                
def PSO(function,SearchSpace,N,iterations):
    fitness_gbest = -float("inf")
    gbest = []

    # Inicializando partículas
    Swarm = []
    for i in range(N):
        Swarm.append( Particle(SearchSpace) )
    
    for i in range(iterations):

        # Atualiza todas as particulas
        for j in range(N):
            Swarm[j].evaluate(function)

            # Verificando/Salvando o melhor global
            if Swarm[j].fitness_X > fitness_gbest:
                gbest = Swarm[j].X
                fitness_gbest = Swarm[j].fitness_X

            # Atualizando particula
            Swarm[j].update_velocity(gbest)
            Swarm[j].update_position()
        
        Vs = []
        Xs = []
        for j in range(N):
            Vs.append(Swarm[j].V)
            Xs.append(Swarm[j].V)
        print('Vi = ' + str(Vs))
        print('Xi = ' + str(Xs))
        print('')

    print('Solução: f('+ str(gbest) + ') = ' + str(fitness_gbest))

def main(): 
    PSO(function, SearchSpace, N, iterations)

main()