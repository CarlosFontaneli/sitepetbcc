from django.shortcuts import render, HttpResponseRedirect
import sendgrid
from sendgrid.helpers.mail import *
from django.conf import settings

# Create your views here.

professores = [{'nome': 'Dr. Valter Vieira de Camargo', 'descricao': 'Tutor do PET-BCC e Coordenador do Curso',
                'foto': 'valter_vieira_de_camargo.jpg', 'contato': 'valter@dc.ufscar.br'},
               {'nome': 'Dr. Antonio Carlos dos Santos', 'descricao': 'Professor colaborador',
                'foto': 'antonio_carlos_dos_santos.png', 'contato': 'santos@dc.ufscar.br'},
               {'nome': 'Dr.ª Rosângela Ap. Dellosso Penteado', 'descricao': 'Professora colaboradora',
                'foto': 'rosangela_aparecida_dellosso_penteado.jpg', 'contato': 'rosangela@<br>dc.ufscar.br'}]

bolsistas = [
    {'nome': 'Alexandre da Silva Lara Pinto', 'descricao': 'BCC 014', 'foto': 'alexandre_da_silva_lara_pinto.jpg', 'contato': 'Alexandre-Lara'},
    {'nome': 'Felipe Sampaio de Souza', 'descricao': 'BCC 015', 'foto': 'felipe_sampaio_de_souza.jpg', 'contato': 'SampaioFelipe'},
    {'nome': 'Gabriel Toret Palomino', 'descricao': 'BCC 013', 'foto': 'gabriel_toret_palomino.jpg', 'contato': 'palomito'},
    {'nome': 'José Vitor de Carvalho Aquino', 'descricao': 'BCC 014', 'foto': 'jose_vitor_de_carvalho_aquino.jpg', 'contato': 'jvcaquino'},
    {'nome': 'Leonardo Destro Bronzato', 'descricao': 'BCC 013', 'foto': 'leonardo_desto_bronzato.jpg', 'contato': 'leobronza'},
    {'nome': 'Leticia Yumi Katsurada', 'descricao': 'BCC 015', 'foto': 'leticia_yumi_katsurada.jpg', 'contato': 'YumiKatsurada'},
    {'nome': 'Marcelo de Oliveira da Silva', 'descricao': 'BCC 012', 'foto': 'marcelo_de_oliveira_da_silva.jpg', 'contato': 'marcelodeolive1ra'},
    {'nome': 'Muriel Guilherme Alves Mauch', 'descricao': 'BCC 014', 'foto': 'muriel_guilherme_alves_mauch.jpg', 'contato': 'MurielMauch'},
    {'nome': 'Pedro Henrique Migliati', 'descricao': 'BCC 015', 'foto': 'pedro_henrique_miglitatti.jpg', 'contato': 'p3m1'},
    {'nome': 'Thiago Yonamine', 'descricao': 'BCC 014', 'foto': 'thiago_yonamine.jpg', 'contato': 'ThiagoYonamine'}]

naoBolsistas = []

voluntarios = [{'nome': 'Fernando Messias da Silva', 'descricao': 'BCC 012', 'foto': 'fernando_messias_da_silva.jpg', 'contato': 'fernandoMessias'},
               {'nome': 'Julia de Moura Caetano', 'descricao': 'BCC 015', 'foto': 'julia_de_moura_caetano.jpg', 'contato': 'juliamourac'},
               {'nome': 'Miguel de Souza Tosta', 'descricao': 'BCC 015', 'foto': 'miguel_de_souza_tosta.jpg', 'contato': 'miguelsott'}]

exMembros = [{'nome': 'Alan Cesar Laine', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Ana Dulce Padovan Torres', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'André Vinicius Bertoni Nicoleti', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Bruno Dias Leite', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Bruno F. Rodrigues', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Bruno Guerra D. Pereira', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Bruno Luigi Borgo', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Bruno Santos', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Caroline Castor dos Santos', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Denis Cappelini', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Douglas Antonio Martins Barbino', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Eduardo Kazuo Nakao', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Felipe Castro Dezotti', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Gabriela Vanessa Pereira Alves Mattos', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Guilherme Cuppi Jeronimo', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Guilherme Rigo Reccio', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Hugo Leonardo M. A. de Barros', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'José Antônio dos Santos Junior', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Júlio Maçumoto', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Leonardo Lopes', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Lucas Antoniale Callegari', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Lucas Bueno', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Lucas Yamanaka', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Marcelo Araujo Pontes', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Mariana Yamamoto', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Matheus dos Santos Freitas', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Nicolas Masonori Shimizu', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Paula Lamin Honda', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Rafael Eduardo Wolf Goes', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Renan Peixoto da Silva', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Tiago Bassani', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Tiago Bonadio Badoco', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Thiago Arraiol Casaes', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Thiago Neves Romero', 'descricao': '', 'foto': 'user.png'}]


def manutencao(request):
    return render(request, 'site2016/manutencao.html', {'DEBUG': settings.DEBUG})


def home(request):
    if not settings.MANUTENCAO:
        context_dictionary = {'pagina': 'home', 'DEBUG': settings.DEBUG}
        return render(request, 'site2016/home.html', context_dictionary)
    else:
        return render(request, 'site2016/manutencao.html', {})


def equipe(request):
    context_dictionary = {'pagina': 'equipe',
                          'professores': professores,
                          'bolsistas': bolsistas,
                          'naoBolsistas': naoBolsistas,
                          'voluntarios': voluntarios,
                          'exMembros': exMembros,
                          'DEBUG': settings.DEBUG}

    return render(request, 'site2016/equipe.html', context_dictionary)


def projetos(request):
    context_dictionary = {'pagina': 'projetos', 'DEBUG': settings.DEBUG}
    return render(request, 'site2016/projetos.html', context_dictionary)


def sobre(request):
    context_dictionary = {'pagina': 'sobre', 'DEBUG': settings.DEBUG}
    return render(request, 'site2016/sobre.html', context_dictionary)


def processo_seletivo(request):
    context_dictionary = {'pagina': 'processo_seletivo', 'DEBUG': settings.DEBUG}
    return render(request, 'site2016/processoseletivo.html', context_dictionary)


def contato(request):
    if request.method == 'POST':
        try:
            nome = request.POST['nome']
            email = request.POST['email']
            assunto = request.POST['assunto']
            mensagem = request.POST['mensagem']

            # print(request.POST['nome'])
            # print(request.POST['email'])
            # print(request.POST['assunto'])
            # print(request.POST['mensagem'])

            sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
            from_email = Email(nome+" <"+email+">")
            subject = "CONTATO VIA SITE: "+assunto
            to_email = Email("PET-BCC <petbcc@googlegroups.com>")

            conteudo_email = mensagem

            content = Content("text/html", conteudo_email)
            ready_mail = Mail(from_email,subject,to_email, content)

            response = sg.client.mail.send.post(request_body=ready_mail.get())

            print(response.status_code)

        except:
            pass

        context_dictionary = {'pagina': 'contato', 'DEBUG': settings.DEBUG}
        return render(request, 'site2016/contato.html', context_dictionary)
    else:
        context_dictionary = {'pagina': 'contato', 'DEBUG': settings.DEBUG}
        return render(request, 'site2016/contato.html', context_dictionary)