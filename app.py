
import cvfy

app = cvfy.register('nongh:0.0.0.0:4278297:3000:8000')

@cvfy.crossdomain
@app.listen()
def concat():
    
    ## receiving the data
    alltext = cvfy.getTextArray()
    
    ## processing the data
    joined_and_uppercase = (alltext[0] + ' ' + alltext[1]).upper()
    and_then_reversed = joined_and_uppercase[::-1]
    
    ## sending back the data
    cvfy.sendTextArray([joined_and_uppercase, and_then_reversed])
    return 'OK'
        
app.run()
