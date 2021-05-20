<template>
  <div class="movie-list">
    <ul class="mbti-list">
      <MBTI v-for="(mbti, index) in mbtis"
      :key="index"
      :mbti="mbti"
      @show-mbti="showMBTI" />
    </ul>
    <MovieCard v-for="(movie, index) in showMovies"
    :key="index"
    :movie="movie" />
  </div>
</template>

<script>
import axios from 'axios'
import MovieCard from './MovieCard.vue'
import MBTI from './MBTI.vue'

export default {
  name: 'Movies',
  components: {
    MovieCard,
    MBTI,
  },
  props: {
    MBTI: Object,
  },
  data: function () {
    return {
      movies: null,
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
      showMovies: null,
    }
  },
  methods: {
    showMBTI: function (mbti) {
      this.checkMBTI.push(mbti)
    },
  },
  created: function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/'
    })
      .then(res => {
        this.movies = res.data
        this.showMovies = this.movies
      })
      .catch(err => {
        console.log(err)
      })
  },
  watch: {
    checkMBTI: function (mbti_list) {
      this.showMovies = []
      mbti_list.forEach(mbti => {
        const result = this.movies.filter(movie => {
          return movie.mbti.some(object => object.mbti == mbti)
        })
        this.showMovies = this.showMovies.concat(result)
      })
      this.showMovies = new Set(this.showMovies)
      this.showMovies = [...this.showMovies]
    }
  }
}
</script>

<style>
  .movie-list {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
  }

  .mbti-list {
    width: 100%;
    margin: 1rem;
    padding: 0;
    display: flex;
    list-style: none;
    flex-wrap: wrap;
    justify-content: space-around;
  }
</style>