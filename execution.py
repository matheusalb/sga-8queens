from statistics import mean, stdev
from sga.SGA_8queens import SGA_8queens
import datetime
from utils.utils import increment_path
import sys


def main():
    try:
        n = int(sys.argv[1])
    except:
        n = 30

    execution_convergences = 0
    converged_iteraction = []
    qtd_converged = 0
    bests = []
    for i in range(n):
        print('\n----> execution:', i)

        eight_queens = SGA_8queens(100, 10000, 0.9, 0.4)
        population, final_i, converge, n_converge, best = eight_queens.fit()

        bests.append(best)

        if converge:
            execution_convergences += 1
            converged_iteraction.append(final_i)
            qtd_converged += n_converge

    generation_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
    path_log = "data/individuals_execution_" + generation_time + ".log"
    path_log = increment_path(path_log, mkdir=True)
    individuals = open(path_log, "w+")
    individuals.write(
        'Quantidade execuções o algoritmo convergiu = ' +
        str(execution_convergences / n) + '\n')
    individuals.write(
        'Iteração o algoritmo convergiu:\n\t- media = ' +
        str(mean(converged_iteraction)) + '\n\t- std = ' +
        str(stdev(converged_iteraction)) + '\n')
    individuals.write(
        'Número de indivíduos que convergiram por execução: ' +
        str(qtd_converged) + '\n')
    # individuals.write('Fitness; media = ' + str(mean(converged_iteraction)) + '; std= ' + str(stdev(converged_iteraction))+ '\n')

    # for p in population:
    individuals.write("\n\n" + 'BESTS: \n')
    for b in bests:
        individuals.write(str(b.phenotype) + "---> ")
        individuals.write('fitness: ' + str(b.fitness) + "\n")


if __name__ == '__main__':
    main()
