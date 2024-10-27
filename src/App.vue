<template>
  <nav-bar-vue></nav-bar-vue>
  <router-view/>
</template>
<script>
import NavBarVue from "./components/NavBar.vue";
export default{
  components : {
    NavBarVue
  }
}
</script>
<style>

</style>
