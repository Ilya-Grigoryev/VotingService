<template>
    <div>
        <v-card class="mx-auto pa-3"
                    elevation="6"
                    outlined
                    width="50%">
            <v-text-field
              v-model="first_name"
              :error-messages="first_nameErrors"
              label="First name"
              required clearable
              @input="$v.first_name.$touch()"
              @blur="$v.first_name.$touch()"
            ></v-text-field>
            <v-text-field
              v-model="last_name"
              :error-messages="last_nameErrors"
              label="Last name"
              required clearable
              @input="$v.last_name.$touch()"
              @blur="$v.last_name.$touch()"
            ></v-text-field>
            <v-text-field
              @keydown.space="(event) => event.preventDefault()"
              v-model="username"
              :error-messages="usernameErrors"
              label="Username"
              :counter="20"
              required clearable
              @input="$v.username.$touch()"
              @blur="$v.username.$touch()"
            ></v-text-field>
            <v-text-field
              v-model="email"
              :error-messages="emailErrors"
              label="E-mail"
              required clearable
              @input="$v.email.$touch()"
              @blur="$v.email.$touch()"
            ></v-text-field>
            <v-text-field
                type="password"
                v-model="password"
                :error-messages="passwordErrors"
                label="Password"
                required clearable
                @input="$v.password.$touch()"
                @blur="$v.password.$touch()"
            ></v-text-field>
            <v-text-field
                type="password"
                v-model="repeatPassword"
                :error-messages="repeatPasswordErrors"
                label="Repeat password"
                required clearable
                @input="$v.repeatPassword.$touch()"
                @blur="$v.repeatPassword.$touch()"
            ></v-text-field>
            <v-text-field
              v-model="avatar"
              :error-messages="avatarErrors"
              label="Photo"
              required clearable
              @input="$v.avatar.$touch()"
              @blur="$v.avatar.$touch()"
            ></v-text-field>
            <v-btn
                class="mr-4"
                @click="register"
                width="25%">
              register
            </v-btn>
            <br>
            <ins style="color: gray; cursor: pointer;"
                 @click="$router.push('/login')">
                Have an account? Login now!
            </ins>
        </v-card>
    </div>
</template>

<script>
  import { validationMixin } from 'vuelidate'
  import { required, maxLength, email } from 'vuelidate/lib/validators'

  export default {
    mixins: [validationMixin],

    validations: {
        first_name: { required },
        last_name: { required },
        username: { required, maxLength: maxLength(20) },
        email: { required, email },
        password: { required },
        repeatPassword: {  },
    },

    data: () => ({
        first_name: '',
        last_name: '',
        username: '',
        email: '',
        password: '',
        repeatPassword: '',
    }),

    computed: {
      first_nameErrors() {
        const errors = []
        if (!this.$v.first_name.$dirty) return errors
        !this.$v.first_name.required && errors.push('First name is required.')
        return errors
      },
      last_nameErrors() {
        const errors = []
        if (!this.$v.last_name.$dirty) return errors
        !this.$v.last_name.required && errors.push('Last name is required.')
        return errors
      },
      usernameErrors() {
        const errors = []
        if (!this.$v.username.$dirty) return errors
        !this.$v.username.maxLength && errors.push('Username must be at most 20 characters long.')
        !this.$v.username.required && errors.push('Username is required.')
        return errors
      },
      emailErrors() {
        const errors = []
        if (!this.$v.email.$dirty) return errors
        !this.$v.email.email && errors.push('Must be valid e-mail.')
        !this.$v.email.required && errors.push('E-mail is required.')
        return errors
      },
      passwordErrors() {
        const errors = []
        if (!this.$v.password.$dirty) return errors
        !this.$v.password.required && errors.push('Password is required')
        return errors
      },
      repeatPasswordErrors() {
        const errors = []
        if (this.password === this.repeatPassword) return errors;
        errors.push('Passwords do not match.')
        return errors
      },

      methods: {
        register() {
          this.$v.$touch()
          if (!this.$v.$invalid && this.password === this.repeatPassword) {
            this.axios.post('http://localhost:8000/api/register/', {
              first_name: this.first_name,
              last_name: this.last_name,
              username: this.username,
              email: this.email,
              password: this.password,
            }).then(response => {
              console.log(response.data)
              if (response.data.status === 200) {
                this.$emit('login', {
                  token: response.data.token,
                  id: response.data.id,
                  email: response.data.email,
                  username: response.data.username,
                  first_name: response.data.first_name,
                  last_name: response.data.last_name,
                });
                this.$router.push('/login');
              } else {
                window.alert(response.data.description)
              }
            })
          }
        },
        clear() {
          this.$v.$reset()
          this.first_name = ''
          this.last_name = ''
          this.username = ''
          this.email = ''
        },
      },
    }
  }
</script>

<style scoped>

</style>