$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})
$('.plus-cart').click(function() {

     console.log('plus Clicked') 
    var id=$(this).attr("pid").toString();
    var em=this.parentNode.children[2] 
    console.log(id)
    $.ajax({
        type:"GET",
        url:'/pluscart',
        data:{
            prod_id:id
        },
        success:function(data){
            console.log(data)
            console.log('Success')
            em.innerText=data.quantity
            document.getElementById('amount').innerText=data.amount
            document.getElementById('totalamount').innerText=data.totalamount
            
        }

    })

})
// minus function runs

$('.minus-cart').click(function() {

    console.log('plus Clicked') 
   var id=$(this).attr("pid").toString();
   var em=this.parentNode.children[2] 
   console.log(id)
   $.ajax({
       type:"GET",
       url:'/minuscart',
       data:{
           prod_id:id
       },
       success:function(data){
           console.log(data)
           console.log('Success')
           em.innerText=data.quantity
           document.getElementById('amount').innerText=data.amount
           document.getElementById('totalamount').innerText=data.totalamount
           
       }

   })

})
// remove-cart function is runs

$('.remove-cart').click(function() {

    console.log('delete') 
   var id=$(this).attr("pid").toString();
   var em=this 
   console.log(id)
   $.ajax({
       type:"GET",
       url:'/removecart',
       data:{
           prod_id:id
       },
       success:function(data){
           console.log(data)
           console.log('Success')
           
           document.getElementById('amount').innerText=data.amount
           document.getElementById('totalamount').innerText=data.totalamount
           em.parentNode.parentNode.parentNode.parentNode.remove()
           
       }

   })

})