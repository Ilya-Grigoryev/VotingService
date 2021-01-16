<template>
<div class="Admin">
    <v-card class="mx-auto pa-3 ma-3"
            elevation="4"
            outlined
            width="65%">
      <v-btn
                @click="$router.go(-1);"
                icon
                depressed
                color="teal"
                style="position: absolute; right: 20px;"
                >
              <v-icon>mdi-close-circle-outline</v-icon>
            </v-btn>

      </v-card>
  <v-card
      class="mx-auto pa-3 ma-3"
            elevation="4"
            outlined
            width="65%">
  </v-card>
</div>
</template>

<script>

export default {
    name: "Admin",
    props: ['admin'],

}

</script>

<style scoped>

</style>