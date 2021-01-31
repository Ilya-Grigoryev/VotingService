<template>
    <div class="vue-report">
        <v-card
        :elevation="report.status === 'open' ? 7 : 0"
        width="65%"
        class="mx-auto ma-3"
        outlined>
            <v-row justify="space-between" class="px-3">
                <v-col md="auto">
                    <div v-if="report.status === 'open'"
                        style="color: green;">
                        <v-icon color="green">
                            mdi-check-outline
                        </v-icon>
                        <h3> {{ report.status }} </h3>
                    </div>
                    <div v-else
                        style="color: #950c0c;">
                        <v-icon color="#950c0c">
                            mdi-cancel
                        </v-icon>
                        <h3> {{ report.status }} </h3>
                    </div>
                </v-col>
                <v-col md="max">
                    <h2>{{ report.title }}</h2>
                </v-col>
                <v-col md="auto">
                    <v-btn icon x-large @click="$router.push(`/report/${report.id}/`)">
                        <v-icon>
                            mdi-arrow-expand-right
                        </v-icon>
                    </v-btn>
                </v-col>
            </v-row>
        </v-card>
    </div>
</template>

<script>

    export default{
        name: 'Report',
        props: ['user', 'report'],
        data: () => ({

        }),
        methods: {

        },
        mounted() {

        }
    }

</script>

<style>
    .vue-report{
      font-family: 'Avenir', Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      color: #2c3e50;
    }
</style>