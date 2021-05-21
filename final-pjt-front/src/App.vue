<template>
  <div>
    <div class="container">
      <div id="logo-box">
        <img src="@/assets/logo.png/" alt="logo">
        <a :href="$router.resolve({name: 'Movies'}).href">MVTI</a>
      </div>
      <div v-if="isLogin">
        <router-link to="#" @click.native="logout">Logout</router-link>
      </div>
      <div v-else class="box">
        <router-link :to="{ name: 'Login' }">Login</router-link>
        <router-link :to="{ name: 'Signup' }">Signup</router-link>
      </div>
    </div>
    <div id="router-box">
      <router-view @login="isLogin = true" />
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push('Login')
    },
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
  }
}
</script>

<style>
  * {
    box-sizing: border-box;
  }

  body {
    background-color: black;
    color: red;
    margin: 0;
    height: 100vh;
  }

  a {
    color: red;
    text-decoration: none;
  }

  .container {
    margin: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .box > a {
    margin: 1rem;
  }

  #router-box {
    text-align: center;
    margin: auto;
  }

  a {
    font-size: 1.3rem;
  }
  
  img {
    width: 50px;
  }

  #logo-box {
    display: flex;
    align-items: center;
  }
</style>
