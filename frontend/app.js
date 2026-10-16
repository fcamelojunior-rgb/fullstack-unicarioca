const API_URL = "http://localhost:8000/projects";

const botaoCarregar = document.getElementById("carregar-projetos");
const listaProjetos = document.getElementById("lista-projetos");
const mensagem = document.getElementById("mensagem");

async function carregarProjetos() {
  mensagem.textContent = "Carregando projetos...";
  listaProjetos.innerHTML = "";

  try {
    const resposta = await fetch(API_URL);

    if (!resposta.ok) {
      throw new Error("Não foi possível consultar a API.");
    }

    const dados = await resposta.json();

    dados.projects.forEach((projeto) => {
      const item = document.createElement("li");

      const nome = document.createElement("h3");
      nome.textContent = projeto.name;

      const categoria = document.createElement("p");
      categoria.textContent = `Categoria: ${projeto.category}`;

      const status = document.createElement("p");
      status.textContent = `Situação: ${projeto.status}`;

      item.append(nome, categoria, status);
      listaProjetos.appendChild(item);
    });

    mensagem.textContent = `${dados.projects.length} projeto(s) carregado(s).`;
  } catch (erro) {
    mensagem.textContent = "Erro ao carregar projetos. Verifique se a API está ativa.";
    console.error(erro);
  }
}

botaoCarregar.addEventListener("click", carregarProjetos);