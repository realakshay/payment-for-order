# payment-for-order

## Description
This is simple application where items are stored in database and user can buy these items with quanity. 

<b>ItemModel</b> contain <b>(id,name,price)</b> and <b>OrderModel</b>
contain <b>(id,status,total_bill,purchase_date,time)</b>.
Here new model <b>ItemInOrderModel</b> is secondary table which is used for handle <b>many-to-many relationship</b>.


<b>Important Libraries</b>

    Flask
    Flask-RESTful
    Marshmallow
    Flask-SQLAlchemy
    Stripe


How to run app:
  
    python mainapp.py




### More About Payment

For payment purpose we have used <b>Stripe Payment Gateway</b>

You can install stripe as

    pip install stripe

Stripe provide two keys i.e. <b>publishable_key</b> and <b>secret_key</b>

We use secret key as,

    import stripe
    stripe.api_key = "Your-Secret_Key"
    
First of all we purchase items then order resource make payment. For payment purpose stripe provide two important methos.

  <b>It will create token</b>
  
    stripe.Token.create(
      card={
          #Customer Card Details
          "number": "xxxxxxxxxxxxxxxx",
          "exp_month": xx,
          "exp_year": xxxx,
          "cvc": "xxx",
      }
    )
  
and, <b>It will make charge</b>

    stripe.Charge.create(
            amount=xxx,
            currency=CURRENCY,
            description="",
            source=token
        )
