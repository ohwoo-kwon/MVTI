<template>
  <div>
    <div class="container">
      <div id="logo-box">
        <img src="@/assets/logo.png/" alt="logo">
        <router-link :to="{ name: 'Movies', params: { cMBTI: checkMBTI } }">MVTI</router-link>
      </div>
      <div v-if="isLogin">
        <router-link to="#" @click.native="logout">Logout</router-link>
      </div>
      <div v-else class="box">
        <router-link :to="{ name: 'Login' }">Login</router-link>
        <router-link :to="{ name: 'Signup' }">Signup</router-link>
      </div>
    </div>
    <div>
      <ul class="mbti-list">
        <MBTI v-for="(mbti, index) in mbtis"
        :key="index"
        :mbti="mbti"
        @show-mbti="showMbti" />
      </ul>
    </div>
    <div id="router-box">
      <router-view @login="isLogin = true"/>
    </div>
  </div>
</template>

<script>
import MBTI from './components/MBTI.vue'

export default {
  name: 'App',
  components: {
    MBTI,
  },
  data: function () {
    return {
      isLogin: false,
      mbtis: [
        'INTJ',
        'INTP',
        'ENTJ',
        'ENTP',
        'INFP',
        'ENFP',
        'INFJ',
        'ENFJ',
        'ISTJ',
        'ISFJ',
        'ESTJ',
        'ESFJ',
        'ISTP',
        'ESTP',
        'ISFP',
        'ESFP'
      ],
      checkMBTI: [],
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push('Login')
    },
    showMbti: function (mbti) {
      this.checkMBTI.push(mbti)
      // this.checkMBTI.map(mbti => console.log(mbti))
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

  .mbti-list {
    margin: 1rem;
    padding: 0;
    display: flex;
    list-style: none;
    flex-wrap: wrap;
    justify-content: space-around;
  }
</style>
