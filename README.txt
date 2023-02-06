Este código é uma aplicação PyQt5 para exibir uma janela principal com um botão "Calcular tempo de simulação". 
Quando o botão é clicado, a função calculate_simulation_time é chamada e o tempo total de simulação é calculado.

A aplicação cria uma instância de QApplication e QWidget e configura o título da janela para "MyApp". 
Em seguida, é criado um botão "Calculate Simulation Time" com uma largura de 200 pixels e altura de 50 pixels, 
posicionado na posição (50, 50) na janela.

A classe MyApp é definida como uma subclasse de QMainWindow e é usada para mostrar a janela principal. 
O método calculate_simulation_time é definido na classe MyApp e é chamado quando o botão é clicado. 
Este método usa o caminho fornecido pelo usuário para calcular o tempo total de simulação e exibir o 
resultado na consola.
