<!--<template>-->
<!--<div>-->
<!--    <v-card class="mx-auto pa-3 ma-3"-->
<!--            elevation="4"-->
<!--            outlined-->
<!--            width="65%">-->
<!--      <v-btn-->
<!--                @click="$router.go(-1);"-->
<!--                icon-->
<!--                depressed-->
<!--                color="teal"-->
<!--                style="position: absolute; right: 20px;"-->
<!--                >-->
<!--              <v-icon>mdi-close-circle-outline</v-icon>-->
<!--            </v-btn>-->
<!--      <form class="mx-auto pa-3 ma-3">-->
<!--      <v-text-field-->
<!--        type="password"-->
<!--        v-model="admin_password"-->
<!--        :error-messages="admin_passwordErrors"-->
<!--        :counter="10"-->
<!--        label="Admin password"-->
<!--        required-->
<!--        @input="$v.admin_password.$touch()"-->
<!--        @blur="$v.admin_password.$touch()"-->
<!--      ></v-text-field>-->
<!--        <v-btn-->
<!--        class="mr-4"-->
<!--          @click="enter()"-->
<!--      >-->
<!--        Enter-->
<!--      </v-btn>-->
<!--      </form>-->
<!--      </v-card>-->
<!--  <v-card v-if="admin_password === admin.password"-->
<!--      class="mx-auto pa-3 ma-3"-->
<!--            elevation="4"-->
<!--            outlined-->
<!--            width="65%">-->
<!--  </v-card>-->
<!--</div>-->
<!--</template>-->
<!--<script>-->
<!--import {required} from "vuelidate/lib/validators";-->
<!--export default {-->
<!--  name: "Admin",-->
<!--  props: ['admin'],-->
<!--  validations: {-->
<!--    admin_password: {required},-->
<!--  },-->
<!--  data: () => ({-->
<!--    admin_password: '',-->
<!--  }),-->
<!--  computed: {-->
<!--    admin_passwordErrors() {-->
<!--      const errors = []-->
<!--      if (!this.$v.admin_password.$dirty) return errors-->
<!--      !this.$v.admin_password.required && errors.push('Password is required')-->
<!--      return errors-->
<!--    },-->
<!--  },-->
<!--  methods: {-->
<!--    enter() {-->
<!--      this.$v.$touch()-->

<!--    },-->
<!--  },-->
<!--}-->

<!--</script>-->

<!--<style scoped>-->

<!--</style>-->