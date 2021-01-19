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
                  color="teal"
                  label="1 hour"
                  :value="1"
                  selected
              ></v-radio>
              <v-radio
                  color="teal"
                  label="3 hours"
                  :value="3"
              ></v-radio>
              <v-radio
                  color="teal"
                  label="6 hours"
                  :value="6"
              ></v-radio>
              <v-radio
                  color="teal"
                  label="1 day"
                  :value="24"
              ></v-radio>
              <v-radio
                  color="teal"
                  label="1 week"
                  :value="24*7"
              ></v-radio>
              <v-radio
                  color="teal"
                  label="Infinite"
                  :value="24*7*4*10000000"
              ></v-radio>
            </v-radio-group>
            <v-radio-group row>
                      <h3 class="mr-12">Types:   </h3>
                      <v-radio
                          v-if="this.savingType === false"
                          color="teal"
                          @click="one_of_all"
                          label="One of all"
                      ></v-radio>
                      <v-radio
                          v-if="this.savingType === false"
                          color="teal"
                          @click="some_of_all"
                          label="Some of all"
                      ></v-radio>
                      <v-radio
                          v-if="this.savingType === false"
                          color="teal"
                          @click="true_false"
                          label="True/False"
                      ></v-radio>
                      <v-btn v-if="this.savingType === false" color="teal" dark x-small @click="saveType">save type</v-btn>
                      <v-btn v-if="this.savingType === true" color="teal" dark x-small @click="removeType">remove type</v-btn>
            </v-radio-group>
            <v-radio-group row >
                      <h3 class="mr-3">Options:  </h3>
                      <v-icon class="mr-7">{{ options.length }}</v-icon>
                      <v-btn dark color="teal" x-small @click="addOption">add option</v-btn>
            </v-radio-group>
            <v-list v-if="this.one  === true">
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
            <v-list v-if="this.some === true">
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
            <v-list v-if="this.true_false === true">
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

            <v-row justify="space-between">
                <v-col md="auto">
                    <h3 class="mr-7">Image:</h3>
                </v-col>
                <v-col>
                    <v-file-input accept="image/*"
                        label="Select image"
                        prepend-icon="mdi-camera"
                        outlined
                        dense
                        v-model="file"
                        @change="addFiles">
                    </v-file-input>
                </v-col>
            </v-row>
            <v-img max-height="300"
                   contain
                   v-if="file"
                   :ref="'file'"
                   title="photo">
            </v-img>
            <br>
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
            options: [''],
            file: null,
            reader: null,
            one: true,
            some: false,
            true_false: false,
            savingType: false,
        }),
        methods: {
          removeType(){
            this.savingType === false
          },
          saveType(){
            this.savingType === true
            if(this.one === true){
              this.some === false
              this.true_false === false
            }
            if(this.some === true){
              this.one === false
              this.true_false === false
            }
            if(this.true_false === true){
              this.one === false
              this.some === false
            }
          },
          one_of_all() {
            this.one === true
          },
          some_of_all() {
            this.some === true
          },
          true_false() {
            this.true_false === true
          },
            addFiles(){
                    this.reader = new FileReader();
                    this.reader.onloadend = () => {
                        let fileData = this.reader.result
                        let imgRef = this.$refs.file
                        imgRef.src = fileData
                    }
                    this.reader.readAsDataURL(this.file);
            },
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
                let formData = new FormData();
                formData.append('file', this.file)
                formData.append('title', this.title)
                formData.append('description', this.description)
                formData.append('options', this.options)
                formData.append('hours', this.hours)
                formData.append('options', this.options)
                this.axios.post(
                    'http://localhost:8000/api/voting/',
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
                !this.$v.description.required && errors.push('Description is required.')
                return errors
            }
        }
    }
</script>

<style scoped>

</style>