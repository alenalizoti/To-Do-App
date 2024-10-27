<template>
    <div class="container-fluid parent  justify-content-center align-items-center">
        <completed-tasks-vue></completed-tasks-vue>
    </div>
    <div class="bc2">
        
    </div>
</template>

<script>
import CompletedTasksVue from '@/components/CompletedTasks.vue'
export default {
    name : 'ComletedTasksView',
    components : {
        CompletedTasksVue
    }
}
</script>

<style scoped>
    .parent{
        background: url('@/assets/pozadina1.jpg');
        height: 35vh;
    }
    .bc2{
        background-color: #181824;
        height: 65vh;
        padding-top: 5em;
  }
</style>