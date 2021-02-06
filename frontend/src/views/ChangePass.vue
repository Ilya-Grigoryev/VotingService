<template>
<div class="Settings" @keydown.enter="change_password()">
    <v-card
    class="mx-auto pa-3 ma-3"
            elevation="4"
            outlined
            width="65%">
        <v-btn @click="$router.go(-1);"
               color="teal"
               depressed
               dark
               style="position: absolute; left: 10px;">
          <v-icon>mdi-arrow-left-bold-outline</v-icon>
        </v-btn>
       <span class="headline">Password change</span>
            <form class="mx-auto pa-3 ma-3">
      <v-text-field
        type="text"
        v-model="username"
        :error-messages="usernameErrors"
        label="Username"
        required
        @input="check_username()"
        @blur="check_username()"
      ></v-text-field>
      <v-text-field
        type="password"
        v-model="backupCode"
        :error-messages="backupCodeErrors"
        label="Backup code"
        required
        @input="$v.backupCode.$touch()"
        @blur="$v.backupCode.$touch()"
      ></v-text-field>
                <v-btn x-small
                       @click="send_code"
                       :loading="loading"
                       :disabled="loading">
                    No code? Send by mail!
                </v-btn>
      <v-text-field
         type="password"
         v-model="new_password"
         :error-messages="new_passwordErrors"
         label="New password"
         required
         @input="$v.new_password.$touch()"
         @blur="$v.new_password.$touch()"
      ></v-text-field>
      <v-btn
          color="purple"
          outlined
          class="mr-4"
          @click="change_password()"
      >
        change password
      </v-btn>
    </form>
        {{ message }}
    </v-card>
</div>
</template>

<script>
import {required} from "vuelidate/lib/validators";

export default {
  name: "Settings",
  props: ['user'],
  validations: {
    backupCode: { required },
    new_password: { required },
    username: { required },
  },
  data: () => ({
    is_valid_username: false,
    user_id: null,
    username: '',
    backupCode: '',
    new_password: '',
    loading: false,
    message: '',
  }),
  computed: {
    backupCodeErrors() {
      const errors = []
      if (!this.$v.backupCode.$dirty) return errors
      !this.$v.backupCode.required && errors.push('Backup code is required.')
      return errors
    },
    new_passwordErrors() {
      const errors = []
      if (!this.$v.new_password.$dirty) return errors
      !this.$v.new_password.required && errors.push('Password is required.')
      return errors
    },
    usernameErrors() {
      const errors = []
      if (!this.$v.username.$dirty) return errors
      !this.$v.username.required && errors.push('Username is required.')
      !this.is_valid_username && errors.push('Invalid username.')
      return errors
    },
  },
  methods: {
      check_username() {
          this.$v.username.$touch()
          if (this.username === '') return
          this.axios.get(`http://localhost:8000/api/check_username/${this.username}/`)
          .then(response => {
              this.is_valid_username = response.data.username_status === 'free'
              this.user_id = this.is_valid_username ? response.data.user_id : ''
          })
      },
      send_code() {
          if (!this.is_valid_username) {
              this.$v.username.$touch()
              this.message = "Enter your username."
              return
          }
          this.loading = true
          this.axios.post(
              `http://localhost:8000/api/generate_code/${this.user_id}/`,
          ).then(response => {
              this.loading = false
              if (response.data.status !== 200)
                  window.alert(response.data.description)
          })
      },
      change_password() {
          if (!this.$v.$invalid) {
                this.axios.post(`http://localhost:8000/api/change_password/`,
                    {
                       backup_code: this.backupCode,
                       new_password: this.new_password
                    },
                ).then(response => {
                if (response.data.status === 200) {
                    this.new_password = ''
                    this.backupCode = ''
                    this.user.password = response.data.new_password
                    this.message = 'Password changed successfully!'
                    this.$v.$reset()
                }
                else {
                    this.backupCode = ''
                    this.$v.$touch()
                    this.message = response.data.description
                }
                })
          }
      }
  },
}

</script>

<style scoped>

</style>
