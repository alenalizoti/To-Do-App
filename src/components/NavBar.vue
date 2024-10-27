<template>
  <nav class="navbar navbar-expand-sm navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="javascript:void(0)">TODO</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mynavbar">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="navbar-collapse" id="mynavbar">
      <ul v-for="(item,index) in menu" :key="index" class="navbar-nav ">
        <li class="nav-item">
          <router-link class="nav-link" :to="item.url">{{item.name}}</router-link>
        </li>
      </ul>
    </div>
  </div>
</nav>
</template>

<script>
export default {
    data(){
        return{
            menu : [
                {url : '/', name : 'Active'},
                {url : '/completed' , name : 'Completed'}
            ]
        }
    }
}
</script>

<style>

</style>