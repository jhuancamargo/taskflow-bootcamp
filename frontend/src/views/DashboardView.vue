<template>
  <div class="h-full">
    <div class="mb-8 flex justify-between items-start">
  <div class="flex-1">
    <h1 class="text-3xl font-extrabold text-slate-900 tracking-tight">Visão Geral do Projeto</h1>
    <p class="text-slate-500 mt-1">Acompanhe o fluxo de trabalho da sua equipe em tempo real.</p>
  </div>

      <div class="flex items-center gap-3 relative filtro-container">
        <button
          @click="mostrarFiltros = !mostrarFiltros"
          class="h-[42px] flex items-center gap-2 bg-slate-200 hover:bg-slate-300 text-slate-700 px-4 rounded-lg text-sm font-medium"
        >
          Filtros
        </button>

        <div class="h-[42px] flex items-center gap-2 bg-white border border-slate-200 rounded-lg px-4 shadow-sm">
          <span class="text-sm font-medium text-slate-600">Total</span>
          <span class="bg-slate-200 text-slate-700 px-2 py-0.5 rounded-full text-xs font-semibold">
            {{ tarefas.length }}
          </span>
        </div>

        <router-link
          to="/tarefas"
          class="h-[42px] flex items-center bg-indigo-600 hover:bg-indigo-700 text-white px-4 rounded-lg text-sm font-medium shadow-sm"
        >
          + Nova Tarefa
        </router-link>

        <div
          v-if="mostrarFiltros"
          class="absolute right-0 top-full mt-3 bg-white border border-slate-200 rounded-xl shadow-lg p-4 z-20 w-[520px]"
        >
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div>
              <label class="block text-sm font-semibold text-slate-700 mb-2">Responsável</label>
              <select
                v-model="filtros.responsavel"
                class="w-full border border-slate-300 rounded-lg px-3 py-2 bg-white text-sm"
              >
                <option value="">Todos</option>
                <option v-for="u in usuarios" :key="u.id" :value="u.id">
                  {{ u.nome }}
                </option>
              </select>
            </div>

            <div>
              <label class="block text-sm font-semibold text-slate-700 mb-2">Status</label>
              <select
                v-model="filtros.status"
                class="w-full border border-slate-300 rounded-lg px-3 py-2 bg-white text-sm"
              >
                <option value="">Todos</option>
                <option value="A Fazer">A Fazer</option>
                <option value="Em Andamento">Em Andamento</option>
                <option value="Concluído">Concluído</option>
              </select>
            </div>

            <div>
              <label class="block text-sm font-semibold text-slate-700 mb-2">Prioridade</label>
              <select
                v-model="filtros.prioridade"
                class="w-full border border-slate-300 rounded-lg px-3 py-2 bg-white text-sm"
              >
                <option value="">Todas</option>
                <option value="Baixa">Baixa</option>
                <option value="Média">Média</option>
                <option value="Alta">Alta</option>
              </select>
            </div>
          </div>

          <div class="mt-4 flex justify-end">
            <button
              @click="limparFiltros"
              class="bg-slate-200 hover:bg-slate-300 text-slate-700 px-4 py-2 rounded-lg text-sm font-medium"
            >
              Limpar filtros
            </button>
          </div>
        </div>
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-start">
      <div class="bg-slate-100 rounded-xl p-4 border border-slate-200 shadow-inner">
        <h2 class="font-bold text-slate-700 mb-4 flex justify-between">
          A Fazer <span class="bg-slate-200 text-slate-600 px-2 py-0.5 rounded-full text-xs">{{ tarefasFiltradas('A Fazer').length }}</span>
        </h2>
        <div class="space-y-3">
          <div v-for="tarefa in tarefasFiltradas('A Fazer')" :key="tarefa.id" class="bg-white p-4 rounded-lg shadow-sm border border-slate-200 hover:shadow-md transition-shadow border-l-4 border-l-slate-400 relative">
            <div class="flex flex-wrap gap-2 mb-3">
              <span class="text-xs font-semibold px-2 py-1 rounded-md bg-blue-50 text-blue-700">
                {{ obterNomeResponsavel(tarefa.responsavel_id) }}
              </span>
              <span class="text-xs font-semibold px-2 py-1 rounded-md bg-amber-50 text-amber-700">
                {{ formatarPrazo(tarefa.prazo) }}
              </span>
              <span :class="['text-xs font-semibold px-2 py-1 rounded-md', classePrioridade(tarefa.prioridade)]">
                {{ tarefa.prioridade }}
              </span>
            </div>

            <button
              @click="excluirTarefa(tarefa.id)"
              class="absolute top-2 right-2 w-6 h-6 flex items-center justify-center rounded-full text-slate-400 hover:bg-red-100 hover:text-red-600 transition"
            >
              ×
            </button>

            <h3 class="font-bold text-slate-800">{{ tarefa.titulo }}</h3>
            <p class="text-sm text-slate-500 mt-1">{{ tarefa.descricao }}</p>

            <button
              @click="() => {atualizarStatus(tarefa.id, 'Em Andamento') }"
              class="text-xs font-medium text-indigo-600 hover:text-indigo-800 cursor-pointer px-1 py-1"
            >
              Iniciar →
            </button>
          </div>
        </div>
      </div>

      <div class="bg-indigo-50 rounded-xl p-4 border border-indigo-100 shadow-inner">
        <h2 class="font-bold text-indigo-800 mb-4 flex justify-between">
          Em Andamento <span class="bg-indigo-200 text-indigo-800 px-2 py-0.5 rounded-full text-xs">{{ tarefasFiltradas('Em Andamento').length }}</span>
        </h2>
        <div class="space-y-3">
          <div v-for="tarefa in tarefasFiltradas('Em Andamento')" :key="tarefa.id" class="bg-white p-4 rounded-lg shadow-sm border border-slate-200 hover:shadow-md transition-shadow border-l-4 border-l-indigo-500 relative">
            <div class="flex flex-wrap gap-2 mb-3">
              <span class="text-xs font-semibold px-2 py-1 rounded-md bg-blue-50 text-blue-700">
                {{ obterNomeResponsavel(tarefa.responsavel_id) }}
              </span>
              <span class="text-xs font-semibold px-2 py-1 rounded-md bg-amber-50 text-amber-700">
                {{ formatarPrazo(tarefa.prazo) }}
              </span>
              <span :class="['text-xs font-semibold px-2 py-1 rounded-md', classePrioridade(tarefa.prioridade)]">
                {{ tarefa.prioridade }}
              </span>            
            </div>
            
            <button
              @click="excluirTarefa(tarefa.id)"
              class="absolute top-2 right-2 w-6 h-6 flex items-center justify-center rounded-full text-slate-400 hover:bg-red-100 hover:text-red-600 transition"
            >
              ×
            </button>

            <h3 class="font-bold text-slate-800">{{ tarefa.titulo }}</h3>
            <p class="text-sm text-slate-500 mt-1">{{ tarefa.descricao }}</p>

            <div class="mt-4 flex justify-between">
            <button
              @click="atualizarStatus(tarefa.id, 'A Fazer')"
              class="text-xs font-medium text-slate-600 hover:text-slate-800 cursor-pointer px-1 py-1"
            >
              ← Voltar
            </button>

            <button
              @click="atualizarStatus(tarefa.id, 'Concluído')"
              class="text-xs font-medium text-emerald-600 hover:text-emerald-800 cursor-pointer px-1 py-1"
            >
              Concluir ✓
            </button>
          </div>
          </div>
        </div>
      </div>

      <div class="bg-emerald-50 rounded-xl p-4 border border-emerald-100 shadow-inner">
        <h2 class="font-bold text-emerald-800 mb-4 flex justify-between">
          Concluído <span class="bg-emerald-200 text-emerald-800 px-2 py-0.5 rounded-full text-xs">{{ tarefasFiltradas('Concluído').length }}</span>
        </h2>
        <div v-for="tarefa in tarefasFiltradas('Concluído')" :key="tarefa.id" class="bg-white p-4 rounded-lg shadow-sm border border-slate-200 opacity-75 border-l-4 border-l-emerald-500 relative">
          <div class="flex flex-wrap gap-2 mb-3">
            <span :class="['text-xs font-semibold px-2 py-1 rounded-md', classePrioridade(tarefa.prioridade)]">
              {{ tarefa.prioridade }}
            </span>
            <span class="text-xs font-semibold px-2 py-1 rounded-md bg-blue-50 text-blue-700">
              {{ obterNomeResponsavel(tarefa.responsavel_id) }}
            </span>
            <span class="text-xs font-semibold px-2 py-1 rounded-md bg-amber-50 text-amber-700">
              {{ formatarPrazo(tarefa.prazo) }}
            </span>
          </div>

          <h3 class="font-bold text-slate-800 line-through decoration-slate-400">{{ tarefa.titulo }}</h3>
          <p class="text-sm text-slate-500 mt-1">Tarefa finalizada.</p>

          <div class="mt-4 flex justify-end">
              <div class="mt-2 flex justify-between">
            <button
              @click="excluirTarefa(tarefa.id)"
              class="absolute top-2 right-2 w-6 h-6 flex items-center justify-center rounded-full text-slate-400 hover:bg-red-100 hover:text-red-600 transition"
            >
              ×
            </button>

            <button
              @click="atualizarStatus(tarefa.id, 'Em Andamento')"
              class="text-xs text-indigo-600 hover:text-indigo-800 cursor-pointer"
            >
              Reabrir
            </button>
          </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const tarefas = ref([])
const usuarios = ref([])
const filtros = ref({responsavel: '', status: '', prioridade: ''})
const mostrarFiltros = ref(false)

const carregarTarefas = async () => {
  try {
    const res = await axios.get('http://localhost:8000/tarefas')
    tarefas.value = res.data
  } catch (error) {
    console.error("Erro ao carregar tarefas", error)
  }
}

const carregarUsuarios = async () => {
  try {
    const res = await axios.get('http://localhost:8000/usuarios')
    usuarios.value = res.data
  } catch (error) {
    console.error("Erro ao carregar usuários", error)
  }
}

const tarefasFiltradas = (statusColuna) => {
  return tarefasComFiltro().filter(t => t.status === statusColuna)
}

const quantidadeTarefasConcluidas = () => {
  return tarefas.value.filter(t => t.status === 'Concluído').length
}

const atualizarStatus = async (id, novoStatus) => {
  // A barra aqui é mantida para separar o ID (ex: tarefas/1)
  await axios.put(`http://localhost:8000/tarefas/${id}`, { status: novoStatus })
  carregarTarefas()
}

const obterNomeResponsavel = (responsavelId) => {
  const usuario = usuarios.value.find(u => u.id === responsavelId)
  return usuario ? usuario.nome : `Usuário #${responsavelId}`
}

const formatarPrazo = (prazo) => {
  if (!prazo) return 'Sem prazo'
  const [ano, mes, dia] = prazo.split('-')
  return `${dia}/${mes}/${ano}`
}

const classePrioridade = (prioridade) => {
  switch (prioridade) {
    case 'Alta':
      return 'bg-red-50 text-red-700'
    case 'Média':
      return 'bg-amber-50 text-amber-700'
    case 'Baixa':
      return 'bg-sky-50 text-sky-700'
    default:
      return 'bg-slate-100 text-slate-600'
  }
}

const tarefasComFiltro = () => {
  return tarefas.value.filter(tarefa => {
    const filtroResponsavel =
      !filtros.value.responsavel ||
      String(tarefa.responsavel_id) === String(filtros.value.responsavel)

    const filtroStatus =
      !filtros.value.status ||
      tarefa.status === filtros.value.status

    const filtroPrioridade =
      !filtros.value.prioridade ||
      tarefa.prioridade === filtros.value.prioridade

    return filtroResponsavel && filtroStatus && filtroPrioridade
  })
}

const limparFiltros = () => {
  filtros.value = {
    responsavel: '',
    status: '',
    prioridade: ''
  }
}

const excluirTarefa = async (id) => {
  if (!confirm("Tem certeza que deseja excluir esta tarefa?")) return

  try {
    await axios.delete(`http://localhost:8000/tarefas/${id}`)
    await carregarTarefas()
  } catch (error) {
    console.error("Erro ao excluir tarefa", error)
  }
}

onMounted(async () => {
  await Promise.all([carregarTarefas(), carregarUsuarios()])
})
</script>
