from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received

def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        print("----------------------------------")
        print("The Payment is Comepleted")
        print("Payment Status:", ipn_obj.payment_status)
        print("Transaction ID:", ipn_obj.txn_id)
        print("Invoice ID:", ipn_obj.invoice)
        print("Receiver Email:", ipn_obj.receiver_email)
        print("Payer Email:", ipn_obj.payer_email)
        print("Payment Amount:", ipn_obj.mc_gross)
        print("Currency Code:", ipn_obj.mc_currency)
        print("Custom Field:", ipn_obj.custom)
        print("Transaction Type:", ipn_obj.txn_type)
        print("Verification Signature:", ipn_obj.verify_sign)
        print("IP Address:", ipn_obj.ipaddress)
        print("Flagged for Review:", ipn_obj.flag)
        print("Flag Info:", ipn_obj.flag_info)
        print("Is Test IPN:", ipn_obj.test_ipn)
        print("----------------------------------")
    else:
        print("The Payment is not Comepleted")
valid_ipn_received.connect(show_me_the_money)