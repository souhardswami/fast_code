<template>
    
    
    <div>
        
                <div id="end"  class="editor"> 

                    <div>
                        <ul>
                        
                            <li><div id="c-red" class="circle"></div></li>
                            <li><div id="c-yellow" class="circle"></div></li>
                            <li><div id="c-green" class="circle"></div></li>
                            <li><div class="other" >write your code</div></li>
                            <li><div class="other" >language:</div></li>
                            <li>
                                <select v-model="language">
                                        
                                        <option v-for="myOption in languages" :value="myOption" :key="myOption">{{ myOption }}</option>
                                </select>
                                


                                
                            </li>
                            
                        </ul>
                    </div>



                    <div id="overall" >
                                <div contenteditable="true" spellcheck="false"  style="outline: none" @blur="onEdit">
                                            <div id="page-1" class="page" style="display: block" >
                                                <br>
                                                <br>

                                                
                                                N=int(input())<br>
                                                for i in range(N):<br>
                                                &nbsp;&nbsp;&nbsp;&nbsp;for j in range(N):<br>
                                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if(i==j):<br>
                                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(1)<br>
                                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else:<br>
                                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(0)
                                                <br>
                                                <br>
                                                <br>
                                                <br>
                                                <br>
                                                <br>
                                            </div>
                                        
                                </div>
                    </div>


                    <div id="fake"></div>

                    </div>





                    <div class="compile">
                        <ul>
                        
                            
                            <li><div class="other1" ><h1>custom input</h1></div></li>
                            
                            <li><div class="other1" ><button @click=compile()>compile</button></div></li>
                            
                        </ul>
                    </div>

                    <div class="custom-input">

                        
                        <textarea rows="4" cols="50" v-model="stdin" >

                        </textarea>
                        <br>
                        <br>
                        <br>
                        <span v-if="seen">
                            <ul>
                                <h3>output: {{output.output}}</h3>
                                <h3>memory:{{output.memory}}Kb</h3>
                                <h3>time:{{output.cpuTime}}</h3>
                            </ul>
                        </span>
                        
                                

                        
                        
                    
                        
                        
                        
                       
                    
                    </div>
                    
                    
                    

                    
    </div>
   

</template>




<script>



    
module.exports = {

    

    data () {
      return {
        
        seen:false,
        tab: null,
        code:'',
        language:'',
        languages: ['python3','c++','c','java','sql'],
        
        stdin: '',
        output:[]
        
 
        
        
        
        
        
      }
    },
    
    methods:{

        
        onEdit(evt){
             var src = evt.target.innerText
             
             this.code = src
             
            
             
             
            
             
             
         },
         
         
        
         
         
         
         
         

        compile: function(){
            let self=this;
            axios.post('http://127.0.0.1:8000/api/codeexecute', {
                code: this.code,
                language: this.language,
                stdin:  this.stdin
                }).then(function (response) {
                    self.seen=true;
                    
                    self.output = response.data
                    
                    
                    
                })
                },
        
        
        
            
    },
    
}


</script>