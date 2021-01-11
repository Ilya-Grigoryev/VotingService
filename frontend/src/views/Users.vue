<template>
    <div>
        <v-card
          class="mx-auto pa-3 ma-3"
          elevation="4"
          outlined
          width="65%">
            <v-row justify="space-between">
                <v-col md="6" class="pa-5"
                       v-for="(user, i) in users" :key="i">
                    <v-card>
                        <v-list-item three-line>
                          <v-list-item-avatar size="80">
                              <img v-if="user.avatar === 'null'"
                                   src="https://ishwortimilsina.com/images/icon_no_avatar.svg">
                              <img v-else
                                   :src="`http://localhost:8000${user.avatar}/`">
                          </v-list-item-avatar>
                          <v-list-item-content>
                            <v-list-item-title class="headline mb-1">
                                {{user.first_name}} {{user.last_name}}
                            </v-list-item-title>
                            <v-list-item-subtitle>
                                <v-btn @click="$router.push(`/profile/${user.id}`)" block>@{{user.username}}</v-btn>
                            </v-list-item-subtitle>
                          </v-list-item-content>
                        </v-list-item>
                    </v-card>
                </v-col>
            </v-row>
        </v-card>
    </div>
</template>

<script>
    export default {
        name: "Users",
        props: ['user'],
        data: () => ({
            users: []
        }),
        methods: {
            getUsers() {
                this.axios.get('http://localhost:8000/api/users/')
                .then(response => {
                    this.users = response.data
                })
            }
        },
        mounted() {
            this.getUsers()
        }
    }
</script>

<style scoped>

</style>