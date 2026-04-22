<template>
  <div class="max-w-6xl mx-auto">
    <div class="mb-8">
      <h1 class="text-3xl font-extrabold text-slate-900">Membros da Equipe</h1>
      <p class="text-slate-500">Cadastre os usuários para atribuir tarefas no Kanban.</p>
    </div>
    
    <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200 mb-8">
      <form @submit.prevent="salvarUsuario" class="grid grid-cols-1 md:grid-cols-4 gap-4 items-end">
        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-1">Nome</label>
          <input v-model="form.nome" type="text" class="w-full border border-slate-300 rounded-lg p-2 outline-none focus:ring-2 focus:ring-indigo-500" required>
        </div>
        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-1">E-mail</label>
          <input v-model="form.email" type="email" class="w-full border border-slate-300 rounded-lg p-2 outline-none focus:ring-2 focus:ring-indigo-500" required>
        </div>
        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-1">Função</label>
          <input v-model="form.funcao" type="text" placeholder="Ex: Desenvolvedor" class="w-full border border-slate-300 rounded-lg p-2 outline-none focus:ring-2 focus:ring-indigo-500" required>
        </div>
        <button type="submit" class="bg-indigo-600 text-white px-4 py-2 rounded-lg font-medium hover:bg-indigo-700 transition-colors h-[42px]">
          Adicionar Membro
        </button>
      </form>
    </div>

    <div class="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
      <table class="w-full text-left">
        <thead class="bg-slate-50 border-b border-slate-200">
          <tr>
            <th class="p-4 text-sm font-semibold text-slate-600">Nome</th>
            <th class="p-4 text-sm font-semibold text-slate-600">E-mail</th>
            <th class="p-4 text-sm font-semibold text-slate-600">Função</th>
            <th class="p-4 text-sm font-semibold text-slate-600 text-right"></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in usuarios" :key="user.id" class="border-b border-slate-100 hover:bg-slate-50">
            <td class="p-4 text-slate-800 font-medium">{{ user.nome }}</td>
            <td class="p-4 text-slate-600">{{ user.email }}</td>
            <td class="p-4 text-slate-600">{{ user.funcao }}</td>
            <td class="p-4 text-right">
              <button
                @click="excluirUsuario(user.id, user.nome)"
                class="w-6 h-6 inline-flex items-center justify-center rounded-full text-slate-400 hover:bg-red-100 hover:text-red-600 transition cursor-pointer"
                title="Excluir usuário"
              >
                ×
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

// REMOVIDO A BARRA DO FINAL DA URL
const api = 'http://localhost:8000/usuarios' 
const usuarios = ref([])
const form = ref({ nome: '', email: '', funcao: '' })

const carregarUsuarios = async () => {
  try {
    const res = await axios.get(api)
    usuarios.value = res.data
  } catch (e) { console.error(e) }
}

const salvarUsuario = async () => {
  try {
    await axios.post(api, form.value)
    form.value = { nome: '', email: '', funcao: '' }
    await carregarUsuarios()
  } catch (e) { alert("Erro ao salvar: " + e.response?.data?.detail || e.message) }
}

const excluirUsuario = async (id, nome) => {
  const confirmar = confirm(
    `Deseja realmente excluir o usuário "${nome}"? Isso pode remover também as tarefas associadas a ele.`
  )
  if (!confirmar) return

  try {
    await axios.delete(`${api}/${id}`)
    await carregarUsuarios()
  } catch (e) {
    alert("Erro ao excluir: " + (e.response?.data?.detail || e.message))
  }
}

onMounted(carregarUsuarios)
</script>