from hashlib import sha256

shop_id = '5'
secretKey = 'SecretKey01'
#secretKey = 'B6iE1vK12gKmWTcMPvH' #need resolve
#secretKey = '0x72C0f0GbSg7nrMjK'

payway = 'payeer_rub'


def sign_creator(amount,
                 currency,
                 shop_id,
                 shop_order_id,
                 secretKey = secretKey): #EUR(code 978) use protocol PAY

    raw_data = '{}:{}:{}:{}{}'.format(amount, currency, shop_id,
                                      str(shop_order_id), secretKey)
    return sha256(raw_data.encode('utf-8')).hexdigest()


def sign_creator_bill(amount,
                      currency,
                      shop_id,
                      shop_order_id,
                      secretKey = secretKey):#USD use API payment (Bill method

    raw_data = '{}:{}:{}:{}:{}{}'.format(currency, amount, currency, shop_id,
                                         str(shop_order_id), secretKey)
    return sha256(raw_data.encode('utf-8')).hexdigest()


def sign_creator_invoice(amount,
                         currency,
                         payway,
                         shop_id,
                         shop_order_id,
                         secretKey = secretKey): #RUB use protocol invoice

    raw_data = '{}:{}:{}:{}:{}{}'.format(amount, currency, payway, shop_id,
                                         str(shop_order_id), secretKey)
    return sha256(raw_data.encode('utf-8')).hexdigest()


def clear_number(number):

    return format(float(number), '.2f')
