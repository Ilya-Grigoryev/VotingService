<template>
    <div>
        <v-card
        class="mx-auto pa-3 ma-3"
        elevation="4"
        outlined
        width="65%">
            <v-text-field
              v-model="title"
              :error-messages="titleErrors"
              label="Title"
              required clearable
              :counter="50"
              @input="$v.title.$touch()"
              @blur="$v.title.$touch()"
            ></v-text-field>

            <v-text-field
              v-model="description"
              :error-messages="descriptionErrors"
              label="Description"
              required clearable
              @input="$v.description.$touch()"
              @blur="$v.description.$touch()"
            ></v-text-field>

            <v-radio-group
              v-model="hours"
              row>
                <h3 class="mr-12">Duration:</h3>
              <v-radio
                label="1 hour"
                :value="1"
                selected
              ></v-radio>
              <v-radio
                label="3 hours"
                :value="3"
              ></v-radio>
              <v-radio
                label="6 hours"
                :value="6"
              ></v-radio>
              <v-radio
                label="1 day"
                :value="24"
              ></v-radio>
              <v-radio
                label="1 week"
                :value="24*7"
              ></v-radio>
            </v-radio-group>

            <br>
            <v-radio-group row>
                <h3 class="mr-7">Options:   {{ options.length }}</h3>
                <v-btn x-small @click="addOption">add option</v-btn>
            </v-radio-group>
            <v-list>
                <v-list-item v-for="(option, ind) of options" :key="ind">
                    <v-text-field
                        v-model="options[ind]"
                        :error-messages="option.replace(/^\s+|\s+$/g, '') === '' ? ['Option is required.'] : []"
                        @input="$v.options.$each[ind].$touch()"
                        @blur="$v.options.$each[ind].$touch()"
                        label="Option"
                        required clearable
                    ></v-text-field>
                    <v-btn icon large @click="removeOption(ind)">
                        <v-icon color="red">mdi-close-box</v-icon>
                    </v-btn>
                </v-list-item>
            </v-list>
            <v-btn @click="create_poll()">
                create new poll
            </v-btn>
        </v-card>
    </div>
</template>

<script>
    import { validationMixin } from 'vuelidate'
    import { required, maxLength } from 'vuelidate/lib/validators'

    export default {
        name: "NewPoll",
        props: ['user'],

        mixins: [validationMixin],

        validations: {
            title: { required, maxLength: maxLength(50) },
            description: { required },
            $each: {
                option: { required, maxLength: maxLength(50) }
            },
            options: {
                required,
                $each: { required }
            }
        },
        data: () => ({
            title: '',
            description: '',
            hours: 1,
            options: [
                ''
            ]
        }),
        methods: {
            addOption() {
                if (this.options.length  < 7)
                    this.options.push('')
            },
            removeOption(ind) {
                if (this.options.length > 1)
                    this.options.splice(ind, 1)
            },
            create_poll() {
                let option_error = false
                for (let option of this.options) {
                    if (option.replace(/^\s+|\s+$/g, '') === '') {
                        option_error = true
                        break
                    }
                }
                if (this.title.length > 50 || this.title.replace(/^\s+|\s+$/g, '') === ''
                    || this.description.replace(/^\s+|\s+$/g, '') === ''
                    || option_error)
                {
                    console.log('invalid')
                    return
                }
                this.axios.post(
                    'http://localhost:8000/api/voting/',
                    {
                        title:  this.title,
                        description: this.description,
                        hours: this.hours,
                        options: this.options,
                    },
                    {
                        headers: {Authorization: `Token ${this.user.token}`}
                    }).then(response => {
                        if (response.data.status === 200) {
                            this.$router.push('/')
                        }
                })
            }
        },
        computed: {
            titleErrors () {
                const errors = []
                if (!this.$v.title.$dirty) return errors
                !this.$v.title.maxLength && errors.push('Title must be at most 50 characters long.')
                !this.$v.title.required && errors.push('Title is required.')
                return errors
            },
            descriptionErrors () {
                const errors = []
                if (!this.$v.description.$dirty) return errors
                !this.$v.description.required && errors.push('Description is required.')
                return errors
            }
        }
    }
</script>

<style scoped>

</style>