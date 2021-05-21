<template>
  <div id="card">
    <img :src="movie.poster_path" alt="movie_poster" style="width: 200px;"
    @click="showDetail">
    <div id="movie-detail" v-show="detail">
      <MovieDetail :movie="movie"/>
    </div>
  </div>
</template>

<script>
import MovieDetail from './MovieDetail.vue'

export default {
  name: 'MovieCard',
  components: {
    MovieDetail,
  },
  data: function () {
    return {
      detail: false,
    }
  },
  props: {
    movie: Object,
  },
  methods: {
    showDetail: function () {
      this.detail = !this.detail
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
    display: flex;
  }
</style>