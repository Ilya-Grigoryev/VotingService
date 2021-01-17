<template>
<div class="Settings">
    <v-card
    class="mx-auto pa-3 ma-3"
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
          <v-dialog v-model="dialog" persistent max-width="700px">
              <template v-slot:activator="{ on, attrs }">
                  <v-btn
                      color="teal"
                      class="white--text"
                      style="position: absolute; right: 80px;"
                      v-bind="attrs"
                      v-on="on">
                        Admin
                    <v-divider vertical></v-divider>
                      <v-icon>mdi-account-key</v-icon>
                    </v-btn>
              </template>
            <v-card class="mx-auto pa-3"
            elevation="4"
            outlined
            width="100%">
            <v-btn
                @click="$router.go(-1);"
                icon
                depressed
                color="teal"
                style="position: absolute; right: 20px;"
            >
              <v-icon>mdi-close-circle-outline</v-icon>
            </v-btn>
              <form class="mx-auto pa-3 ma-3">
                    <v-text-field
                      type="password"
                      v-model="admin_password"
                      :error-messages="admin_passwordErrors"
                      :counter="10"
                      label="Admin password"
                      required
                      @input="$v.admin_password.$touch()"
                      @blur="$v.admin_password.$touch()"
                    ></v-text-field>
                      <v-btn
                      class="mr-4"
                      @click="$router.push(`/admin`)"
                    >
                      Enter
                    </v-btn>
              </form>
      </v-card>
          </v-dialog>
            <form class="mx-auto pa-3 ma-3">
      <v-text-field
        type="password"
        v-model="password_1"
        :error-messages="password_1Errors"
        :counter="10"
        label="Old password"
        required
        @input="$v.password_1.$touch()"
        @blur="$v.password_1.$touch()"
      ></v-text-field>
      <v-text-field
         type="password"
         v-model="password_2"
         :error-messages="password_2Errors"
         :counter="10"
         label="New password"
         required
         @input="$v.password_2.$touch()"
         @blur="$v.password_2.$touch()"
      ></v-text-field>
      <v-checkbox
        v-model="checkbox"
        :error-messages="checkboxErrors"
        label="Do you agree?"
        required
        @change="$v.checkbox.$touch()"
        @blur="$v.checkbox.$touch()"
      ></v-checkbox>
      <v-btn
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
  props: ['user', 'id', 'admin'],
  validations: {
    password_1: {required},
    password_2: {required},
    admin_password: {required},
    checkbox: {
      checked (val) {
        return val
      }
      },
  },
  data: () => ({
    password_1: '',
    password_2: '',
    admin_password: '',
    dialog: false,
    checkbox: false,
  }),
  computed: {
    checkboxErrors() {
      const errors = []
      if (!this.$v.checkbox.$dirty) return errors
      !this.$v.checkbox.checked && errors.push('You must agree to continue!')
      this.password_1 === this.password_2 && errors.push('Passwords match')
      //this.password_1 !== this.user.password && errors.push('Old passwords don\'t match')
      !this.$v.password_1.required && !this.$v.password_2.required && errors.push('Passwords aren\'t entered')
      return errors
    },
    password_1Errors() {
      const errors = []
      if (!this.$v.password_1.$dirty) return errors
      !this.$v.password_1.required && errors.push('Password is required')
      return errors
    },
    password_2Errors() {
      const errors = []
      if (!this.$v.password_2.$dirty) return errors
      !this.$v.password_2.required && errors.push('Password is required')
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
    enter() { },
    submit() {
        this.$v.$touch()
                if (!this.$v.$invalid) {
                    this.axios.post(`http://localhost:8000/api/change_password/`,
                        {
                           old_password: this.password_1,
                           new_password: this.password_2
                        },
                        {
                        headers: { Authorization: `Token ${this.user.token}` }
                        }
                    ).then(response => {
                        if (response.data.status === 200) {
                            this.password = response.data.password_2,
                            this.user.password = response.data.password_2
                            this.$router.push('/')
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
