<template>
  <div id="signup-box">
    <div id="user-box">
      <label for="username"><i class="fas fa-user"></i></label>
      <input type="text" id="username" v-model="credentials.username" placeholder="username">
    </div>
    <div id="pw-box">
      <label for="password"><i class="fas fa-unlock"></i></label>
      <input type="password" id="password" v-model="credentials.password" placeholder="password">
    </div>
    <div id="pw-box">
      <label for="password-confirmation"><i class="fas fa-unlock"></i></label>
      <input type="password" id="password-confirmation" v-model="credentials.passwordConfirmation" @keyup.enter="signup" placeholder="password confrimation">
    </div>
    <button @click="signup" id="btn-login">Signup</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Singup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      },
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials,
      })
        .then(() => {
          // console.log(res)
          this.$router.push({name:'Login'})
        })
        .catch(err => {
          console.log(err)
        })
    },
  }
}
</script>

<style>
  #signup-box {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

</style>