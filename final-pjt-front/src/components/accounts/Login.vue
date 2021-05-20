<template>
  <div id="login-box">
    <div id="user-box">
      <label for="username"><i class="fas fa-user"></i></label>
      <input type="text" id="username" v-model="credentials.username" placeholder="username">
    </div>
    <div id="pw-box">
      <label for="password"><i class="fas fa-unlock"></i></label>
      <input type="password" id="password" v-model="credentials.password" @keyup.enter="login" placeholder="password">
    </div>
    <button @click="login" id="btn-login">Login</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      },
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials,
      })
        .then(res => {
          // console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$router.push('/')
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style>
  i {
    margin: 0 1rem;
    font-size: 1rem;
  }

  #user-box {
    color: white;
    display: inline-block;
    background-color: grey;
    background: grey;
    border-radius: 30px;
    padding: 1rem;
    margin-bottom: 1rem;
    width: 323.72px;
    text-align: start;
  }

  #pw-box {
    color: white;
    display: inline-block;
    background-color: grey;
    border-radius: 30px;
    padding: 1rem;
    margin-bottom: 1rem;
    width: 323.72px;
    text-align: start;
  }

  input {
    background: grey;
    border: none;
    color: white;
  }

  input::placeholder {
    color: white;
  }

  #btn-login {
    background-color: red;
    border: none;
    color: white;
    padding: 1rem;
    display: inline-block;
    cursor: pointer;
    width: 323.72px;
    height: 55px;
    border-radius: 30px;
    margin-bottom: 1rem;
  }

  #login-box {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
</style>