from pytonapi import Tonapi

# Enter your API key
API_KEY = "AFH7AUTQMY4CKMAAAAAA76X6K36GZN2YICGMSAS2Q5TOIL3WRXCKQ7QCFORMLXAIXUQWICA"  # noqa

# Specify the account ID
ACCOUNT_ID = "kQBWtsaGAc7WQInphnDBaz6D0LqVW09ysY1rNX5RcKnI_ElC"  # noqa


def main():
    # Creating new Tonapi object
    tonapi = Tonapi(api_key=API_KEY,is_testnet=True)
    account = tonapi.accounts.get_info(account_id=ACCOUNT_ID)

    
    print(f"Balance nanoton: {account.balance.to_nano()}")
    

    print(f"Balance TON: {account.balance.to_amount()}")
    


if __name__ == '__main__':
    main()