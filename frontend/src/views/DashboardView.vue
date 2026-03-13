<template>
  <div class="h-full">
    <div class="mb-8 flex justify-between items-center">
      <div>
        <h1 class="text-3xl font-extrabold text-slate-900 tracking-tight">Visão Geral do Projeto</h1>
        <p class="text-slate-500 mt-1">Acompanhe o fluxo de trabalho da sua equipe em tempo real.</p>
      </div>
      <router-link to="/tarefas" class="bg-indigo-600 hover:bg-indigo-700 text-white px-5 py-2.5 rounded-lg font-medium shadow-sm transition-all">
        + Nova Tarefa
      </router-link>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-start">
      <div class="bg-slate-100 rounded-xl p-4 border border-slate-200 shadow-inner">
        <h2 class="font-bold text-slate-700 mb-4 flex justify-between">
          A Fazer <span class="bg-slate-200 text-slate-600 px-2 py-0.5 rounded-full text-xs">{{ tarefasFiltradas('A Fazer').length }}</span>
        </h2>
        <div class="space-y-3">
          <div v-for="tarefa in tarefasFiltradas('A Fazer')" :key="tarefa.id" class="bg-white p-4 rounded-lg shadow-sm border border-slate-200 hover:shadow-md transition-shadow border-l-4 border-l-slate-400">
            <span class="text-xs font-semibold px-2 py-1 rounded-md bg-slate-100 text-slate-600 mb-2 inline-block">{{ tarefa.prioridade }}</span>
            <h3 class="font-bold text-slate-800">{{ tarefa.titulo }}</h3>
            <p class="text-sm text-slate-500 mt-1">{{ tarefa.descricao }}</p>
            <div class="mt-4 flex justify-end">
              <button @click="atualizarStatus(tarefa.id, 'Em Andamento')" class="text-xs font-medium text-indigo-600 hover:text-indigo-800">Iniciar →</button>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-indigo-50 rounded-xl p-4 border border-indigo-100 shadow-inner">
        <h2 class="font-bold text-indigo-800 mb-4 flex justify-between">
          Em Andamento <span class="bg-indigo-200 text-indigo-800 px-2 py-0.5 rounded-full text-xs">{{ tarefasFiltradas('Em Andamento').length }}</span>
        </h2>
        <div class="space-y-3">
          <div v-for="tarefa in tarefasFiltradas('Em Andamento')" :key="tarefa.id" class="bg-white p-4 rounded-lg shadow-sm border border-slate-200 hover:shadow-md transition-shadow border-l-4 border-l-indigo-500">
            <span class="text-xs font-semibold px-2 py-1 rounded-md bg-indigo-50 text-indigo-600 mb-2 inline-block">{{ tarefa.prioridade }}</span>
            <h3 class="font-bold text-slate-800">{{ tarefa.titulo }}</h3>
            <p class="text-sm text-slate-500 mt-1">{{ tarefa.descricao }}</p>
            <div class="mt-4 flex justify-end">
              <button @click="atualizarStatus(tarefa.id, 'Concluído')" class="text-xs font-medium text-emerald-600 hover:text-emerald-800">Concluir ✓</button>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-emerald-50 rounded-xl p-4 border border-emerald-100 shadow-inner">
        <h2 class="font-bold text-emerald-800 mb-4 flex justify-between">
          Concluído <span class="bg-emerald-200 text-emerald-800 px-2 py-0.5 rounded-full text-xs">{{ tarefasFiltradas('Concluído').length }}</span>
        </h2>
        <div class="space-y-3">
          <div v-for="tarefa in tarefasFiltradas('Concluído')" :key="tarefa.id" class="bg-white p-4 rounded-lg shadow-sm border border-slate-200 opacity-75 border-l-4 border-l-emerald-500">
            <h3 class="font-bold text-slate-800 line-through decoration-slate-400">{{ tarefa.titulo }}</h3>
            <p class="text-sm text-slate-500 mt-1">Tarefa finalizada.</p>
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

const carregarTarefas = async () => {
  try {
    // CORREÇÃO: Removida a barra final
    const res = await axios.get('http://localhost:8000/tarefas')
    tarefas.value = res.data
  } catch (error) {
    console.error("Erro ao carregar tarefas", error)
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

onMounted(carregarTarefas)
</script>