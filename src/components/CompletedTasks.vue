<template>
  <div class="container ">
    <h1 class="text-light p-5">Completed tasks</h1>
    <div class="completed">
        <div class="tasks">
        <div v-for="task,index in firstTasks" :key="task.id" class="task">
          <div class="d-flex gap-3">
            <p class="text-light">{{ index +1 }}</p>
            <p class="text-decoration-line-through">{{ task.task }}</p>
          </div>
          <div class="options d-flex align-items-center gap-4">
            <i @click="deleteTaskMixin(task.id)" class="gg-trash"></i>
          </div>
        </div>
        <div class="buttons d-flex gap-3 mt-2 align-items-center">
          <button @click="previousPageMixin"  class="btn btn-primary" :disabled="checkPrevious">Back</button>
          <span class="currentPage">{{ currentPage }}</span>
          <button  @click="nextPageMixin" class="btn btn-primary" :disabled="checkNext">Next</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { TaskMixin } from '@/mixins/TaskMixin';
export default {
    data(){
        return {
            allTasks : [],
            numberOfTasks : 5,
            currentPage : 1,
            error : '',
            editedTask : '',
            edit : false,
        }
        
    },
    methods : {
        getCompletedTasks(){
            axios.get('http://127.0.0.1:5000/completedTasks')
            .then((response => {
                this.allTasks = response.data.data;
                console.log(this.allTasks);
            }))
            .catch((err => {
                console.log(err);
            }))
        },
        deleteTaskMixin(id){
            this.deleteTask(id);
            location.reload();
        },
        toggleCompletionMixin(task){
            this.toggleCompletion(task);
        },
        nextPageMixin(){
            this.nextPage();
        },
        previousPageMixin(){
            this.previousPage();
        },

    },
    mounted(){
        this.getCompletedTasks();
    },
    mixins : [TaskMixin],
    computed : {
        firstTasks(){
            const start = (this.currentPage - 1) * 5;
            const end = this.numberOfTasks + start;

            return this.allTasks.slice(start,end);
        },
        checkNext(){
            const lastPage = Math.ceil(this.allTasks.length / this.numberOfTasks);
            if(this.currentPage < lastPage){
                return false;
            }
                return true
            },
        checkPrevious(){

            if(this.currentPage > 1){
                return false
            }
                return true
            }
    }
   
}
</script>

<style>

</style>