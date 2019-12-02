<template>
  <div id="app">
    <div id="nav">
      <el-container>
        <el-button @click="show3 = !show3">Click Me</el-button>
        <el-container>
          <el-header>Header</el-header>
          <el-main>Main</el-main>
          <el-footer>Footer</el-footer>
          
        </el-container>
        <el-collapse-transition>
        <div v-show="show3">
          <el-aside width="200px">Aside</el-aside>
        </div>
        </el-collapse-transition>
      </el-container>
    </div>

    <!-- <router-view /> -->
  </div>
</template>

<script>
    export default {
    data: () => ({
      show3: true
    })
  }
</script>


<style>
  .el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }
  
  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }
  
  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 160px;
  }
  
  body > .el-container {
    margin-bottom: 40px;
  }
  
  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }
  
  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
</style>
