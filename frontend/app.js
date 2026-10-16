
const API_URL = "http://localhost:8000";

const formulario = document.getElementById("demand-form");
const campoId = document.getElementById("demand-id");
const campoTitulo = document.getElementById("title");
const campoCategoria = document.getElementById("category");
const campoDescricao = document.getElementById("description");
const campoStatus = document.getElementById("status");
const campoResponsavel = document.getElementById("owner");
const campoData = document.getElementById("created_at");

const botaoEnviar = document.getElementById("submit-demand-btn");
const botaoCancelar = document.getElementById("cancel-edit-btn");
const botaoAtualizar = document.getElementById("load-demands-btn");

const caixaStatus = document.getElementById("status-box");
const caixaResumo = document.getElementById("summary-box");
const listaDemandas = document.getElementById("demand-list");

function criarElemento(tag, texto, classe = "") {
  const elemento = document.createElement(tag);
  elemento.textContent = texto;

  if (classe) {
    elemento.className = classe;
  }

  return elemento;
}

function formatarStatus(status) {
  if (status === "em andamento") return "Em andamento";
  if (status === "concluída") return "Concluída";
  return "Pendente";
}

function classeStatus(status) {
  if (status === "em andamento") return "etiqueta-andamento";
  if (status === "concluída") return "etiqueta-concluida";
  return "etiqueta-pendente";
}

async function requisicao(url, opcoes = {}) {
  const resposta = await fetch(url, opcoes);

  if (!resposta.ok) {
    let mensagem = `Erro na requisição (HTTP ${resposta.status}).`;

    try {
      const dadosErro = await resposta.json();
      if (dadosErro.detail) {
        mensagem = dadosErro.detail;
      }
    } catch {
      // Mantém a mensagem HTTP padrão.
    }

    throw new Error(mensagem);
  }

  return resposta.json();
}

function renderizarResumo(resumo) {
  caixaResumo.replaceChildren();

  const indicadores = [
    ["Total de demandas", resumo.total],
    ["Pendentes", resumo.pending],
    ["Em andamento", resumo.in_progress],
    ["Concluídas", resumo.done],
  ];

  indicadores.forEach(([rotulo, valor]) => {
    const cartao = document.createElement("article");
    cartao.className = "cartao-resumo";

    cartao.append(
      criarElemento("p", rotulo, "rotulo"),
      criarElemento("p", String(valor), "valor")
    );

    caixaResumo.appendChild(cartao);
  });
}

function criarCartaoDemanda(demanda) {
  const cartao = document.createElement("article");
  cartao.className = "cartao-demanda";

  const titulo = criarElemento("h3", demanda.title);
  const categoria = criarElemento("p", `Categoria: ${demanda.category}`);
  const descricao = criarElemento("p", `Descrição: ${demanda.description}`);
  const responsavel = criarElemento("p", `Responsável: ${demanda.owner}`);
  const data = criarElemento("p", `Criada em: ${demanda.created_at}`);

  const status = criarElemento(
    "span",
    formatarStatus(demanda.status),
    `etiqueta-status ${classeStatus(demanda.status)}`
  );

  const linhaStatus = document.createElement("p");
  linhaStatus.appendChild(status);

  const acoes = document.createElement("div");
  acoes.className = "acoes-demanda";

  const botaoEditar = criarElemento("button", "Editar");
  botaoEditar.type = "button";
  botaoEditar.className = "botao-secundario";
  botaoEditar.addEventListener("click", () => iniciarEdicao(demanda));

  const botaoExcluir = criarElemento("button", "Excluir", "botao-excluir");
  botaoExcluir.type = "button";
  botaoExcluir.addEventListener("click", () => excluirDemanda(demanda));

  acoes.append(botaoEditar, botaoExcluir);
  cartao.append(titulo, categoria, descricao, responsavel, data, linhaStatus, acoes);

  return cartao;
}

async function carregarDemandas() {
  caixaStatus.textContent = "Carregando demandas...";
  botaoAtualizar.disabled = true;

  try {
    const dados = await requisicao(`${API_URL}/demands`);

    listaDemandas.replaceChildren();

    dados.demands.forEach((demanda) => {
      listaDemandas.appendChild(criarCartaoDemanda(demanda));
    });

    caixaStatus.textContent =
      `${dados.demands.length} demanda(s) encontrada(s).`;
  } catch (erro) {
    caixaStatus.textContent = `Não foi possível carregar as demandas: ${erro.message}`;
  } finally {
    botaoAtualizar.disabled = false;
  }
}

async function carregarResumo() {
  try {
    const resumo = await requisicao(`${API_URL}/summary`);
    renderizarResumo(resumo);
  } catch (erro) {
    caixaResumo.replaceChildren(
      criarElemento("p", `Erro ao carregar o resumo: ${erro.message}`)
    );
  }
}

async function atualizarPainel() {
  await Promise.all([carregarDemandas(), carregarResumo()]);
}

function iniciarEdicao(demanda) {
  campoId.value = demanda.id;
  campoTitulo.value = demanda.title;
  campoCategoria.value = demanda.category;
  campoDescricao.value = demanda.description;
  campoStatus.value = demanda.status;
  campoResponsavel.value = demanda.owner;
  campoData.value = demanda.created_at;

  botaoEnviar.textContent = "Salvar alterações";
  botaoCancelar.hidden = false;
  caixaStatus.textContent = `Editando a demanda ${demanda.id}.`;

  formulario.scrollIntoView({ behavior: "smooth", block: "start" });
  campoTitulo.focus();
}

function limparFormulario() {
  formulario.reset();
  campoId.value = "";
  botaoEnviar.textContent = "Cadastrar demanda";
  botaoCancelar.hidden = true;
}

botaoCancelar.addEventListener("click", () => {
  limparFormulario();
  caixaStatus.textContent = "Edição cancelada.";
});

formulario.addEventListener("submit", async (evento) => {
  evento.preventDefault();

  const demanda = {
    title: campoTitulo.value.trim(),
    category: campoCategoria.value.trim(),
    description: campoDescricao.value.trim(),
    status: campoStatus.value,
    owner: campoResponsavel.value.trim(),
    created_at: campoData.value,
  };

  if (
    !demanda.title ||
    !demanda.category ||
    !demanda.description ||
    !demanda.owner ||
    !demanda.created_at
  ) {
    caixaStatus.textContent = "Preencha todos os campos obrigatórios.";
    return;
  }

  const id = campoId.value;
  const editando = Boolean(id);
  const url = editando
    ? `${API_URL}/demands/${id}`
    : `${API_URL}/demands`;

  const metodo = editando ? "PUT" : "POST";
  botaoEnviar.disabled = true;

  try {
    const resultado = await requisicao(url, {
      method: metodo,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(demanda),
    });

    limparFormulario();
    caixaStatus.textContent = resultado.message;
    await atualizarPainel();
    caixaStatus.textContent = resultado.message;
  } catch (erro) {
    caixaStatus.textContent = `Não foi possível salvar: ${erro.message}`;
  } finally {
    botaoEnviar.disabled = false;
  }
});

async function excluirDemanda(demanda) {
  const confirmou = window.confirm(
    `Deseja excluir a demanda "${demanda.title}"?`
  );

  if (!confirmou) return;

  try {
    const resultado = await requisicao(`${API_URL}/demands/${demanda.id}`, {
      method: "DELETE",
    });

    if (campoId.value === String(demanda.id)) {
      limparFormulario();
    }

    await atualizarPainel();
    caixaStatus.textContent = resultado.message;
  } catch (erro) {
    caixaStatus.textContent = `Não foi possível excluir: ${erro.message}`;
  }
}

botaoAtualizar.addEventListener("click", atualizarPainel);

atualizarPainel();
