<template>
  <div class="reports">
      <v-btn width="65%"
             color="teal"
             elevation="10"
             @click="$router.push('/new-report')">
        add new report
      </v-btn>
    <v-card
            v-for="(report, index) in reports" :key="index"
            class="mx-auto pa-3 ma-3"
            elevation="4"
            outlined
            width="65%">
      <v-btn icon depressed color="teal" style="position: absolute; right: 10px;">
        <v-icon @click="$router.push(`/report/${report.id}/`)">mdi-arrow-expand-all</v-icon>
      </v-btn>
      <Report v-bind="report" :user="user"/>
    </v-card>
  </div>
</template>

<script>
import Report from '../components/Report.vue'

export default {
  name: "MyReports",
  props: ['user', 'id', 'admin'],
  components: {
    Report
  },
  data: () => ({
    reports: [],
  }),
}
</script>

<style scoped>

</style>