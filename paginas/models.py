from django.db import models

# todas as classes deve ter herança de models.Model
# Create your models here.
# Para fazer uma herança em py basta colocar o nome da classe entre parenteses




# Cadastrar alunos (nome, CPF, curso)

#Cadastrar cursos (nome, código, duração)

#Listar alunos por curso

#Salvar os dados em um arquivo .json

#Carregar os dados ao iniciar o programa








# Cria sua classes

class HomePage (models.Model):
        title = "Combate ao sedentarismo: o papel da atividade Física na promoção da saúde"
        descricao = "Pretendemos abordar a importância da interrupção do comportamento sedentário,e mostrar os danos que o sedentarismo pode causar em nossas vidas, e com isso mostrar o benefício de praticar atividades fisicas."

class SobreNos(models.Model):
     title = "Sobre Nós"
     descrição = "Somos Natan Garcia e Emanuely de Carvalho Niza, uma dupla comprometida em promover mais saúde e qualidade de vida por meio da informação. Nosso objetivo é conscientizar as pessoas sobre os riscos do sedentarismo e a importância da atividade física no dia a dia. Acreditamos que pequenas mudanças de hábitos podem fazer uma grande diferença no bem-estar físico e mental de todos. Por isso, criamos este espaço para compartilhar conhecimentos, dicas práticas e reflexões que incentivem um estilo de vida mais ativo, equilibrado e saudável. Vamos juntos nessa jornada contra o sedentarismo!"


class OqueESedentarismo(models.Model):
     title = "O que é Sedentarismo?"
     description = "O sedentarismo é a falta de atividade física regular, caracterizado por um estilo de vida com pouca movimentação, como passar longos períodos sentado ou deitado. É comum em rotinas modernas, marcadas pelo uso excessivo de tecnologias e pela falta de tempo ou motivação para se exercitar. Essa condição está associada a diversos problemas de saúde, como obesidade, doenças cardiovasculares, diabetes tipo 2 e transtornos emocionais. Para combatê-lo, é importante adotar hábitos simples, como caminhar mais, usar escadas e praticar atividades físicas regularmente. Manter-se ativo é fundamental para a saúde e qualidade de vida."

    
class ImportanciaDaPraticaDeAtividadesFisicas(models.Model):
     title = "Importancia da Pratica de Atividades Fisicas"
     description = "A atividade física é essencial para a saúde do corpo e da mente. Quando praticada regularmente, ajuda a prevenir doenças como obesidade, diabetes e problemas cardíacos, além de melhorar o humor, reduzir o estresse e aumentar a disposição. Também fortalece músculos e ossos, melhora a autoestima e contribui para um envelhecimento mais saudável. Mesmo pequenas ações, como caminhar ou subir escadas, já fazem diferença. Por isso, incluir o exercício na rotina é um passo importante para uma vida mais equilibrada e com qualidade."
     topicos = "1 - Melhora da saúde física 2 - Bem-estar mental e emocional 3 - Mais disposição e energia 4 - Melhora da autoestima e confiança 5 - Prevenção do envelhecimento precoce"

class ComoCombater(models.Model):
     title = "Como Combater?"
     description = "Combater o sedentarismo exige mudanças simples, mas consistentes no dia a dia. A primeira atitude é incluir mais movimento na rotina, mesmo que de forma gradual. Caminhar até lugares próximos, usar escadas em vez de elevadores e fazer pausas ativas durante o trabalho ou os estudos são formas eficazes de começar. Além disso, é importante reservar um tempo para praticar atividades físicas regulares, como caminhar, pedalar, dançar ou praticar esportes. Escolher uma atividade que traga prazer torna o processo mais fácil e motivador. Manter-se ativo também envolve diminuir o tempo sentado em frente à TV, celular ou computador. Com pequenas atitudes e persistência, é possível sair do sedentarismo e conquistar uma vida mais saudável, com mais energia, bem-estar e qualidade."
