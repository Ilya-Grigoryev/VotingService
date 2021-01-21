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
              <v-radio
                  label="Infinite"
                  value="infinite"
              ></v-radio>
            </v-radio-group>
            <v-row>
                <v-col md="auto">
                    <h3 class="mr-7">Start time:</h3>
                    <v-checkbox
                      v-model="start_now"
                      label="Start now"
                      hide-details
                      class="shrink mr-2 mt-0"
                    ></v-checkbox>
                </v-col>
                <v-col
                  md="max"
                >
                  <v-menu
                    ref="menu1"
                    v-model="menu1"
                    :close-on-content-click="false"
                    :return-value.sync="date"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        :disabled="start_now"
                        v-model="date"
                        label="Date"
                        prepend-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                      v-model="date"
                      no-title
                      scrollable
                    >
                      <v-spacer></v-spacer>
                      <v-btn
                        text
                        color="primary"
                        @click="menu1 = false"
                      >
                        Cancel
                      </v-btn>
                      <v-btn
                        text
                        color="primary"
                        @click="$refs.menu1.save(date)"
                      >
                        OK
                      </v-btn>
                    </v-date-picker>
                  </v-menu>
                </v-col>
                <v-col
                  md="max"
                >
                  <v-menu
                    ref="menu2"
                    v-model="menu2"
                    :close-on-content-click="false"
                    :nudge-right="40"
                    :return-value.sync="time"
                    transition="scale-transition"
                    offset-y
                    max-width="290px"
                    min-width="290px"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        :disabled="start_now"
                        v-model="time"
                        label="Time"
                        prepend-icon="mdi-clock-time-four-outline"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-time-picker
                      v-if="menu2"
                      v-model="time"
                      full-width
                      @click:minute="$refs.menu2.save(time)"
                    ></v-time-picker>
                  </v-menu>
                </v-col>
            </v-row>
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
            start_now: true,
            menu1: false,
            menu2: false,
            date: '',
            time: '',
            title: '',
            description: '',
            hours: 1,
            options: [''],
            file: null,
            reader: null,
        }),
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
                formData.append('hours', this.hours)
                formData.append('options', this.options)
                if (!this.start_now)
                    formData.append('start', `${this.date} ${this.time}`)
                else
                    formData.append('start', 'now')
                this.axios.post(
                    'http://localhost:8000/api/voting/',
                    formData,
                    {
                        headers: {Authorization: `Token ${this.user.token}`}
                    }
                ).then(response => {
                    if (response.data.status === 200) {
                        this.$router.push('/all-polls')
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