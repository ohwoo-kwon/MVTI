<template>
  <div>
    <div class="logo-container">
      <div id="logo-box">
        <img src="@/assets/logo.png/" alt="logo" style="margin-right: 1rem;">
        <a :href="$router.resolve({name: 'Movies'}).href"><img src="@/assets/MVTI2.png/" style="height: 30px; width: 170px;" alt="MVTI"></a>
        <!-- <a :href="$router.resolve({name: 'Movies'}).href" style="font-family: 'Mate SC', serif; font-weight:bold; font-size: 1.7rem;">M V T I</a> -->
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
    background: url(https://cdn.wallpapersafari.com/14/55/DRKqGr.jpg);
  }

  a {
    color: red;
    text-decoration: none;
    font-family: 'Pattaya', sans-serif;
  }

  .logo-container {
    width: 100%;
    margin: 1rem;
    padding-right: 2rem;
    padding-left: 2rem;
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

  a {
    text-decoration: none;
  }
</style>
