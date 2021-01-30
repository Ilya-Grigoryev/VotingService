<template>
  <div>
    <v-card class="mx-auto pa-3 ma-3"
            elevation="4"
            outlined
            width="65%"
            height="100%">
      <v-carousel>
      <v-carousel-item
        v-for="(item,i) in items"
        :key="i"
        :src="item.src"
        reverse-transition="fade-transition"
        transition="fade-transition"
      ></v-carousel-item>
    </v-carousel>
      <v-divider></v-divider>
      </v-card>
  </div>
</template>



<script>
  // @ is an alias to /src
  // import Poll from '../components/Poll.vue'

  export default {
    name: 'Home',
    props: ['user'],

    data: () => ({
      items: [
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg',
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg',
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg',
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg',
        },
      ],

    }),
    methods: {

    },
  }
</script>
