/*  Programação para Automação de Testes
Hands-on
Validador de idade mínima para adoção

Crie um script que verifique se um dog pode ser adotado com base na idade mínima definida, por exemplo, 2 anos.
Use os operadores adequados e exiba:

Nome do dog
Idade

Se está apto ou não para adoção
Extra: aplique uma regra com operador lógico para permitir que se o cão for de pequeno porte, 
pode ser adotado independente da idade.

idade 1 + porte P = sim pelo porte
idade 1 + porte M = Não 
idade 1 + porte G = Não 
idade 2 + porte P = sim pela idade
idade 2 + porte M = sim pela idade
idade 2 + porte G = sim pela idade

 */

//1°  - Exemplo  
/*
const idadeMinima = 2
    const nomeDog = "Ted"
    const idadeDog = 1
    const pequenoPorte = false

    const podeAdotar = idadeDog >= idadeMinima || pequenoPorte;

    console.log("=== VALIDAÇÃO PARA ADOÇÃO ===");
    console.log("Nome do dog: " + nomeDog);
    console.log("Idade: " + idadeDog + " anos");
    console.log("Apto para adoção? " + (podeAdotar ? "Sim" : "Não"));
    console.log("==============================");

    */
 
// ------------------------------------------------------------------------------//
// 2°  - Exemplo

const nome = 'Ada'
const idade = 0
const porte = 'P'

const idadeMinima = 2 

const adocao = idade >= idadeMinima 
                ? 'sim'
                : porte === 'P' 
                ? 'sim'
                : 'não'

const adocaov2 = idade >= idadeMinima || porte === 'P'

console.log(adocao)
console.log(adocaov2)

function verificarSePodeSerAdotado(idade, porte) {
  const adocao = idade >= idadeMinima 
                ? 'sim'
                : porte === 'P' 
                ? 'sim'
                : 'não'

  // return adocao
  console.log(adocao)
}

// idade 1 + porte M = nao
// idade 2 + porte M = sim, pela idade
// idade 2 + porte P = sim, pela idade
// idade 1 + porte P = sim, pelo porte

verificarSePodeSerAdotado(1, 'M')
verificarSePodeSerAdotado(2, 'M')
verificarSePodeSerAdotado(2, 'P')
verificarSePodeSerAdotado(1, 'P')


