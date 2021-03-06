<template>
  <div class="reports">
      <v-dialog
        v-model="dialog"
        max-width="50%">
          <template v-slot:activator="{ on, attrs }">
              <v-btn v-if="!user.is_admin"
                     width="65%"
                     color="teal"
                     elevation="10"
                     v-bind="attrs"
                     v-on="on">
                add new report
              </v-btn>
          </template>
        <v-card>
            <v-card-title>
                <v-btn icon outlined color="red" style="position: absolute; right: 10px;"
                    @click="dialog=false">
                    <v-icon color="red">
                        mdi-close
                    </v-icon>
                </v-btn>
              <span class="headline">New report</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-text-field
                    v-model="title"
                    :error-messages="titleErrors"
                    label="Title"
                    required clearable
                    :counter="50"
                    @input="$v.title.$touch()"
                    @blur="$v.title.$touch()"
                ></v-text-field>
                  <br>
                <v-textarea
                  v-model="description"
                  :error-messages="descriptionErrors"
                  @input="$v.description.$touch()"
                  @blur="$v.description.$touch()"
                  label="Description"
                  auto-grow
                  outlined
                  rows="10"
                ></v-textarea>
                  <br>
                <v-file-input accept="image/*"
                    label="Select image"
                    prepend-icon="mdi-camera"
                    outlined
                    dense
                    v-model="file"
                    @change="addFiles">
                </v-file-input>
                <v-img max-height="300"
                   contain
                   v-if="file"
                   :ref="'file'"
                   title="photo">
                </v-img>
              </v-container>
              <v-btn
                color="purple"
                outlined
                @click="add_report">
                Add report
              </v-btn>
            </v-card-text>
        </v-card>
      </v-dialog>

      <div v-if="!user.is_admin"><br><br></div>
      <v-card width="65%" elevation="0"
          class="mx-auto ma-3"
          v-if="user.is_admin">
        <v-row justify="space-between"><v-col md="auto">
          <h1>Users` problems:</h1>
        </v-col></v-row>
      </v-card>
      <Report v-for="(report, i) in reports.opened" :key="i" :report="report" :user="user"/>
      <br>
      <Report v-for="(report, i) in reports.closed" :key="i" :report="report" :user="user"/>

  </div>
</template>

<script>
import Report from '../components/Report.vue'
import {required, maxLength} from 'vuelidate/lib/validators'

export default {
  name: "MyReports",
  props: ['user'],
  components: {
    Report
  },
  data: () => ({
      reports: {
          opened: [],
          closed: [],
      },
      dialog: false,
      description: '',
      title: '',
      file: null,
      reader: null,
  }),
  validations: {
      title: { required, maxLength: maxLength(50) },
      description: { required },
  },
  methods: {
      addFiles(){
          this.reader = new FileReader();
          this.reader.onloadend = () => {
              let fileData = this.reader.result
              let imgRef = this.$refs.file
              imgRef.src = fileData
          }
          this.reader.readAsDataURL(this.file);
      },
      getReportsList() {
          this.axios.get('http://localhost:8000/api/reports/',
              {
                  headers: { Authorization: `Token ${this.user.token}` }
              })
          .then(response => {
              let all_reports = response.data.reverse()
              this.reports = {
                  opened: [],
                  closed: [],
              }
              for (let report of all_reports) {
                  if (report.status === 'open')
                      this.reports.opened.push(report)
                  else
                      this.reports.closed.push(report)
              }
          })
      },
      add_report() {
          this.$v.$touch()
          if (this.$v.$invalid) return
          let formData = new FormData();
          formData.append('file', this.file)
          formData.append('title', this.title)
          formData.append('description', this.description)
          this.axios.post('http://localhost:8000/api/reports/',
              formData,{
                  headers: { Authorization: `Token ${this.user.token}` }
              })
          .then(response => {
              this.reports.opened.unshift(response.data)
              this.dialog = false
              this.title = ''
              this.description = ''
              this.file = null
          })
      },
  },
  computed: {
      titleErrors() {
          const errors = []
          if (!this.$v.title.$dirty) return errors
          !this.$v.title.required && errors.push('Title is required.')
          !this.$v.title.maxLength && errors.push('Title must be at most 50 characters long.')
          return errors
      },
      descriptionErrors() {
          const errors = []
          if (!this.$v.description.$dirty) return errors
          !this.$v.description.required && errors.push('Description is required.')
          return errors
      },
  },
  mounted() {
      this.getReportsList()
  }
}
</script>

<style scoped>

</style>