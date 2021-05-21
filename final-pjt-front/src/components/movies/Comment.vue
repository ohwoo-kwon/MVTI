<template>
  <li>
    {{ comment.content }}
    <span>-{{ comment.username }}</span>
    <button @click="deleteComment">삭제</button>
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