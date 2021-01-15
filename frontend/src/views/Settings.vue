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
          <v-btn
              @click="$router.push(`/admin`)"
              color="teal"
              class="white--text"
              style="position: absolute; right: 80px;">
                Admin
            <v-divider vertical></v-divider>
              <v-icon>mdi-account-key</v-icon>
            </v-btn>
            <form class="mx-auto pa-3 ma-3">
      <v-text-field
        type="password"
        v-model="password_1"
        :error-messages="password_1Errors"
        :counter="10"
        label="New password"
        required
        @input="$v.password_1.$touch()"
        @blur="$v.password_1.$touch()"
      ></v-text-field>
      <v-text-field
         type="password"
         v-model="password_2"
         :error-messages="password_2Errors"
         :counter="10"
         label="Repeat new password"
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
  props: ['user', 'id'],
  validations: {
    password_1: {required},
    password_2: {required},
    checkbox: {
      checked (val) {
        return val
      }
      },
  },
  data: () => ({
    password_1: '',
    password_2: '',
    checkbox: false,
  }),
  computed: {
    checkboxErrors() {
      const errors = []
      if (!this.$v.checkbox.$dirty) return errors
      !this.$v.checkbox.checked && errors.push('You must agree to continue!')
      this.password_1 !== this.password_2 && errors.push('Passwords don\'t match')
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
  },
  methods: {
    submit() {
      this.$v.$touch()
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
                            this.password = response.data.password_1,
                            this.user.password = response.data.password_1
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