<template>
  <div class="h-full">
    <div class="mb-8 flex justify-between items-start">
      <div class="flex-1">
        <h1 class="text-3xl font-extrabold text-slate-900 tracking-tight">Visão Geral do Projeto</h1>
        <p class="text-slate-500 mt-1">Acompanhe o fluxo de trabalho da sua equipe em tempo real.</p>
      </div>

    
      <div class="flex items-center gap-4">
        <div class="flex items-center gap-2 bg-white border border-slate-200 rounded-lg px-4 py-2.5 shadow-sm">
          <span class="text-sm font-medium text-slate-600">Total de Tarefas</span>
          
          <span class="bg-slate-200 text-slate-700 px-2 py-0.5 rounded-full text-xs font-semibold">
            {{ tarefas.length }}
          </span>
        </div>

        <router-link
          to="/tarefas"
          class="bg-indigo-600 hover:bg-indigo-700 text-white px-5 py-2.5 rounded-lg font-medium shadow-sm transition-all"
        >
          + Nova Tarefa
        </router-link>
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-start">
      <div class="bg-slate-100 rounded-xl p-4 border border-slate-200 shadow-inner">
        <h2 class="font-bold text-slate-700 mb-4 flex justify-between">
          A Fazer <span class="bg-slate-200 text-slate-600 px-2 py-0.5 rounded-full text-xs">{{ tarefasFiltradas('A Fazer').length }}</span>
        </h2>
        <div class="space-y-3">
          <div v-for="tarefa in tarefasFiltradas('A Fazer')" :key="tarefa.id" class="bg-white p-4 rounded-lg shadow-sm border border-slate-200 hover:shadow-md transition-shadow border-l-4 border-l-slate-400">
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
          <div v-for="tarefa in tarefasFiltradas('Em Andamento')" :key="tarefa.id" class="bg-white p-4 rounded-lg shadow-sm border border-slate-200 hover:shadow-md transition-shadow border-l-4 border-l-indigo-500">
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
        <div v-for="tarefa in tarefasFiltradas('Concluído')" :key="tarefa.id" class="bg-white p-4 rounded-lg shadow-sm border border-slate-200 opacity-75 border-l-4 border-l-emerald-500">
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
            <button
              @click="atualizarStatus(tarefa.id, 'Em Andamento')"
              class="text-xs font-medium text-indigo-600 hover:text-indigo-800 cursor-pointer px-1 py-1"
            >
              Reabrir
            </button>
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

const tarefasFiltradas = (status) => {
  return tarefas.value.filter(t => t.status === status)
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
onMounted(async () => {
  await Promise.all([carregarTarefas(), carregarUsuarios()])
})
</script>
