<template>
  <li>
    {{ comment.content }}
    <span>-{{ comment.username }}</span>
    <i class="fas fa-times" @click="deleteComment"></i>
  </li>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Comment',
  props:{
    comment: Object,
  },
  methods: {
    deleteComment: function () {
      const token = localStorage.getItem('jwt')
      const headers = {
        Authorization: `JWT ${token}`
      }
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/comment/${this.comment.id}/`,
        // url: `https://upmygrade.shop/movies/comment/${this.comment.id}/`,
        headers,
      })
        .then(() => {
          this.$emit('get-detail')
        })
    }
  },
}
</script>

<style>

</style>