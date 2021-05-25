<template>
  <div class="movie-list">
    <ul class="mbti-list">
      <MBTI v-for="(mbti, index) in mbtis"
      :key="index"
      :mbti="mbti"
      @show-mbti="showMBTI" />
    </ul>
    <div id="image-slide">

      <div v-show="checkMBTI === 'INTJ'" style="color: rgb(254, 148, 48);">
        <p style="font-family: 'Black And White Picture', sans-serif; font-size:2rem;">용의주도한 전략가 / 과학자형</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">전체적인 부분을 조합하여 비전을 제시하는 사람들</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">대부분 똑똑하고 신념이 뚜렷해서 악역이 많음</p>
        <carousel-3d v-show="checkMBTI === 'INTJ'">
          <slide :index="0">
            <img src="../../assets/INTJ/1.jpg" alt="">
          </slide>
          <slide :index="1">
            <img src="../../assets/INTJ/2.jpg" alt="">
          </slide>
          <slide :index="2">
            <img src="../../assets/INTJ/3.jpg" alt="">
          </slide>
          <slide :index="3">
            <img src="../../assets/INTJ/4.jpg" alt="">
          </slide>
          <slide :index="4">
            <img src="../../assets/INTJ/5.jpg" alt="">
          </slide>
          <slide :index="5">
            <img src="../../assets/INTJ/6.jpg" alt="">
          </slide>
          <slide :index="6">
            <img src="../../assets/INTJ/7.jpg" alt="">
          </slide>
          <slide :index="7">
            <img src="../../assets/INTJ/8.jpg" alt="">
          </slide>
          <slide :index="8">
            <img src="../../assets/INTJ/9.jpg" alt="">
          </slide>
          <slide :index="9">
            <img src="../../assets/INTJ/10.jpg" alt="">
          </slide>
          <slide :index="10">
            <img src="../../assets/INTJ/11.jpg" alt="">
          </slide>
          <slide :index="11">
            <img src="../../assets/INTJ/12.jpg" alt="">
          </slide>
          <slide :index="12">
            <img src="../../assets/INTJ/13.jpg" alt="">
          </slide>
          <slide :index="13">
            <img src="../../assets/INTJ/14.jpg" alt="">
          </slide>
          <slide :index="14">
            <img src="../../assets/INTJ/15.jpg" alt="">
          </slide>
        </carousel-3d>
      </div>

      <div v-show="checkMBTI === 'INTP'" style="color: rgb(252, 54, 69);">
        <p style="font-family: 'Black And White Picture', sans-serif; font-size:2rem;">논리적인 사색가 / 아이디어 뱅크형</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">비평적인 관점을 가지고 있는 뛰어난 전략가들</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">수줍은 천재, 까칠한 천재, 비운의 천재 등등 천제 집합체</p>
        <carousel-3d v-show="checkMBTI === 'INTP'">
          <slide :index="0">
            <img src="../../assets/INTP/1.jpg" alt="">
          </slide>
          <slide :index="1">
            <img src="../../assets/INTP/2.jpg" alt="">
          </slide>
          <slide :index="2">
            <img src="../../assets/INTP/3.jpg" alt="">
          </slide>
          <slide :index="3">
            <img src="../../assets/INTP/4.jpg" alt="">
          </slide>
          <slide :index="4">
            <img src="../../assets/INTP/5.jpg" alt="">
          </slide>
          <slide :index="5">
            <img src="../../assets/INTP/6.jpg" alt="">
          </slide>
          <slide :index="6">
            <img src="../../assets/INTP/7.jpg" alt="">
          </slide>
          <slide :index="7">
            <img src="../../assets/INTP/8.jpg" alt="">
          </slide>
          <slide :index="8">
            <img src="../../assets/INTP/9.jpg" alt="">
          </slide>
          <slide :index="9">
            <img src="../../assets/INTP/10.jpg" alt="">
          </slide>
          <slide :index="10">
            <img src="../../assets/INTP/11.jpg" alt="">
          </slide>
          <slide :index="11">
            <img src="../../assets/INTP/12.jpg" alt="">
          </slide>
          <slide :index="12">
            <img src="../../assets/INTP/13.jpg" alt="">
          </slide>
          <slide :index="13">
            <img src="../../assets/INTP/14.jpg" alt="">
          </slide>
          <slide :index="14">
            <img src="../../assets/INTP/15.jpg" alt="">
          </slide>
          <slide :index="15">
            <img src="../../assets/INTP/16.jpg" alt="">
          </slide>
        </carousel-3d>
      </div>
      
      <div v-show="checkMBTI === 'ENTJ'" style="color: rgb(202, 124, 42);">
        <p style="font-family: 'Black And White Picture', sans-serif; font-size:2rem;">대담한 통솔자 / 지도자형</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">비전을 가지고 사람들을 활력적으로 이끄는 사람들</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">무조건 쎄고 치명적이며 항상 리드함</p>
        <carousel-3d v-show="checkMBTI === 'ENTJ'">
          <slide :index="0">
            <img src="../../assets/ENTJ/1.jpg" alt="">
          </slide>
          <slide :index="1">
            <img src="../../assets/ENTJ/2.jpg" alt="">
          </slide>
          <slide :index="2">
            <img src="../../assets/ENTJ/3.jpg" alt="">
          </slide>
          <slide :index="3">
            <img src="../../assets/ENTJ/4.jpg" alt="">
          </slide>
          <slide :index="4">
            <img src="../../assets/ENTJ/5.jpg" alt="">
          </slide>
          <slide :index="5">
            <img src="../../assets/ENTJ/6.jpg" alt="">
          </slide>
          <slide :index="6">
            <img src="../../assets/ENTJ/7.jpg" alt="">
          </slide>
          <slide :index="7">
            <img src="../../assets/ENTJ/8.jpg" alt="">
          </slide>
          <slide :index="8">
            <img src="../../assets/ENTJ/9.jpg" alt="">
          </slide>
          <slide :index="9">
            <img src="../../assets/ENTJ/10.jpg" alt="">
          </slide>
          <slide :index="10">
            <img src="../../assets/ENTJ/11.jpg" alt="">
          </slide>
          <slide :index="11">
            <img src="../../assets/ENTJ/12.jpg" alt="">
          </slide>
          <slide :index="12">
            <img src="../../assets/ENTJ/13.jpg" alt="">
          </slide>
          <slide :index="13">
            <img src="../../assets/ENTJ/14.jpg" alt="">
          </slide>
          <slide :index="14">
            <img src="../../assets/ENTJ/15.jpg" alt="">
          </slide>
          <slide :index="15">
            <img src="../../assets/ENTJ/16.jpg" alt="">
          </slide>
          <slide :index="16">
            <img src="../../assets/ENTJ/17.jpg" alt="">
          </slide>
        </carousel-3d>
      </div>

      <div v-show="checkMBTI === 'ENTP'" style="color: rgb(252, 0, 23);">
        <p style="font-family: 'Black And White Picture', sans-serif; font-size:2rem;">뜨거운 논쟁을 즐기는 변론가 / 발명가형</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">풍부한 상상력은 가지고 새로운 것에 도전하는 사람들</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">수줍은 또라이, 까칠한 또라이, 비운의 또라이 등등 또라이 집합체</p>
        <carousel-3d v-show="checkMBTI === 'ENTP'">
          <slide :index="0">
            <img src="../../assets/ENTP/1.jpg" alt="">
          </slide>
          <slide :index="1">
            <img src="../../assets/ENTP/2.jpg" alt="">
          </slide>
          <slide :index="2">
            <img src="../../assets/ENTP/3.jpg" alt="">
          </slide>
          <slide :index="3">
            <img src="../../assets/ENTP/4.jpg" alt="">
          </slide>
          <slide :index="4">
            <img src="../../assets/ENTP/5.jpg" alt="">
          </slide>
          <slide :index="5">
            <img src="../../assets/ENTP/6.jpg" alt="">
          </slide>
          <slide :index="6">
            <img src="../../assets/ENTP/7.jpg" alt="">
          </slide>
          <slide :index="7">
            <img src="../../assets/ENTP/8.jpg" alt="">
          </slide>
          <slide :index="8">
            <img src="../../assets/ENTP/9.jpg" alt="">
          </slide>
          <slide :index="9">
            <img src="../../assets/ENTP/10.jpg" alt="">
          </slide>
          <slide :index="10">
            <img src="../../assets/ENTP/11.jpg" alt="">
          </slide>
          <slide :index="11">
            <img src="../../assets/ENTP/12.jpg" alt="">
          </slide>
          <slide :index="12">
            <img src="../../assets/ENTP/13.jpg" alt="">
          </slide>
          <slide :index="13">
            <img src="../../assets/ENTP/14.jpg" alt="">
          </slide>
          <slide :index="14">
            <img src="../../assets/ENTP/15.jpg" alt="">
          </slide>
          <slide :index="15">
            <img src="../../assets/ENTP/16.jpg" alt="">
          </slide>
          <slide :index="16">
            <img src="../../assets/ENTP/17.jpg" alt="">
          </slide>
        </carousel-3d>
      </div>

      <div v-show="checkMBTI === 'INFP'" style="color: rgb(254, 190, 191);">
        <p style="font-family: 'Black And White Picture', sans-serif; font-size:2rem;">열정적인 중재자 / 잔다르크형</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">이상적인 세상을 만들어 가는 사람들</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">감성적인 영화에 나오는 외유내강형 캐릭터</p>
        <carousel-3d v-show="checkMBTI === 'INFP'">
          <slide :index="0">
            <img src="../../assets/INFP/1.jpg" alt="">
          </slide>
          <slide :index="1">
            <img src="../../assets/INFP/2.jpg" alt="">
          </slide>
          <slide :index="2">
            <img src="../../assets/INFP/3.jpg" alt="">
          </slide>
          <slide :index="3">
            <img src="../../assets/INFP/4.jpg" alt="">
          </slide>
          <slide :index="4">
            <img src="../../assets/INFP/5.jpg" alt="">
          </slide>
          <slide :index="5">
            <img src="../../assets/INFP/6.jpg" alt="">
          </slide>
          <slide :index="6">
            <img src="../../assets/INFP/7.jpg" alt="">
          </slide>
          <slide :index="7">
            <img src="../../assets/INFP/8.jpg" alt="">
          </slide>
          <slide :index="8">
            <img src="../../assets/INFP/9.jpg" alt="">
          </slide>
          <slide :index="9">
            <img src="../../assets/INFP/10.jpg" alt="">
          </slide>
          <slide :index="10">
            <img src="../../assets/INFP/11.jpg" alt="">
          </slide>
          <slide :index="11">
            <img src="../../assets/INFP/12.jpg" alt="">
          </slide>
          <slide :index="12">
            <img src="../../assets/INFP/13.jpg" alt="">
          </slide>
          <slide :index="13">
            <img src="../../assets/INFP/14.jpg" alt="">
          </slide>
          <slide :index="14">
            <img src="../../assets/INFP/15.jpg" alt="">
          </slide>
        </carousel-3d>

      </div>

      <div v-show="checkMBTI === 'ENFP'" style="color: rgb(254, 125, 130);">
        <p style="font-family: 'Black And White Picture', sans-serif; font-size:2rem;">재기발랄한 활동가 / 스파크형</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">열정적으로 새로운 관계를 만드는 사람들</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">명랑한 캐릭터들, 코미디에 자주 등장</p>
        <carousel-3d v-show="checkMBTI === 'ENFP'">
          <slide :index="0">
            <img src="../../assets/ENFP/1.jpg" alt="">
          </slide>
          <slide :index="1">
            <img src="../../assets/ENFP/2.jpg" alt="">
          </slide>
          <slide :index="2">
            <img src="../../assets/ENFP/3.jpg" alt="">
          </slide>
          <slide :index="3">
            <img src="../../assets/ENFP/4.jpg" alt="">
          </slide>
          <slide :index="4">
            <img src="../../assets/ENFP/5.jpg" alt="">
          </slide>
          <slide :index="5">
            <img src="../../assets/ENFP/6.jpg" alt="">
          </slide>
          <slide :index="6">
            <img src="../../assets/ENFP/7.jpg" alt="">
          </slide>
          <slide :index="7">
            <img src="../../assets/ENFP/8.jpg" alt="">
          </slide>
          <slide :index="8">
            <img src="../../assets/ENFP/9.jpg" alt="">
          </slide>
          <slide :index="9">
            <img src="../../assets/ENFP/10.jpg" alt="">
          </slide>
          <slide :index="10">
            <img src="../../assets/ENFP/11.jpg" alt="">
          </slide>
          <slide :index="11">
            <img src="../../assets/ENFP/12.jpg" alt="">
          </slide>
          <slide :index="12">
            <img src="../../assets/ENFP/13.jpg" alt="">
          </slide>
          <slide :index="13">
            <img src="../../assets/ENFP/14.jpg" alt="">
          </slide>
          <slide :index="14">
            <img src="../../assets/ENFP/15.jpg" alt="">
          </slide>
          <slide :index="15">
            <img src="../../assets/ENFP/16.jpg" alt="">
          </slide>
          <slide :index="16">
            <img src="../../assets/ENFP/17.jpg" alt="">
          </slide>
        </carousel-3d>
      </div>

      <div v-show="checkMBTI === 'INFJ'" style="color: rgb(255, 201, 137);">
        <p style="font-family: 'Black And White Picture', sans-serif; font-size:2rem;">선의의 옹호자 / 예언자형</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">사람과 관련된 뛰어난 통찰력을 가진 사람들</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">묘한 능력이 있는 캐릭터, 조력자로 자주 등장</p>
        <carousel-3d v-show="checkMBTI === 'INFJ'">
          <slide :index="0">
            <img src="../../assets/INFJ/1.jpg" alt="">
          </slide>
          <slide :index="1">
            <img src="../../assets/INFJ/2.jpg" alt="">
          </slide>
          <slide :index="2">
            <img src="../../assets/INFJ/3.jpg" alt="">
          </slide>
          <slide :index="3">
            <img src="../../assets/INFJ/4.jpg" alt="">
          </slide>
          <slide :index="4">
            <img src="../../assets/INFJ/5.jpg" alt="">
          </slide>
          <slide :index="5">
            <img src="../../assets/INFJ/6.jpg" alt="">
          </slide>
          <slide :index="6">
            <img src="../../assets/INFJ/7.jpg" alt="">
          </slide>
          <slide :index="7">
            <img src="../../assets/INFJ/8.jpg" alt="">
          </slide>
          <slide :index="8">
            <img src="../../assets/INFJ/9.jpg" alt="">
          </slide>
          <slide :index="9">
            <img src="../../assets/INFJ/10.jpg" alt="">
          </slide>
          <slide :index="10">
            <img src="../../assets/INFJ/11.jpg" alt="">
          </slide>
          <slide :index="11">
            <img src="../../assets/INFJ/12.jpg" alt="">
          </slide>
          <slide :index="12">
            <img src="../../assets/INFJ/13.jpg" alt="">
          </slide>
          <slide :index="13">
            <img src="../../assets/INFJ/14.jpg" alt="">
          </slide>
          <slide :index="14">
            <img src="../../assets/INFJ/15.jpg" alt="">
          </slide>
          <slide :index="15">
            <img src="../../assets/INFJ/16.jpg" alt="">
          </slide>
          <slide :index="16">
            <img src="../../assets/INFJ/17.jpg" alt="">
          </slide>
          <slide :index="17">
            <img src="../../assets/INFJ/18.jpg" alt="">
          </slide>
          <slide :index="18">
            <img src="../../assets/INFJ/19.jpg" alt="">
          </slide>
        </carousel-3d>
      </div>

      <div v-show="checkMBTI === 'ENFJ'" style="color: rgb(254, 175, 82);">
        <p style="font-family: 'Black And White Picture', sans-serif; font-size:2rem;">정의로운 사회운동가 / 언변능숙형</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">타인의 성장을 도모하고 협동하는 사람들</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">명랑한 분위기를 가졌으나 조금 차분하고 목표지향적</p>
        <carousel-3d v-show="checkMBTI === 'ENFJ'">
          <slide :index="0">
            <img src="../../assets/ENFJ/1.jpg" alt="">
          </slide>
          <slide :index="1">
            <img src="../../assets/ENFJ/2.jpg" alt="">
          </slide>
          <slide :index="2">
            <img src="../../assets/ENFJ/3.jpg" alt="">
          </slide>
          <slide :index="3">
            <img src="../../assets/ENFJ/4.jpg" alt="">
          </slide>
          <slide :index="4">
            <img src="../../assets/ENFJ/5.jpg" alt="">
          </slide>
          <slide :index="5">
            <img src="../../assets/ENFJ/6.jpg" alt="">
          </slide>
          <slide :index="6">
            <img src="../../assets/ENFJ/7.jpg" alt="">
          </slide>
          <slide :index="7">
            <img src="../../assets/ENFJ/8.jpg" alt="">
          </slide>
          <slide :index="8">
            <img src="../../assets/ENFJ/9.jpg" alt="">
          </slide>
          <slide :index="9">
            <img src="../../assets/ENFJ/10.jpg" alt="">
          </slide>
          <slide :index="10">
            <img src="../../assets/ENFJ/11.jpg" alt="">
          </slide>
          <slide :index="11">
            <img src="../../assets/ENFJ/12.jpg" alt="">
          </slide>
          <slide :index="12">
            <img src="../../assets/ENFJ/13.jpg" alt="">
          </slide>
          <slide :index="13">
            <img src="../../assets/ENFJ/14.jpg" alt="">
          </slide>
        </carousel-3d>
      </div>

      <div v-show="checkMBTI === 'ISTJ'" style="color: rgb(42, 101, 45);">
        <p style="font-family: 'Black And White Picture', sans-serif; font-size:2rem;">청렴결백한 논리주의자 / 세상의 소금형</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">한번 시작한 일은 끝까지 해내는 사람</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">진지한 모범생형 캐릭터</p>
        <carousel-3d v-show="checkMBTI === 'ISTJ'">
          <slide :index="0">
            <img src="../../assets/ISTJ/1.jpg" alt="">
          </slide>
          <slide :index="1">
            <img src="../../assets/ISTJ/2.jpg" alt="">
          </slide>
          <slide :index="2">
            <img src="../../assets/ISTJ/3.jpg" alt="">
          </slide>
          <slide :index="3">
            <img src="../../assets/ISTJ/4.jpg" alt="">
          </slide>
          <slide :index="4">
            <img src="../../assets/ISTJ/5.jpg" alt="">
          </slide>
          <slide :index="5">
            <img src="../../assets/ISTJ/6.jpg" alt="">
          </slide>
          <slide :index="6">
            <img src="../../assets/ISTJ/7.jpg" alt="">
          </slide>
          <slide :index="7">
            <img src="../../assets/ISTJ/8.jpg" alt="">
          </slide>
          <slide :index="8">
            <img src="../../assets/ISTJ/9.jpg" alt="">
          </slide>
          <slide :index="9">
            <img src="../../assets/ISTJ/10.jpg" alt="">
          </slide>
          <slide :index="10">
            <img src="../../assets/ISTJ/11.jpg" alt="">
          </slide>
          <slide :index="11">
            <img src="../../assets/ISTJ/12.jpg" alt="">
          </slide>
          <slide :index="12">
            <img src="../../assets/ISTJ/13.jpg" alt="">
          </slide>
          <slide :index="13">
            <img src="../../assets/ISTJ/14.jpg" alt="">
          </slide>
          <slide :index="14">
            <img src="../../assets/ISTJ/15.jpg" alt="">
          </slide>
          <slide :index="15">
            <img src="../../assets/ISTJ/16.jpg" alt="">
          </slide>
          <slide :index="16">
            <img src="../../assets/ISTJ/17.jpg" alt="">
          </slide>
          <slide :index="17">
            <img src="../../assets/ISTJ/18.jpg" alt="">
          </slide>
        </carousel-3d>
      </div>
      
      <div v-show="checkMBTI === 'ISFJ'" style="color: rgb(107, 222, 65);">
        <p style="font-family: 'Black And White Picture', sans-serif; font-size:2rem;">용감한 수호자 / 임금 뒷편의 권력형</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">성실하고 온화하며 협조를 잘하는 사람들</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">정직하게 착한 캐릭터들이 많음</p>
        <carousel-3d v-show="checkMBTI === 'ISFJ'">
          <slide :index="0">
            <img src="../../assets/ISFJ/1.jpg" alt="">
          </slide>
          <slide :index="1">
            <img src="../../assets/ISFJ/2.jpg" alt="">
          </slide>
          <slide :index="2">
            <img src="../../assets/ISFJ/3.jpg" alt="">
          </slide>
          <slide :index="3">
            <img src="../../assets/ISFJ/4.jpg" alt="">
          </slide>
          <slide :index="4">
            <img src="../../assets/ISFJ/5.jpg" alt="">
          </slide>
          <slide :index="5">
            <img src="../../assets/ISFJ/6.jpg" alt="">
          </slide>
          <slide :index="6">
            <img src="../../assets/ISFJ/7.jpg" alt="">
          </slide>
          <slide :index="7">
            <img src="../../assets/ISFJ/8.jpg" alt="">
          </slide>
          <slide :index="8">
            <img src="../../assets/ISFJ/9.jpg" alt="">
          </slide>
          <slide :index="9">
            <img src="../../assets/ISFJ/10.jpg" alt="">
          </slide>
          <slide :index="10">
            <img src="../../assets/ISFJ/11.jpg" alt="">
          </slide>
          <slide :index="11">
            <img src="../../assets/ISFJ/12.jpg" alt="">
          </slide>
          <slide :index="12">
            <img src="../../assets/ISFJ/13.jpg" alt="">
          </slide>
          <slide :index="13">
            <img src="../../assets/ISFJ/14.jpg" alt="">
          </slide>
          <slide :index="14">
            <img src="../../assets/ISFJ/15.jpg" alt="">
          </slide>
          <slide :index="15">
            <img src="../../assets/ISFJ/16.jpg" alt="">
          </slide>
          <slide :index="16">
            <img src="../../assets/ISFJ/17.jpg" alt="">
          </slide>
          <slide :index="17">
            <img src="../../assets/ISFJ/18.jpg" alt="">
          </slide>
        </carousel-3d>
      </div>

      <div v-show="checkMBTI === 'ESTJ'" style="color: rgb(48, 72, 48);">
        <p style="font-family: 'Black And White Picture', sans-serif; font-size:2rem;">엄격한 관리자 / 사업가형</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">사무적, 실용적, 현실도모적인 일을 많이 하는 사람</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">보통 엄청난 능력자</p>
        <carousel-3d v-show="checkMBTI === 'ESTJ'">
          <slide :index="0">
            <img src="../../assets/ESTJ/1.jpg" alt="">
          </slide>
          <slide :index="1">
            <img src="../../assets/ESTJ/2.jpg" alt="">
          </slide>
          <slide :index="2">
            <img src="../../assets/ESTJ/3.jpg" alt="">
          </slide>
          <slide :index="3">
            <img src="../../assets/ESTJ/4.jpg" alt="">
          </slide>
          <slide :index="4">
            <img src="../../assets/ESTJ/5.jpg" alt="">
          </slide>
          <slide :index="5">
            <img src="../../assets/ESTJ/6.jpg" alt="">
          </slide>
          <slide :index="6">
            <img src="../../assets/ESTJ/7.jpg" alt="">
          </slide>
          <slide :index="7">
            <img src="../../assets/ESTJ/8.jpg" alt="">
          </slide>
          <slide :index="8">
            <img src="../../assets/ESTJ/9.jpg" alt="">
          </slide>
          <slide :index="9">
            <img src="../../assets/ESTJ/10.jpg" alt="">
          </slide>
          <slide :index="10">
            <img src="../../assets/ESTJ/11.jpg" alt="">
          </slide>
          <slide :index="11">
            <img src="../../assets/ESTJ/12.jpg" alt="">
          </slide>
          <slide :index="12">
            <img src="../../assets/ESTJ/13.jpg" alt="">
          </slide>
          <slide :index="13">
            <img src="../../assets/ESTJ/14.jpg" alt="">
          </slide>
          <slide :index="14">
            <img src="../../assets/ESTJ/15.jpg" alt="">
          </slide>
          <slide :index="15">
            <img src="../../assets/ESTJ/16.jpg" alt="">
          </slide>
          <slide :index="16">
            <img src="../../assets/ESTJ/17.jpg" alt="">
          </slide>
        </carousel-3d>
      </div>

      <div v-show="checkMBTI === 'ESFJ'" style="color: rgb(84, 152, 49);">
        <p style="font-family: 'Black And White Picture', sans-serif; font-size:2rem;">사교적인 외교관 / 친선도모형</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">친절과 현실감을 바탕으로 타인에게 봉사하는 사람들</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">능력치 골고루 발달한 전교회장 느낌</p>
        <carousel-3d v-show="checkMBTI === 'ESFJ'">
          <slide :index="0">
            <img src="../../assets/ESFJ/1.jpg" alt="">
          </slide>
          <slide :index="1">
            <img src="../../assets/ESFJ/2.jpg" alt="">
          </slide>
          <slide :index="2">
            <img src="../../assets/ESFJ/3.jpg" alt="">
          </slide>
          <slide :index="3">
            <img src="../../assets/ESFJ/4.jpg" alt="">
          </slide>
          <slide :index="4">
            <img src="../../assets/ESFJ/5.jpg" alt="">
          </slide>
          <slide :index="5">
            <img src="../../assets/ESFJ/6.jpg" alt="">
          </slide>
          <slide :index="6">
            <img src="../../assets/ESFJ/7.jpg" alt="">
          </slide>
          <slide :index="7">
            <img src="../../assets/ESFJ/8.jpg" alt="">
          </slide>
          <slide :index="8">
            <img src="../../assets/ESFJ/9.jpg" alt="">
          </slide>
          <slide :index="9">
            <img src="../../assets/ESFJ/10.jpg" alt="">
          </slide>
          <slide :index="10">
            <img src="../../assets/ESFJ/11.jpg" alt="">
          </slide>
          <slide :index="11">
            <img src="../../assets/ESFJ/12.jpg" alt="">
          </slide>
          <slide :index="12">
            <img src="../../assets/ESFJ/13.jpg" alt="">
          </slide>
          <slide :index="13">
            <img src="../../assets/ESFJ/14.jpg" alt="">
          </slide>
          <slide :index="14">
            <img src="../../assets/ESFJ/15.jpg" alt="">
          </slide>
        </carousel-3d>
      </div>

      <div v-show="checkMBTI === 'ISTP'" style="color: rgb(48, 84, 243);">
        <p style="font-family: 'Black And White Picture', sans-serif; font-size:2rem;">만능 재주꾼 / 백과사전형</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">논리적이고 뛰어난 적응력을 가진 사람들</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">액션영화 주인공이 엄청 과묵하고 엄청 멋있음</p>
        <carousel-3d v-show="checkMBTI === 'ISTP'">
          <slide :index="0">
            <img src="../../assets/ISTP/1.jpg" alt="">
          </slide>
          <slide :index="1">
            <img src="../../assets/ISTP/2.jpeg" alt="">
          </slide>
          <slide :index="2">
            <img src="../../assets/ISTP/3.jpg" alt="">
          </slide>
          <slide :index="3">
            <img src="../../assets/ISTP/4.jpg" alt="">
          </slide>
          <slide :index="4">
            <img src="../../assets/ISTP/5.jpg" alt="">
          </slide>
          <slide :index="5">
            <img src="../../assets/ISTP/6.jpg" alt="">
          </slide>
          <slide :index="6">
            <img src="../../assets/ISTP/7.jpg" alt="">
          </slide>
          <slide :index="7">
            <img src="../../assets/ISTP/8.jpg" alt="">
          </slide>
          <slide :index="8">
            <img src="../../assets/ISTP/9.jpg" alt="">
          </slide>
          <slide :index="9">
            <img src="../../assets/ISTP/10.jpg" alt="">
          </slide>
          <slide :index="10">
            <img src="../../assets/ISTP/11.jpg" alt="">
          </slide>
          <slide :index="11">
            <img src="../../assets/ISTP/12.jpg" alt="">
          </slide>
          <slide :index="12">
            <img src="../../assets/ISTP/13.jpg" alt="">
          </slide>
          <slide :index="13">
            <img src="../../assets/ISTP/14.jpg" alt="">
          </slide>
          <slide :index="14">
            <img src="../../assets/ISTP/15.jpg" alt="">
          </slide>
          <slide :index="15">
            <img src="../../assets/ISTP/16.jpg" alt="">
          </slide>
          <slide :index="16">
            <img src="../../assets/ISTP/17.jpg" alt="">
          </slide>
          <slide :index="17">
            <img src="../../assets/ISTP/18.jpg" alt="">
          </slide>
          <slide :index="18">
            <img src="../../assets/ISTP/19.jpg" alt="">
          </slide>
        </carousel-3d>
      </div>

      <div v-show="checkMBTI === 'ESTP'" style="color: rgb(0, 53, 247);">
        <p style="font-family: 'Black And White Picture', sans-serif; font-size:2rem;">모험을 즐기는 사업가 / 수완 좋은 활동가형</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">친구, 운동, 음식 등 다양한 활동을 선호하는 사람들</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">매력적인 캐릭터들</p>
        <carousel-3d v-show="checkMBTI === 'ESTP'">
          <slide :index="0">
            <img src="../../assets/ESTP/1.jpg" alt="">
          </slide>
          <slide :index="1">
            <img src="../../assets/ESTP/2.jpg" alt="">
          </slide>
          <slide :index="2">
            <img src="../../assets/ESTP/3.jpg" alt="">
          </slide>
          <slide :index="3">
            <img src="../../assets/ESTP/4.jpg" alt="">
          </slide>
          <slide :index="4">
            <img src="../../assets/ESTP/5.jpg" alt="">
          </slide>
          <slide :index="5">
            <img src="../../assets/ESTP/6.jpg" alt="">
          </slide>
          <slide :index="6">
            <img src="../../assets/ESTP/7.jpg" alt="">
          </slide>
          <slide :index="7">
            <img src="../../assets/ESTP/8.jpg" alt="">
          </slide>
          <slide :index="8">
            <img src="../../assets/ESTP/9.jpg" alt="">
          </slide>
          <slide :index="9">
            <img src="../../assets/ESTP/10.jpg" alt="">
          </slide>
          <slide :index="10">
            <img src="../../assets/ESTP/11.jpg" alt="">
          </slide>
          <slide :index="11">
            <img src="../../assets/ESTP/12.jpg" alt="">
          </slide>
          <slide :index="12">
            <img src="../../assets/ESTP/13.jpg" alt="">
          </slide>
          <slide :index="13">
            <img src="../../assets/ESTP/14.jpg" alt="">
          </slide>
          <slide :index="14">
            <img src="../../assets/ESTP/15.jpg" alt="">
          </slide>
          <slide :index="15">
            <img src="../../assets/ESTP/16.jpg" alt="">
          </slide>
          <slide :index="16">
            <img src="../../assets/ESTP/17.jpg" alt="">
          </slide>
          <slide :index="17">
            <img src="../../assets/ESTP/18.jpg" alt="">
          </slide>
          <slide :index="18">
            <img src="../../assets/ESTP/19.jpg" alt="">
          </slide>
          <slide :index="19">
            <img src="../../assets/ESTP/20.jpg" alt="">
          </slide>
          <slide :index="20">
            <img src="../../assets/ESTP/21.jpg" alt="">
          </slide>
        </carousel-3d>
      </div>

      <div v-show="checkMBTI === 'ISFP'" style="color: rgb(189, 194, 250);">
        <p style="font-family: 'Black And White Picture', sans-serif; font-size:2rem;">호기심 많은 예술가 / 성인군자형</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">따뜻한 감성을 가지고 있는 겸손한 사람들</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">성장물의 주인공으로 쓰기에 가장 적합한 유형</p>
        <carousel-3d v-show="checkMBTI === 'ISFP'">
          <slide :index="0">
            <img src="../../assets/ISFP/1.jpg" alt="">
          </slide>
          <slide :index="1">
            <img src="../../assets/ISFP/2.jpg" alt="">
          </slide>
          <slide :index="2">
            <img src="../../assets/ISFP/3.jpg" alt="">
          </slide>
          <slide :index="3">
            <img src="../../assets/ISFP/4.jpg" alt="">
          </slide>
          <slide :index="4">
            <img src="../../assets/ISFP/5.jpg" alt="">
          </slide>
          <slide :index="5">
            <img src="../../assets/ISFP/6.jpg" alt="">
          </slide>
          <slide :index="6">
            <img src="../../assets/ISFP/7.jpg" alt="">
          </slide>
          <slide :index="7">
            <img src="../../assets/ISFP/8.jpg" alt="">
          </slide>
          <slide :index="8">
            <img src="../../assets/ISFP/9.jpg" alt="">
          </slide>
          <slide :index="9">
            <img src="../../assets/ISFP/10.jpg" alt="">
          </slide>
          <slide :index="10">
            <img src="../../assets/ISFP/11.jpg" alt="">
          </slide>
          <slide :index="11">
            <img src="../../assets/ISFP/12.jpg" alt="">
          </slide>
          <slide :index="12">
            <img src="../../assets/ISFP/13.jpg" alt="">
          </slide>
          <slide :index="13">
            <img src="../../assets/ISFP/14.jpg" alt="">
          </slide>
          <slide :index="14">
            <img src="../../assets/ISFP/15.jpg" alt="">
          </slide>
          <slide :index="15">
            <img src="../../assets/ISFP/16.jpg" alt="">
          </slide>
        </carousel-3d>
      </div>

      <div v-show="checkMBTI === 'ESFP'" style="color: rgb(123, 134, 249);">
        <p style="font-family: 'Black And White Picture', sans-serif; font-size:2rem;">자유로운 영혼의 연예인 / 사교적인 유형</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">분위기를 고조시키는 우호적인 사람들</p>
        <p style="font-family: 'East Sea Dokdo', cursive; font-size:1.7rem;">에너지 넘치는 캐릭터들</p>
        <carousel-3d v-show="checkMBTI === 'ESFP'">
          <slide :index="0">
            <img src="../../assets/ESFP/1.jpg" alt="">
          </slide>
          <slide :index="1">
            <img src="../../assets/ESFP/2.jpg" alt="">
          </slide>
          <slide :index="2">
            <img src="../../assets/ESFP/3.jpg" alt="">
          </slide>
          <slide :index="3">
            <img src="../../assets/ESFP/4.jpg" alt="">
          </slide>
          <slide :index="4">
            <img src="../../assets/ESFP/5.jpg" alt="">
          </slide>
          <slide :index="5">
            <img src="../../assets/ESFP/6.jpg" alt="">
          </slide>
          <slide :index="6">
            <img src="../../assets/ESFP/7.jpg" alt="">
          </slide>
          <slide :index="7">
            <img src="../../assets/ESFP/8.jpg" alt="">
          </slide>
          <slide :index="8">
            <img src="../../assets/ESFP/9.jpg" alt="">
          </slide>
          <slide :index="9">
            <img src="../../assets/ESFP/10.jpg" alt="">
          </slide>
          <slide :index="10">
            <img src="../../assets/ESFP/11.jpg" alt="">
          </slide>
          <slide :index="11">
            <img src="../../assets/ESFP/12.jpg" alt="">
          </slide>
          <slide :index="12">
            <img src="../../assets/ESFP/13.jpg" alt="">
          </slide>
          <slide :index="13">
            <img src="../../assets/ESFP/14.jpg" alt="">
          </slide>
          <slide :index="14">
            <img src="../../assets/ESFP/15.jpg" alt="">
          </slide>
          <slide :index="15">
            <img src="../../assets/ESFP/16.jpg" alt="">
          </slide>
          <slide :index="16">
            <img src="../../assets/ESFP/17.jpg" alt="">
          </slide>
          <slide :index="17">
            <img src="../../assets/ESFP/18.jpg" alt="">
          </slide>
          <slide :index="18">
            <img src="../../assets/ESFP/19.jpg" alt="">
          </slide>
        </carousel-3d>
      </div>

    </div>
    <MovieCard v-for="(movie, index) in showMovies"
    :key="index"
    :movie="movie" />
  </div>
</template>

<script>
import axios from 'axios'
import MovieCard from './MovieCard.vue'
import MBTI from './MBTI.vue'
import { Carousel3d, Slide } from 'vue-carousel-3d';

export default {
  name: 'Movies',
  components: {
    MovieCard,
    MBTI,
    Carousel3d,
    Slide,
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

  #image-slide {
    width: 100vw;
    margin: 2rem;
  }

  #image-slide img {
    width: 210px;
    height: 280px;
  }

  .carousel-3d-container {
    height: 280px !important;
  }

  .carousel-3d-slider {
    height: 280px !important;
    width: 210px !important;
  }

  .carousel-3d-slide {
    height: 280px !important;
    width: 210px !important;
    border: none !important;
    border-radius: 4px;
  }


</style>