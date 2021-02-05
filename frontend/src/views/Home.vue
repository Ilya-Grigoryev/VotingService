<template>
  <div>
    <v-card class="mx-auto pa-3 ma-3"
            elevation="4"
            outlined
            :width="user.id == null ? '90%' : '65%'"
            height="100%">
      <h1>
        Simple Voting Service
      </h1>
      <v-divider></v-divider>
      <br>
      <v-row justify="space-between">
        <v-col md="max">
          <h3 style="color: gray">Service for fast and convenient voting</h3>
        </v-col>
        <v-col md="auto" v-if="user.id == null">
          <v-btn @click="$router.push('/login')">
            Login
          </v-btn>
        </v-col>
        <v-col md="auto" v-if="user.id == null">
          <v-btn @click="$router.push('/register')">
            Register
          </v-btn>
        </v-col>
      </v-row>
      <v-carousel height="auto" width="auto">
        <v-carousel-item
          src="../assets/Slide1.jpg"
          reverse-transition="fade-transition"
          transition="fade-transition"
        ></v-carousel-item>
        <v-carousel-item
          src="../assets/Slide2.jpg"
          reverse-transition="fade-transition"
          transition="fade-transition"
        ></v-carousel-item>
        <v-carousel-item
          src="../assets/Slide3.jpg"
          reverse-transition="fade-transition"
          transition="fade-transition"
        ></v-carousel-item>
        <v-carousel-item
          src="../assets/Slide4.jpg"
          reverse-transition="fade-transition"
          transition="fade-transition"
        ></v-carousel-item>
        <v-carousel-item
          src="../assets/Slide5.jpg"
          reverse-transition="fade-transition"
          transition="fade-transition"
        ></v-carousel-item>
        <v-carousel-item
          src="../assets/Slide6.jpg"
          reverse-transition="fade-transition"
          transition="fade-transition"
        ></v-carousel-item>
        <v-carousel-item
          src="../assets/Slide7.jpg"
          reverse-transition="fade-transition"
          transition="fade-transition"
        ></v-carousel-item>
        <v-carousel-item
          src="../assets/Slide8.jpg"
          reverse-transition="fade-transition"
          transition="fade-transition"
        ></v-carousel-item>
        <v-carousel-item
          src="../assets/Slide9.jpg"
          reverse-transition="fade-transition"
          transition="fade-transition"
        ></v-carousel-item>
        <v-carousel-item
          src="../assets/Slide10.jpg"
          reverse-transition="fade-transition"
          transition="fade-transition"
        ></v-carousel-item>
        <v-carousel-item
          src="../assets/Slide11.jpg"
          reverse-transition="fade-transition"
          transition="fade-transition"
        ></v-carousel-item>
        <v-carousel-item
          src="../assets/Slide12.jpg"
          reverse-transition="fade-transition"
          transition="fade-transition"
        ></v-carousel-item>
        <v-carousel-item
          src="../assets/Slide13.jpg"
          reverse-transition="fade-transition"
          transition="fade-transition"
        ></v-carousel-item>
    </v-carousel>
      <v-divider></v-divider>
      </v-card>
  </div>
</template>



<script>
  export default {
    name: 'Home',
    props: ['user'],

    data: () => ({
      items: [],
    }),
    mounted() {
      for (let i = 1; i <= 13; i++) {
        this.items.push(`../assets/Slide${i}.jpg`)
        console.log(`../assets/Slide${i}.jpg`)
      }
    }
  }
</script>
