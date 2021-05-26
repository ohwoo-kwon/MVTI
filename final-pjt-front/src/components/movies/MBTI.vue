<template>
  <li :id="mbti" @click="showMbti">
    {{ mbti }}
  </li>
</template>

<script>
export default {
  name: 'MBTI',
  props: {
    mbti: String,
  },
  methods: {
    showMbti: function () {
      // console.log(this.mbti)
      this.$emit('show-mbti', this.mbti)
    }
  },
}
</script>

<style>
  li {
    caret-color: none;
    cursor: pointer;
    transition: transform 0.5s;
    font-family: 'Reggae One', cursive;
  }

  li:hover {
    transform: translate(0, -10px);
  }

  #INTJ {
    color: rgb(254, 148, 48);
  }
  #INTP {
    color: rgb(252, 54, 69);
  }
  #ENTJ {
    color: rgb(202, 124, 42);
  }
  #ENTP {
    color: rgb(252, 0, 23);
  }
  #INFP {
    color: rgb(254, 190, 191);
  }
  #ENFP {
    color: rgb(254, 125, 130);
  }
  #INFJ {
    color: rgb(255, 201, 137);
  }
  #ENFJ {
    color: rgb(254, 175, 82);
  }
  #ISTJ {
    color: rgb(42, 101, 45);
  }
  #ISFJ {
    color: rgb(107, 222, 65);
  }
  #ESTJ {
    color: rgb(48, 72, 48);
  }
  #ESFJ {
    color: rgb(84, 152, 49);
  }
  #ISTP {
    color: rgb(48, 84, 243);
  }
  #ESTP {
    color: rgb(0, 53, 247);
  }
  #ISFP {
    color: rgb(189, 194, 250);
  }
  #ESFP {
    color: rgb(123, 134, 249);
  }
</style>