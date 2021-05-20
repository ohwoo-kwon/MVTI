<template>
  <div class="movie-list">
    <p>{{ $route.params.cMBTI }}</p>
    <p>{{ MBTI }}</p>
    <MovieCard v-for="(movie, index) in movies"
    :key="index"
    :movie="movie" />
  </div>
</template>

<script>
import axios from 'axios'
import MovieCard from './MovieCard.vue'

export default {
  name: 'Movies',
  components: {
    MovieCard,
  },
  props: {
    MBTI: Object,
  },
  data: function () {
    return {
      movies: null,
    }
  },
  methods: {

  },
  created: function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/'
    })
      .then(res => {
        this.movies = res.data
      })
      .catch(err => {
        console.log(err)
      })
  }
}
</script>

<style>
  .movie-list {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
  }
</style>