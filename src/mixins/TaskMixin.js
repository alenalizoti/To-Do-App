import axios from 'axios';
export const TaskMixin = {
    methods: {
      nextPage() {
        const lastPage = Math.ceil(this.allTasks.length / this.numberOfTasks);
        if (this.currentPage < lastPage) {
          this.currentPage++;
        }
      },
      previousPage() {
        if (this.currentPage > 1) {
          this.currentPage--;
        }
      },
      deleteTask(id) {
        axios.delete(`http://127.0.0.1:5000/deleteTask/${id}`)
          .then((response) => {
            console.log(response);
            this.getTasks();
          })
          .catch((err) => {
            console.log(err);
          });
      },
      update(id) {
        this.edit = true;
        axios.get(`http://127.0.0.1:5000/getTask/${id}`)
          .then((response) => {
            console.log(response);
            this.editedTask = response.data.data;
          })
          .catch((err) => {
            console.log(err);
          });
      },
      updateTask(id) {
        console.log(id);
        if (this.editedTask.task.length < 4) {
          this.error = 'Invalid input for update!';
          return;
        }
        axios.put(`http://127.0.0.1:5000/updateTask/${id}`, {
            editedTask: this.editedTask.task
          })
          .then((response) => {
            console.log(response);
            this.editedTask = '';
            this.edit = false;
            this.getTasks();
          })
          .catch((err) => {
            console.log(err);
          });
      },
      toggleCompletion(task) {
        task.completed = !task.completed;
        this.updateCompletedTask(task);
      },
      async updateCompletedTask(task) {
        const completedValue = task.completed ? 1 : 0;
        await axios.put(`http://127.0.0.1:5000/api/tasks/${task.id}`, {
            completed: completedValue
          })
          .then((response) => {
            console.log(response);
          })
          .catch((err) => {
            console.log(err);
          });
      }
    }
  };
  