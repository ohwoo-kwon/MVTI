<template>
  <div id="card">
    <img @click="getDetail()" :src="movie.poster_path" alt="movie_poster" style="width: 200px;" data-bs-toggle="modal" :data-bs-target="`#d${movie.id}`">
    <!-- Modal -->
    <div class="modal fade" :id="`d${movie.id}`" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="text-end">
            <button type="button" class="btn-close text-end" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-header">
            <img :src="movie.poster_path" alt="movie_poster" style="width: 200px;">
            <div class="movie-detail ms-3">
              <p style="font-size: 1.8rem; font-weight: bold;">{{ this.movie.title }}</p>
              <p class="movie-overview">{{ movie.overview }}</p>
            </div>
          </div>
          <div class="modal-comment">
            <ul>
              <Comment v-for="(comment, index) in movieDetail.comment_set"
              :key="index"
              :comment="comment"
              @get-detail="getDetail"
              />
            </ul>
            <div>
              <input type="text" v-model="inputText" @keyup.enter="createComment" placeholder="댓글 쓰기">
              <!-- <i class="fas fa-plus" @click="createComment"></i> -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Comment from './Comment.vue'

export default {
  name: 'MovieCard',
  components: {
    Comment,
  },
  data: function () {
    return {
      movieDetail: {
        id: null,
        comment_set: [],
        mbti: [],
        title: '',
        overview: '',
        poster_path: '',
        movie_id: 1,
      },
      inputText: null,
    }
  },
  props: {
    movie: Object,
  },
  methods: {
    createComment: function () {
      const token = localStorage.getItem('jwt')
      const data = {
        content: this.inputText,
      }
      const headers = {
        Authorization: `JWT ${token}`
      }
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.movie.movie_id}/comment/`,
        // url: `https://upmygrade.shop/${this.movie.movie_id}/comment/`,
        data,
        headers,
      })
        .then(() => {
          this.getDetail()
        })
        .catch(err => {
          console.log(err)
        })
      this.inputText = null
    },
    getDetail: function () {
      axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/${this.movie.movie_id}/`
      // url: `https://upmygrade.shop/movies/${this.movie.movie_id}/`
    })
      .then(res => {
        this.movieDetail = res.data
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  created: function () {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/${this.movie.movie_id}/`
      // url: `https://upmygrade.shop/movies/${this.movie.movie_id}/`
    })
      .then(res => {
        this.movieDetail = res.data
      })
      .catch(err => {
        console.log(err)
      })
  },
}
</script>

<style>
  #card {
    margin: 1rem;
    display: flex;
    cursor: pointer;
    border: 1px solid rgb(110, 110, 110, 0.3);
    border-radius: 10px;
  }

  #card > img {
    border-radius: 10px;
    transition: transform 0.5s;
  }

  #card > img:hover {
    transform: scale(1.1);
    border: 1px solid rgb(110, 110, 110, 0.3);
  }

  .movie-detail {
    height: 300px;
    width: 100%;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 8;
    -webkit-box-orient: vertical;
  }

  .modal-content {
    color:grey;
    background: url('../../assets/detail-background3.png') no-repeat;
    background-size: 500px 100%;
    font-family: 'Nanum Pen Script', cursive;
    font-size: 1.5rem;
  }

  ul {
    list-style: none;
  }
</style>