<template>
    <v-footer dark padless app inset>
        <v-card class="flex" flat title color="reed" :elevation="10">
            <v-card-text class="py-2 white--text text-center">
                {{new Date().getFullYear()}} - <strong>SmartClass</strong>
            </v-card-text>
        </v-card>
    </v-footer>
</template>