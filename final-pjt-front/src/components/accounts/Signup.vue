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
      // const username = this.credentials.username
      const password = this.credentials.password
      const passwordConfirmation = this.credentials.passwordConfirmation

      if (password !== passwordConfirmation) {
        alert('비밀번호와 비밀번호 확인이 일치하지 않습니다.')
      } else {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/accounts/signup/',
          // url: 'https://upmygrade.shop/accounts/signup/',
          data: this.credentials,
        })
          .then(() => {
            // console.log(res)
            this.$router.push({name:'Login'})
          })
          .catch(() => {
            alert('이미 사용 중인 아이디이거나, 아이디에 공백이 있습니다.')
          })
      }
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