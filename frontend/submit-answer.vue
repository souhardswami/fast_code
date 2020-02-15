<template>
    
    
     <div class="final">
     

     
    
      <input placeholder="       problem number "  v-model="number" ><br>
      <input placeholder="       Answer"  v-model="answer" >
      
      
      <button  @click=submit()>Submit</button>
      <span v-if="seen1">
           <h1>&#x2705;</h1>
      </span>
     <span v-if="seen2">
          <h1>&#x274C;</h1>
      </span>
     </div>
</template>


<script>
module.exports= {
     data(){
          return{
               answer:'',
               number:'',
               
               seen1:false,
               seen2:false,
          }
     },
     
     methods:{

        
        submit(evt){

             
             let self=this;
             self.seen1=false;
             self.seen2=false;
            axios.post('http://127.0.0.1:8000/api/submitionlist', {
                number: this.number,
                answer:this.answer
                }).then(function (response) {
                    res=response.data;
                    if(res=='wrong'){
                         self.seen2=true;
                    }
                    else{
                         self.seen1=true;
                    }
                    
                    
                    
                })
                },
            
             
             
            
             
             
         
     }
     
}
</script>