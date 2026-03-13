<template>
  <div class="min-h-screen bg-slate-50">
    <nav class="bg-slate-900 text-white shadow-md">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16">
          <div class="font-bold text-xl tracking-tight">TaskFlow</div>
          <div class="flex space-x-4">
            <router-link to="/" class="hover:bg-slate-700 px-3 py-2 rounded-md transition-colors">Dashboard</router-link>
            <router-link to="/tarefas" class="hover:bg-slate-700 px-3 py-2 rounded-md transition-colors">Tarefas</router-link>
            <router-link to="/usuarios" class="hover:bg-slate-700 px-3 py-2 rounded-md transition-colors">Usuários</router-link>
          </div>
        </div>
      </div>
    </nav>

    <main class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
      <router-view></router-view>
    </main>
  </div>
</template>