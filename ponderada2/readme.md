<h1>Documentação da entrega da ponderada 2</h1> 

Nesta atividade busquei simular uma etapa inicial do projeto, que é dar posições para turtlebot e fazê-lo se mover naquela direção.

Para isso então, primeiramente importei as bibliotecas necessárias, sendo as principais, a de movimentação,geometry_msgs, contendo a função Twist() e a segunda foi a nav_msgs, contendo a odom, necessário para determinar a posição do robô. Após isso fiz um pequeno input apenas para que o código ficasse um pouco mais inetrativo e para mostrar que o robô pode se movimentar para qualquer ponto.

Quanto a classe, fiz um publisher para a movimentação e um subscriber para verificar a posição do robô. A função principal é chamada de odometria e lá todos os processos acontecem. Como funciona: primeiro ele registra a posição do robô em uma variável e usa a função euler_from_quaternion para tornar a posição um ângulo de euler. Em seguida acho a diferença entre o ângulo de euler atual e da posição que desejo ir, usando a função do arco tagente. Antes de iniciar a movimentação, checo se ele está com o ângulo certo, se não, ele roda até entrar no intervalo desejo. Depois de corrigir o ângulo, ele começa andar, até que ele, novamente, entre no intervalo que corresponde a coordenada desejada. Em alguns momentos, o turtlebot para, mas apenas para corrigir sua direção. Para finalizar ele publica os comandos e printa as coordenadas x,y e o ângulo de euler atual, apenas para acompanhamento.

