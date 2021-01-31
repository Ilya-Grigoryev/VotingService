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
        v-model="old_password"
        :error-messages="old_passwordErrors"
        label="Old password"
        required
        @input="$v.old_password.$touch()"
        @blur="$v.old_password.$touch()"
      ></v-text-field>
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
          @click="submit()"
      >
        Save
      </v-btn>
    </form>
    </v-card>
</div>
</template>

<script>
import {required} from "vuelidate/lib/validators";

export default {
  name: "Settings",
  props: ['user'],
  validations: {
    old_password: {required},
    new_password: {required},
    admin_password: {required},
    checkbox: {
      checked (val) {
        return val
      }
      },
  },
  data: () => ({
    old_password: '',
    new_password: '',
    admin_password: '',
    dialog: false,
    checkbox: false,
  }),
  computed: {
    checkboxErrors() {
      const errors = []
      if (!this.$v.checkbox.$dirty) return errors
      !this.$v.checkbox.checked && errors.push('You must agree to continue!')
      this.old_password === this.new_password && errors.push('Passwords match')
      //this.old_password !== this.user.password && errors.push('Old passwords don\'t match')
      !this.$v.old_password.required && !this.$v.new_password.required && errors.push('Passwords aren\'t entered')
      return errors
    },
    old_passwordErrors() {
      const errors = []
      if (!this.$v.old_password.$dirty) return errors
      !this.$v.old_password.required && errors.push('Password is required')
      return errors
    },
    new_passwordErrors() {
      const errors = []
      if (!this.$v.new_password.$dirty) return errors
      !this.$v.new_password.required && errors.push('Password is required')
      return errors
    },
    admin_passwordErrors() {
      const errors = []
      if (!this.$v.admin_password.$dirty) return errors
      !this.$v.admin_password.required && errors.push('Password is required')
      //this.$v.admin_password !== this.admin.password && errors.push('You are not admin!')
      return errors
        },
  },
  methods: {
    submit() {
        this.$v.$touch()
                if (!this.$v.$invalid) {
                    this.axios.post(`http://localhost:8000/api/change_password/`,
                        {
                           old_password: this.old_password,
                           new_password: this.new_password
                        },
                        {
                        headers: { Authorization: `Token ${this.user.token}` }
                        }
                    ).then(response => {
                        if (response.data.status === 200) {
                            this.new_password = response.data.new_password,
                            this.user.password = response.data.new_password

                        }
                        else window.alert(response.data.description)
                    })
                }
    },
  },
}

</script>

<style scoped>

</style>
