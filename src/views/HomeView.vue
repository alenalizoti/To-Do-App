<template>
  <div class="bc">
    <div class="container ">
      <div class="head mb-2">
        <h2>T O D O</h2>
        <i class="gg-edit-highlight light-icon"></i>
      </div>
      <div class="input">
        <input type="text" placeholder="Create a new task.." v-model="newTask">
      </div>
      <div class="category form-group">
        <select class="form-control" name="" id="" v-model="category">
          <option value="" checked>Choose...</option>
          <option v-for="category in categories" :key="category.id" :value="category.id">{{ category.naziv }}</option>
        </select>
      </div>
      <p class="text-center text-danger">{{ error }}</p>
      <div class="tasks">
        <div v-for="task in firstTasks" :key="task.id" class="task">
          <div class="d-flex gap-3">
            <input v-model="task.completed" @click="toggleCompletion(task)" class="checkbox" type="checkbox">
            <p>{{ task.task }}</p>
          </div>
          <div class="options d-flex align-items-center gap-4">
            <i @click="update(task.id)" class="gg-pen"></i>
            <i @click="deleteTask(task.id)" class="gg-trash"></i>
          </div>
        </div>
        <div class="buttons d-flex gap-3 mt-2 align-items-center">
          <button @click="previousPage"  class="btn btn-primary" :disabled="checkPrevious">Back</button>
          <span class="currentPage">{{ currentPage }}</span>
          <button  @click="nextPage" class="btn btn-primary" :disabled="checkNext">Next</button>
        </div>
      </div>
      <button @click="addTask" class="btn btn-primary add-btn mt-4">Add task</button>
    </div>
    <div v-if="edit" class="edit-task input">
      <div class="edit-input d-flex justify-content-center mt-3 gap-2 align-items-center">
        <input v-model="editedTask.task" type="text" placeholder="Edit taks...">
        <button @click="updateTask(editedTask.id)"  class="btn btn-primary">Update</button>
      </div>
    </div>
  </div>
  <div class="bc2">
  </div>
</template>

<script>
import axios from 'axios';

export default   {
  name: 'HomeView',
  data(){
    return{
      newTask : '',
      allTasks : [],
      numberOfTasks : 5,
      currentPage : 1,
      error : '',
      editedTask : '',
      edit : false,
      categories : [],
      category : ''
    }
  },
  methods: {
    addTask(){
      if(this.newTask.length < 4){
        this.error = 'Error, invalid number of characters!';
        return
      }
      if(!this.category){
        this.error = 'Choose category!'
        return
      }
      this.error = '';
      axios.post('http://127.0.0.1:5000/addTask',{
        newTask : this.newTask,
        category : this.category
      })
      .then((response =>{
        console.log(response.data);
        location.reload();
      }))
      .catch((error => {
        console.log(error);
      }))
    },
    getTasks(){
    axios.get('http://127.0.0.1:5000/tasks')
      .then((response => {
        console.log(response);
        this.allTasks = response.data.data;
        console.log(this.allTasks);
        this.getCategory()
      }))
      .catch((error =>{
        console.log(error);
      }))
    },
    nextPage(){
      const lastPage = Math.ceil(this.allTasks.length / this.numberOfTasks);
      if(this.currentPage < lastPage){
        this.currentPage++;
      }
    },
    previousPage(){
      if(this.currentPage > 1){
        this.currentPage--;
      }
    },
    deleteTask(id){
      axios.delete(`http://127.0.0.1:5000/deleteTask/${id}`)
      .then((response =>{
        console.log(response);
        this.getTasks();
      }))
      .catch((err =>{
        console.log(err);
      }))
    },
    update(id){
      this.edit = true;
      axios.get(`http://127.0.0.1:5000/getTask/${id}`)
      .then((response => {
        console.log(response);
        this.editedTask = response.data.data;
      }))
      .catch((err => {
        console.log(err);
      }))
    },
    updateTask(id){
      console.log(id);
      if(this.editedTask.task.length < 4){
        this.error = 'Invalid inout for update!';
        return
      }
      axios.put(`http://127.0.0.1:5000/updateTask/${id}`,{
        editedTask : this.editedTask.task
      })
      .then((response =>{
        console.log(response);
        this.editedTask = '';
        this.edit = false;
        this.getTasks();
      }))
      .catch((err => {
        console.log(err);
      }))
    },toggleCompletion(task){
      task.completed = !task.completed;
      this.updateCompletedTask(task);
      location.reload();
    },
    async updateCompletedTask(task){
      const completedValue = task.completed ? 1 : 0;
      await axios.put(`http://127.0.0.1:5000/api/tasks/${task.id}`,{
        completed : completedValue
      })
      .then((response => {
        console.log(response);
      }))
      .catch((err => {
        console.log(err);
      }))
    },
    getCategory(){
      axios.get('http://127.0.0.1:5000/api/category')
      .then((response => {
        console.log(response);
        this.categories = response.data.data;
        console.log(this.categories);
      }))
      .catch((err => {
        console.log(err);
      }))
    }
  },
  mounted(){
    this.getTasks()
  },
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
  },
  
}
</script>
<style >
  .container{
    padding: 0 20em;
    /* margin-top: 5em; */
  }
  .head{
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #fff;
  }
  .light-icon{
    cursor: pointer;
  }
  .input{
    display: flex;
    justify-content: center;
    /* margin-bottom: 2em; */
  }
  .input input{
    width: 80%;
    padding: 0.5em;
    border-radius: 5px;
    background-color: #25273c;
    border: none;
    height: 3em;
    color: #5e6078;
    /* margin-top: 2em; */
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
  }
  .bc{
    background-image: url("@/assets/pozadina1.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    height: 35vh;
    padding-top: 5em;
  }
  .tasks{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: 2em;
    background-color: #25273c;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    position: relative;
    width: 80%;
    margin: 0 auto;
    padding: 1em;
  }
  .task{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 2em;
    width: 80%;
    background-color: #25273c;
    color: #5e6078;
    font-size: 1em;
    height: 3.2em;
  }
  .task p{
    padding-top: 0.7em;
  }
  .checkbox{
    transform: scale(1.4);
  }
  .bc2{
    background-color: #181824;
    height: 65vh;
    padding-top: 5em;
  }
  .add-btn{
    display: block;
    margin: 0 auto;
    position: relative;
  }
  .buttons{
    background-color: #25273c;
  }
  .currentPage{
    color: #5e6078;
  }
  .category{
    width: 50%;
    display: block;
    margin: 0 auto;
    margin-top: 1em;
    
  }
  .category select{
    background-color: #25273c;
    color: #5e6078;
    text-align: center;
  }
</style>
