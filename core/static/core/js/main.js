// Filtros simples das listas de Provas e de Atletas.
// Rodam no navegador: escondem ou mostram os itens que já estão na página.

// Deixa o texto em minúsculas e sem acento, para a busca achar "joao" em "João".
function normalizar(texto) {
    return texto.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
}

document.addEventListener('DOMContentLoaded', function () {
    filtrarProvas();
    filtrarAtletas();
    filtrarEquipes();
});

// ----- Lista de provas: chips de modalidade + busca pelo nome -----
function filtrarProvas() {
    var cards = document.querySelectorAll('.grade .card');
    var chips = document.querySelectorAll('.chips .chip');
    var busca = document.getElementById('busca-prova');
    if (cards.length === 0 || !busca) {
        return; // não é a página de provas
    }

    var modalidade = ''; // '' = todas

    function aplicar() {
        var texto = normalizar(busca.value);
        cards.forEach(function (card) {
            var okModalidade = modalidade === '' || card.dataset.modalidade === modalidade;
            var okNome = normalizar(card.dataset.nome).includes(texto);
            card.style.display = okModalidade && okNome ? '' : 'none';
        });
    }

    chips.forEach(function (chip) {
        chip.addEventListener('click', function () {
            chips.forEach(function (c) { c.classList.remove('ativo'); });
            chip.classList.add('ativo');
            modalidade = chip.dataset.modalidade;
            aplicar();
        });
    });
    busca.addEventListener('input', aplicar);
}

// ----- Lista de equipes: busca pelo nome ou sigla + modalidade -----
function filtrarEquipes() {
    var linhas = document.querySelectorAll('tbody tr[data-sigla]');
    var busca = document.getElementById('busca-equipe');
    var selModalidade = document.getElementById('filtro-modalidade-equipe');
    if (linhas.length === 0 || !busca) {
        return; // não é a página de equipes
    }

    function aplicar() {
        var texto = normalizar(busca.value);
        linhas.forEach(function (linha) {
            var okTexto = normalizar(linha.dataset.nome).includes(texto) || normalizar(linha.dataset.sigla).includes(texto);
            var okModalidade = selModalidade.value === '' || linha.dataset.modalidade === selModalidade.value;
            linha.style.display = okTexto && okModalidade ? '' : 'none';
        });
    }

    busca.addEventListener('input', aplicar);
    selModalidade.addEventListener('change', aplicar);
}

// ----- Lista de atletas: busca pelo nome + modalidade + equipe -----
function filtrarAtletas() {
    var linhas = document.querySelectorAll('tbody tr[data-nome]');
    var busca = document.getElementById('busca-atleta');
    var selModalidade = document.getElementById('filtro-modalidade');
    var selEquipe = document.getElementById('filtro-equipe');
    if (linhas.length === 0 || !busca) {
        return; // não é a página de atletas
    }

    function aplicar() {
        var texto = normalizar(busca.value);
        linhas.forEach(function (linha) {
            var okNome = normalizar(linha.dataset.nome).includes(texto);
            var okModalidade = selModalidade.value === '' || linha.dataset.modalidade === selModalidade.value;
            var okEquipe = selEquipe.value === '' || linha.dataset.equipe === selEquipe.value;
            linha.style.display = okNome && okModalidade && okEquipe ? '' : 'none';
        });
    }

    busca.addEventListener('input', aplicar);
    selModalidade.addEventListener('change', aplicar);
    selEquipe.addEventListener('change', aplicar);
}
