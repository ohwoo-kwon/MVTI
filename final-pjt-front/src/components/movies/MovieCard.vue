<template>
  <div id="card">
    <img :src="movie.poster_path" alt="movie_poster" style="width: 200px;"
    @click="showDetail">
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movie: Object,
  },
  methods: {
    showDetail: function () {
      // axios({
      //   method: 'get',
      //   url: `http://127.0.0.1:8000/movies/${this.movie.movie_id}`
      // })
      //   .then(res => {
      //     console.log(res)
      //   })
      //   .catch(err => {
      //     console.log(err)
      //   })
    }
  }
}
</script>

<style>
  #card {
    margin: 1rem;
  }
</style>