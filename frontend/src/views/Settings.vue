<template>
<div class="Settings">
    <v-card
    class="mx-auto pa-3 ma-3"
            elevation="4"
            outlined
            width="65%">
             <v-btn
                 color="teal"
                 class="white--text"
                 :disabled="!user.is_admin"
                 style="position: absolute; right: 10px;"
                 @click="$router.push('/admin')"
             >
               Admin
               <v-divider vertical></v-divider>
               <v-icon>mdi-account-key</v-icon>
             </v-btn>
       <span class="headline">Password change</span>
            <form class="mx-auto pa-3 ma-3">
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
  },
  data: () => ({
    backupCode: '',
    new_password: '',
    dialog: false,
    loading: false,
    message: '',
  }),
  computed: {
    backupCodeErrors() {
      const errors = []
      if (!this.$v.backupCode.$dirty) return errors
      !this.$v.backupCode.required && errors.push('Backup code is required')
      return errors
    },
    new_passwordErrors() {
      const errors = []
      if (!this.$v.new_password.$dirty) return errors
      !this.$v.new_password.required && errors.push('Password is required')
      return errors
    },
  },
  methods: {
      send_code() {
          this.loading = true
          this.axios.post(
              `http://localhost:8000/api/generate_code/${this.user.id}/`
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
