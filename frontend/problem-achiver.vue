<template>
  <div id='card'>
        <!-- <v-card > -->
          <v-card-title >
            <h1 style="padding-left:30%">
              Problem Achiver
              </h1>
          </v-card-title>

          <v-tabs
            v-model="tab"
            grow
          >
            <v-tab
              v-for="item in items"
              :key="item.code"
            >
              {{ item.code }}
            </v-tab>
          </v-tabs>

          <v-tabs-items v-model="tab">
            <v-tab-item
              v-for="item in items"
              :key="item.code"
            >
              <v-card
                color="basil"
                flat
              >
                <v-card-text>
                  <h1 style="text-align:center;color:red">{{ item.title }}</h1>
                  <br>
                  <hr>
                  <br>
                  <span style="font-size:20px;opacity:1">{{ item.statement }}</span>
                  <br>
                  <br>
                  <hr>
                  <br>
                  <span style="font-size:20px">Your task:       </span>
                  <span style="font-size:20px;opacity:1">{{ item.test_input }}</span>
                  </v-card-text>

              </v-card>
            </v-tab-item>
          </v-tabs-items>
        <!-- </v-card> -->
</div>
</template>



<script>
module.exports = {
    data () {
      return {
        tab: null,
        items: [
          { code: 'One', statement: 'Tab 1 Content' ,'title':'A',test_input:'00000'},
          { code: 'Two', statement: 'Tab 2 Content','title':'A' ,test_input:'00000'},
          { code: 'Three', statement: 'Tab 3 Content','title':'A',test_input:'00000' },
          { code: 'Four', statement: 'Tab 4 Content' ,'title':'A',test_input:'00000'},
          { code: 'Five', statement: 'Tab 5 Content','title':'A' ,test_input:'00000'},
          
          
        ],
       
        
      }
    },
    mounted() {
            axios.get("http://127.0.0.1:8000/api/questionlist")
            .then(response => {
              
              this.items = response.data
              })
              
    }

  }

</script>

<style>


  .basil {
    
          background-color: white ;
  }
    .basil--text {
      color: black ;
    }
    #card{
      border: 5px black dotted;
    }
</style>



