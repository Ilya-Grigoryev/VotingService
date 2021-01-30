<template>
  <div class="reports">
      <v-btn width="65%"
             color="teal"
             elevation="10"
             @click="$router.push('/new-report')">
        add new report
      </v-btn>
        <v-card class="mx-auto ma-3"
            elevation="4"
            outlined
            width="65%">
      <v-toolbar
        flat
        color="teal"
        dark
      >
        <v-icon>mdi-alert-octagon</v-icon>
        <v-toolbar-title class="font-weight-light">
          Reports
        </v-toolbar-title>
<!--        <v-spacer></v-spacer>-->
        <v-autocomplete
        v-model="select"
        :loading="loading"
        :items="items"
        :search-input.sync="search"
        cache-items
        class="mx-4"
        flat
        hide-no-data
        hide-details
        label="Search in your reports"
        solo-inverted
      ></v-autocomplete>
        <v-btn
          dark
          icon
          style="right:10px;"
          @click="search"
        >
          <v-icon >
             mdi-magnify
          </v-icon>
        </v-btn>
      </v-toolbar>
      <Report v-bind="report" :user="user"/>

    </v-card>
  </div>
</template>

<script>
import Report from '../components/Report.vue'
import {maxLength, required} from "vuelidate/lib/validators";

export default {
  name: "MyReports",
  props: ['user', 'id', 'admin'],
  components: {
    Report
  },
  validations: {
          title: {required, maxLength: maxLength(50)},
          subtitle: {required},
          $each: {
            option: {required, maxLength: maxLength(50)}
          },
          options: {
            required,
            $each: {required}
          }
        },
      data: () => ({
        report: null,
        loading: false,
        items: [],
        search: null,
        select: null,
      }),
  methods:{

  },
}
</script>

<style scoped>

</style>