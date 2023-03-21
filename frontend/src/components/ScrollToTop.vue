<template>
    <div v-if="showButton" class="scroll-to-top" @click="scrollToTop">
      <i class="fa fa-chevron-up"></i>
    </div>
</template>
  
  <script>
  export default {
    data() {
      return {
        showButton: false
      };
    },
    methods: {
      scrollToTop() {
        window.scrollTo({ top: 0, behavior: "smooth" });
      },
      handleScroll() {
        this.showButton = window.pageYOffset > 100;
      }
    },
    mounted() {
      window.addEventListener("scroll", this.handleScroll);
    },
    beforeDestroy() {
      window.removeEventListener("scroll", this.handleScroll);
    }
  };
  </script>
  
  <style>
  .scroll-to-top {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #6e9190;
    color: #c5dad2;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
  }
  
  .scroll-to-top:hover {
    background-color: #444;
  }
  </style>
  