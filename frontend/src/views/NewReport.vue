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
              :counter="500"
              label="Description"
              required clearable
              @input="$v.description.$touch()"
              @blur="$v.description.$touch()"
            ></v-text-field>
            <br>
            <v-btn color="purple"
                   outlined
                   @click="create_report()">
                create new report
            </v-btn>
        </v-card>
    </div>
</template>

<script>
    import { validationMixin } from 'vuelidate'
    import { required, maxLength } from 'vuelidate/lib/validators'

    export default {
        name: "NewReport",
        props: ['user'],

        mixins: [validationMixin],

        validations: {
            title: { required, maxLength: maxLength(50) },
            description: { required, maxLength: maxLength(500) },
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
            reader: null,
        }),
        methods: {
            create_report() {
                let option_error = false
                for (let option of this.options) {
                    if (option.replace(/^\s+|\s+$/g, '') === '') {
                        option_error = true
                        break
                    }
                }
                if (this.title.length > 50 || this.description.length > 500|| this.title.replace(/^\s+|\s+$/g, '') === ''
                    || this.description.replace(/^\s+|\s+$/g, '') === ''
                    || option_error)
                {
                    console.log('invalid')
                    return
                }
                let formData = new FormData();
                formData.append('file', this.file)
                formData.append('title', this.title)
                formData.append('description', this.description)
                formData.append('hours', this.hours)
                formData.append('options', this.options)
                this.axios.post(
                    'http://localhost:8000/api/report/',
                    formData,
                    {
                        headers: {Authorization: `Token ${this.user.token}`}
                    }
                ).then(response => {
                    if (response.data.status === 200) {
                        this.$router.push('/')
                    }
                    else window.alert(response.data.description)
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
                !this.$v.description.maxLength && errors.push('Description must be at most 500 characters long.')
                !this.$v.description.required && errors.push('Description is required.')
                return errors
            }
        }
    }
</script>

<style scoped>

</style>