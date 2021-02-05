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
      <v-carousel hide-delimiters height="auto" width="auto">
        <v-carousel-item
          v-for="(item,i) in items"
          :key="i"
          :src="item"
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

    data() {
      return {
        items: [
          'https://i.ibb.co/TT6V5fj/Slide1.jpg',
          'https://i.ibb.co/G3pTK75/Slide2.jpg',
          'https://i.ibb.co/K9hG5GK/Slide3.jpg',
          'https://i.ibb.co/6w9Q3qV/Slide4.jpg',
          'https://i.ibb.co/w0fKCjx/Slide5.jpg',
          'https://i.ibb.co/mXmZ6wc/Slide6.jpg',
          'https://i.ibb.co/60GLssd/Slide7.jpg',
          'https://i.ibb.co/6X5hbWP/Slide8.jpg',
          'https://i.ibb.co/1rTKMFt/Slide9.jpg',
          'https://i.ibb.co/ZGy8QXB/Slide10.jpg',
          'https://i.ibb.co/SQB0Wsc/Slide11.jpg',
          'https://i.ibb.co/cyCqRZz/Slide12.jpg',
          'https://i.ibb.co/9HnNZ6f/Slide13.jpg',
        ],
      }
    }
  }
</script>
