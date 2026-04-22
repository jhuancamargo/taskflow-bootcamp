<template>
  <div class="max-w-3xl mx-auto">
    <div class="mb-8">
      <h1 class="text-3xl font-extrabold text-slate-900 tracking-tight">Criar Nova Tarefa</h1>
      <p class="text-slate-500 mt-1">Detalhe a atividade para que a equipe possa executar corretamente.</p>
    </div>
    
    <div class="bg-white p-8 rounded-xl shadow-sm border border-slate-200">
      <form @submit.prevent="salvarTarefa" class="space-y-6">
        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Título da Tarefa</label>
          <input v-model="form.titulo" type="text" placeholder="Ex: Implementar tela de login" class="w-full border border-slate-300 rounded-lg p-3 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition-all" required>
        </div>
        
        <div>
          <label class="block text-sm font-semibold text-slate-700 mb-2">Descrição Técnica</label>
          <textarea v-model="form.descricao" rows="4" placeholder="Descreva os requisitos técnicos..." class="w-full border border-slate-300 rounded-lg p-3 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition-all"></textarea>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <label class="block text-sm font-semibold text-slate-700 mb-2">Nível de Prioridade</label>
            <select v-model="form.prioridade" class="w-full border border-slate-300 rounded-lg p-3 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition-all bg-white">
              <option value="Baixa">Baixa</option>
              <option value="Média">Média</option>
              <option value="Alta">Alta</option>
            </select>
          </div>
          <div>
            <label class="block text-sm font-semibold text-slate-700 mb-2">Atribuir a (Responsáveis)</label>
            <select v-model="form.responsavel_ids" multiple class="w-full border border-slate-300 rounded-lg p-3 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition-all bg-white" required>
              <option v-for="u in usuarios" :key="u.id" :value="u.id">{{ u.nome }}</option>
            </select>
            <p class="text-xs text-slate-500 mt-1">Segure Ctrl/Cmd para selecionar múltiplos usuários</p>
          </div>
        </div>
        
        <div class="pt-4 border-t border-slate-100 mt-6 flex justify-end">
          <button type="submit" class="bg-indigo-600 text-white px-8 py-3 rounded-lg font-medium shadow-sm hover:bg-indigo-700 transition-colors">Criar Tarefa</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()
const usuarios = ref([])
const form = ref({ titulo: '', descricao: '', prioridade: 'Média', responsavel_ids: [] })

onMounted(async () => {
  const res = await axios.get('http://localhost:8000/usuarios')
  usuarios.value = res.data
})

const salvarTarefa = async () => {
  // Converter para integers
  const dados = {
    ...form.value,
    responsavel_ids: form.value.responsavel_ids.map(id => parseInt(id))
  }
  await axios.post('http://localhost:8000/tarefas', dados)
  router.push('/')
}
</script>