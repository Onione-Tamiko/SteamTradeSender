
pip install steampy openpyxl

This script can send trading offers from the account 
on which it is authorized to another (to the main one).

File.xlsx(Excel) should have 4 columns:
Login,Password,Api key,Recipient ID

In stempy client.py change to:

*def make_offer(self, items_from_me: List[Asset], items_from_them: List[Asset], partner_steam_id: str,
                   message: str = '',identity_secret = '',steam_id = '') -> dict:*
*response.update(self._confirm_transaction(response['tradeofferid'],identity_secret =identity_secret,steam_id=steam_id))*
*def _confirm_transaction(self, trade_offer_id: str,identity_secret ,steam_id ) -> dict:
        confirmation_executor = ConfirmationExecutor(identity_secret, steam_id ,
                                                     self._session)
        return confirmation_executor.send_trade_allow_request(trade_offer_id)*
