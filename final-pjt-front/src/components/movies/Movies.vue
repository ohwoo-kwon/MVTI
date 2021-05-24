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
      checkMBTI: null,
      showMovies: null,
    }
  },
  methods: {
    showMBTI: function (mbti) {
      // const index = this.checkMBTI.indexOf(mbti)
      // if (index === -1) {
      //   this.checkMBTI.push(mbti)
      // } else {
      //   this.checkMBTI.splice(index, 1)
      // }

      if (this.checkMBTI === mbti) {
        this.showMovies = this.movies
        this.checkMBTI = null
      } else {
        this.checkMBTI = mbti
      }

      // 체크한 mbti만 돋보이게 하기
      const mbtiList = document.querySelectorAll('.mbti-list > li')
      // console.log(mbtiList)
      mbtiList.forEach(mbti => {
        // console.log(this.checkMBTI)
        if (mbti.innerText === this.checkMBTI) {
          mbti.setAttribute('style', 'font-size: 2rem;')
          return
        } else {
          mbti.setAttribute('style', 'font-size: 1rem;')
        }
      })
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
    checkMBTI: function (mbti) {
      this.showMovies = []
      // mbti_list.forEach(mbti => {
        // const result = this.movies.filter(movie => {
        //   return movie.mbti.some(object => object.mbti == mbti)
        // })
        // this.showMovies = result.concat(this.showMovies)
        // })
        this.showMovies = this.movies.filter(movie => {
          return movie.mbti.some(object => object.mbti == mbti)
      })
      // this.showMovies = new Set(this.showMovies)
      // this.showMovies = [...this.showMovies]
    },
    showMovies: function (showMovies) {
      // console.log(showMovies.length)
      if (showMovies.length === 0) {
        this.showMovies = this.movies
      }
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
    height: 2rem;
    margin-top: 1rem;
    padding: 0;
    display: flex;
    list-style: none;
    flex-wrap: wrap;
    justify-content: space-around;
    line-height: 2rem;
  }
</style>