<template>
    <nav>
        <v-app-bar color="blue" dark app>
            <v-app-bar-nav-icon @click.stop="drawer = !drawer">

            </v-app-bar-nav-icon>
            <v-toolbar-title class="text-uppercase">
                <span class="font-weight-light">SmartClass</span>
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-menu offset-y>
                <template v-slot:activator="{ on }">
                    <v-btn text v-on="on">
                    <v-icon left>expand_more</v-icon>
                    <span>Menu</span>
                </v-btn>
                </template>
                <v-list flat>
                    <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
                        <v-list-title>{{link.text}}</v-list-title>
                    </v-list-item>
                </v-list>
            </v-menu>
            <v-btn text>
                <span>Salir</span>
                <v-icon right>exit_to_app</v-icon>
            </v-btn>
        </v-app-bar>
        <v-navigation-drawer v-model="drawer" dark app class="reed">
            <v-layout column align-center>
                <v-flex class="mt-5">
                    <v-avatar size="100">
                        <v-img src="../assets/logo.svg"></v-img>
                    </v-avatar>
                    <p class="white--text subheading mt-1 text-center">Usuario Administrador</p>
                </v-flex>
            </v-layout>
            <v-list flat>
                <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
                    <v-list-item-acion>
                        <v-icon>{{link.icon}}</v-icon>
                    </v-list-item-acion>
                    <v-list-item-content>
                        <v-list-item-title>{{link.text}}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
    </nav>
</template>

<script>
export default {
   data: () => ({
      drawer: true,
      links :[
          {icon: 'dashboard', text:'Cargas', route: '/Carga'},
          {icon: 'folder', text:'Manejo de Bloques', route: '/'},
          {icon: 'reporte', text:'Reportes', route: '/Report'}
      ]
     
    }),
    components: {
  },
   
}
</script>