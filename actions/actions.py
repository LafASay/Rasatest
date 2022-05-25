from typing import Text, List, Any, Dict
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import EventType, SlotSet, AllSlotsReset
from rasa_sdk import Action



class ValidateTransferForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_transfer_form"


    def validate_transfer_verb(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if slot_value == "exchange" \
        or slot_value == "transfer":
            return {"transfer_verb": slot_value, \
            "transfer_purse_type": "wmz", \
            "transfer_method": "bank_card"}
        elif slot_value == "withdraw" \
        or slot_value == "topup":
            return {"transfer_verb": slot_value}
        else:
            return {"transfer_verb": None}



    def validate_transfer_purse_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if tracker.get_slot("transfer_verb") == "withdraw":
            if slot_value == "wmp":
                dispatcher.utter_message(response="utter_transfer_form_transfer_wmp_wmr")
                return {"transfer_purse_type": slot_value, "transfer_method": "bank_card"}
            elif slot_value == "wme":
                return {"transfer_purse_type": slot_value}
            elif slot_value == "wmb":
                return {"transfer_purse_type": slot_value}
            elif slot_value == "wmg":
                return {"transfer_purse_type": slot_value}
            elif slot_value == "wmz":
                return {"transfer_purse_type": slot_value}
            elif slot_value == "wmk":
                return {"transfer_purse_type": slot_value}
            elif slot_value == "wmy":
                if tracker.get_slot("transfer_method") == "bank_card":
                    return {"transfer_purse_type": slot_value}
                else:
                    dispatcher.utter_message(response="utter_transfer_form_withdraw_transfer_method_wmy")
                    return {"transfer_purse_type": slot_value, "transfer_method": "bank_card"}
            elif slot_value == "wmv":
                return {"transfer_purse_type": slot_value}
            elif slot_value == "wmx":
                return {"transfer_purse_type": slot_value}
            elif slot_value == "wmh":
                return {"transfer_purse_type": slot_value}
            elif slot_value == "wml":
                return {"transfer_purse_type": slot_value}
            elif slot_value == "wmr":
                dispatcher.utter_message(response="utter_transfer_form_transfer_wmp_wmr")
                return {"transfer_purse_type": slot_value, "transfer_method": "bank_card"}
            elif slot_value == "wmc":
                return {"transfer_purse_type": slot_value}
            elif slot_value == "wmd":
                return {"transfer_purse_type": slot_value}
            elif slot_value == "wmu":
                dispatcher.utter_message(response="utter_transfer_form_transfer_wmu")
                return {"transfer_purse_type": slot_value, "transfer_method": "bank_card"}



        elif tracker.get_slot("transfer_verb") == "topup":
            if slot_value == "wmp":
                dispatcher.utter_message(response="utter_transfer_form_transfer_wmp_wmr")
                return {"transfer_purse_type": slot_value, "transfer_method": "bank_card"}
            elif slot_value == "wme":
                return {"transfer_purse_type": slot_value}
            elif slot_value == "wmb":
                return {"transfer_purse_type": slot_value}
            elif slot_value == "wmg":
                return {"transfer_purse_type": slot_value}
            elif slot_value == "wmz":
                return {"transfer_purse_type": slot_value}
            elif slot_value == "wmk":
                return {"transfer_purse_type": slot_value}
            elif slot_value == "wmy":
                if tracker.get_slot("transfer_method") == "bank_card":
                    return {"transfer_purse_type": slot_value}
                else:
                    dispatcher.utter_message(response="utter_transfer_form_topup_transfer_method_wmy")
                    return {"transfer_purse_type": slot_value, "transfer_method": "bank_card"}
            elif slot_value == "wmv":
                return {"transfer_purse_type": slot_value}
            elif slot_value == "wmx":
                return {"transfer_purse_type": slot_value}
            elif slot_value == "wmh":
                return {"transfer_purse_type": slot_value}
            elif slot_value == "wml":
                return {"transfer_purse_type": slot_value}
            elif slot_value == "wmr":
                dispatcher.utter_message(response="utter_transfer_form_transfer_wmp_wmr")
                return {"transfer_purse_type": slot_value, "transfer_method": "bank_card"}
            elif slot_value == "wmc":
                return {"transfer_purse_type": slot_value}
            elif slot_value == "wmd":
                return {"transfer_purse_type": slot_value}
            elif slot_value == "wmu":
                dispatcher.utter_message(response="utter_transfer_form_transfer_wmu")
                return {"transfer_purse_type": slot_value, "transfer_method": "bank_card"}

        else:
            return {"transfer_purse_type": None}



    def validate_transfer_method(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if tracker.get_slot("transfer_verb") == "withdraw":
            if tracker.get_slot("transfer_purse_type") == "wmz":
                if slot_value == "bank_card" \
                or slot_value == "bank_account" \
                or slot_value == "electronic_money" \
                or slot_value == "cash":
                    return {"transfer_method": slot_value}
                elif slot_value == "qiwi" \
                or slot_value == "юmoney":
                    return {"transfer_method": 'electronic_money'}
                else:
                    dispatcher.utter_message(text="utter_this_method_is_not_possible")
                    return {"transfer_method": None}

        if tracker.get_slot("transfer_verb") == "withdraw":
            if tracker.get_slot("transfer_purse_type") == "wme":
                if slot_value == "bank_card" \
                or slot_value == "bank_account" \
                or slot_value == "electronic_money" \
                or slot_value == "cash":
                    return {"transfer_method": slot_value}
                elif slot_value == "qiwi" \
                or slot_value == "юmoney":
                    return {"transfer_method": 'electronic_money'}
                else:
                    dispatcher.utter_message(text="utter_this_method_is_not_possible")
                    return {"transfer_method": None}

        if tracker.get_slot("transfer_verb") == "withdraw":
            if tracker.get_slot("transfer_purse_type") == "wmb":
                if slot_value == "bank_card" \
                or slot_value == "bank_account" \
                or slot_value == "electronic_money" \
                or slot_value == "cash":
                    return {"transfer_method": slot_value}
                elif slot_value == "qiwi" \
                or slot_value == "юmoney":
                    return {"transfer_method": 'electronic_money'}
                else:
                    dispatcher.utter_message(text="utter_this_method_is_not_possible")
                    return {"transfer_method": None}

        if tracker.get_slot("transfer_verb") == "withdraw":
            if tracker.get_slot("transfer_purse_type") == "wmk":
                if slot_value == "bank_card" \
                or slot_value == "bank_account" \
                or slot_value == "electronic_money" \
                or slot_value == "cash":
                    return {"transfer_method": slot_value}
                elif slot_value == "qiwi" \
                or slot_value == "юmoney":
                    return {"transfer_method": 'electronic_money'}
                else:
                    dispatcher.utter_message(text="utter_this_method_is_not_possible")
                    return {"transfer_method": None}

        if tracker.get_slot("transfer_verb") == "withdraw":
            if tracker.get_slot("transfer_purse_type") == "wmy":
                if slot_value == "bank_card":
                    return {"transfer_method": slot_value}
                else:
                    return {"transfer_method": "bank_card"}

        if tracker.get_slot("transfer_verb") == "withdraw":
            if tracker.get_slot("transfer_purse_type") == "wmx":
                if slot_value == "electronic_money" \
                or slot_value == "from_storage_with_the_guarantor":
                    return {"transfer_method": slot_value}
                elif slot_value == "qiwi" \
                or slot_value == "юmoney":
                    return {"transfer_method": 'electronic_money'}
                else:
                    dispatcher.utter_message(text="utter_this_method_is_not_possible")
                    return {"transfer_method": None}

        if tracker.get_slot("transfer_verb") == "withdraw":
            if tracker.get_slot("transfer_purse_type") == "wmh":
                if slot_value == "electronic_money" \
                or slot_value == "from_storage_with_the_guarantor":
                    return {"transfer_method": slot_value}
                elif slot_value == "qiwi" \
                or slot_value == "юmoney":
                    return {"transfer_method": 'electronic_money'}
                else:
                    dispatcher.utter_message(text="utter_this_method_is_not_possible")
                    return {"transfer_method": None}

        if tracker.get_slot("transfer_verb") == "withdraw":
            if tracker.get_slot("transfer_purse_type") == "wml":
                if slot_value == "electronic_money" \
                or slot_value == "from_storage_with_the_guarantor":
                    return {"transfer_method": slot_value}
                elif slot_value == "qiwi" \
                or slot_value == "юmoney":
                    return {"transfer_method": 'electronic_money'}
                else:
                    dispatcher.utter_message(text="utter_this_method_is_not_possible")
                    return {"transfer_method": None}

        if tracker.get_slot("transfer_verb") == "withdraw":
            if tracker.get_slot("transfer_purse_type") == "wmg":
                if slot_value == "bank_account" \
                or slot_value == "electronic_money" \
                or slot_value == "cash" \
                or slot_value == "from_storage_with_the_guarantor":
                    return {"transfer_method": slot_value}
                elif slot_value == "qiwi" \
                or slot_value == "юmoney":
                    return {"transfer_method": 'electronic_money'}
                else:
                    dispatcher.utter_message(text="utter_this_method_is_not_possible")
                    return {"transfer_method": None}

        if tracker.get_slot("transfer_verb") == "topup":
            if tracker.get_slot("transfer_purse_type") == "wmz":
                if slot_value == "bank_card" \
                or slot_value == "bank_account" \
                or slot_value == "electronic_money" \
                or slot_value == "cash":
                    return {"transfer_method": slot_value}
                elif slot_value == "qiwi" \
                or slot_value == "юmoney":
                    return {"transfer_method": 'electronic_money'}
                else:
                    dispatcher.utter_message(text="utter_this_topup_method_is_not_possible")
                    return {"transfer_method": None}

        if tracker.get_slot("transfer_verb") == "topup":
            if tracker.get_slot("transfer_purse_type") == "wme":
                if slot_value == "bank_card" \
                or slot_value == "bank_account" \
                or slot_value == "electronic_money" \
                or slot_value == "cash":
                    return {"transfer_method": slot_value}
                elif slot_value == "qiwi" \
                or slot_value == "юmoney":
                    return {"transfer_method": 'electronic_money'}
                else:
                    dispatcher.utter_message(text="utter_this_topup_method_is_not_possible")
                    return {"transfer_method": None}

        if tracker.get_slot("transfer_verb") == "topup":
            if tracker.get_slot("transfer_purse_type") == "wmb":
                if slot_value == "bank_card" \
                or slot_value == "bank_account" \
                or slot_value == "electronic_money" \
                or slot_value == "cash":
                    return {"transfer_method": slot_value}
                elif slot_value == "qiwi" \
                or slot_value == "юmoney":
                    return {"transfer_method": 'electronic_money'}
                else:
                    dispatcher.utter_message(text="utter_this_topup_method_is_not_possible")
                    return {"transfer_method": None}

        if tracker.get_slot("transfer_verb") == "topup":
            if tracker.get_slot("transfer_purse_type") == "wmk":
                if slot_value == "bank_card" \
                or slot_value == "bank_account" \
                or slot_value == "electronic_money" \
                or slot_value == "cash":
                    return {"transfer_method": slot_value}
                elif slot_value == "qiwi" \
                or slot_value == "юmoney":
                    return {"transfer_method": 'electronic_money'}
                else:
                    dispatcher.utter_message(text="utter_this_topup_method_is_not_possible")
                    return {"transfer_method": None}

        if tracker.get_slot("transfer_verb") == "topup":
            if tracker.get_slot("transfer_purse_type") == "wmy":
                if slot_value == "bank_card":
                    return {"transfer_method": slot_value}
                else:
                    return {"transfer_method": None}

        if tracker.get_slot("transfer_verb") == "topup":
            if tracker.get_slot("transfer_purse_type") == "wmx":
                if slot_value == "electronic_money" \
                or slot_value == "from_storage_with_the_guarantor":
                    return {"transfer_method": slot_value}
                elif slot_value == "qiwi" \
                or slot_value == "юmoney":
                    return {"transfer_method": 'electronic_money'}
                else:
                    dispatcher.utter_message(text="utter_this_topup_method_is_not_possible")
                    return {"transfer_method": None}

        if tracker.get_slot("transfer_verb") == "topup":
            if tracker.get_slot("transfer_purse_type") == "wmh":
                if slot_value == "electronic_money" \
                or slot_value == "from_storage_with_the_guarantor":
                    return {"transfer_method": slot_value}
                elif slot_value == "qiwi" \
                or slot_value == "юmoney":
                    return {"transfer_method": 'electronic_money'}
                else:
                    dispatcher.utter_message(text="utter_this_topup_method_is_not_possible")
                    return {"transfer_method": None}

        if tracker.get_slot("transfer_verb") == "topup":
            if tracker.get_slot("transfer_purse_type") == "wml":
                if slot_value == "electronic_money" \
                or slot_value == "from_storage_with_the_guarantor":
                    return {"transfer_method": slot_value}
                elif slot_value == "qiwi" \
                or slot_value == "юmoney":
                    return {"transfer_method": 'electronic_money'}
                else:
                    dispatcher.utter_message(text="utter_this_topup_method_is_not_possible")
                    return {"transfer_method": None}

        if tracker.get_slot("transfer_verb") == "topup":
            if tracker.get_slot("transfer_purse_type") == "wmg":
                if slot_value == "bank_account" \
                or slot_value == "electronic_money" \
                or slot_value == "cash" \
                or slot_value == "from_storage_with_the_guarantor":
                    return {"transfer_method": slot_value}
                elif slot_value == "qiwi" \
                or slot_value == "юmoney":
                    return {"transfer_method": 'electronic_money'}
                else:
                    dispatcher.utter_message(text="utter_this_topup_method_is_not_possible")
                    return {"transfer_method": None}





# class AskForSlotAction(Action):
#     def name(self) -> Text:
#         return "action_ask_transfer_verb"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         dispatcher.utter_message(text="Скажи действие")
#         return []






class AskForSlotAction(Action):
    def name(self) -> Text:
        return "action_ask_transfer_form_transfer_purse_type"


    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        if tracker.get_slot("transfer_verb") == "withdraw":
            dispatcher.utter_message(response="utter_ask_transfer_form_withdraw_transfer_purse_type")
        elif tracker.get_slot("transfer_verb") == "topup":
            dispatcher.utter_message(response="utter_ask_transfer_form_topup_transfer_purse_type")
        return []



class AskForSlotAction(Action):
    def name(self) -> Text:
        return "action_ask_transfer_form_transfer_method"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        if tracker.get_slot("transfer_verb") == "withdraw":
            if tracker.get_slot("transfer_purse_type") == "wmz":
                dispatcher.utter_message(response="utter_transfer_form_withdraw_transfer_method_wmz")

        if tracker.get_slot("transfer_verb") == "withdraw":
            if tracker.get_slot("transfer_purse_type") == "wme":
                dispatcher.utter_message(response="utter_transfer_form_withdraw_transfer_method_wme")

        if tracker.get_slot("transfer_verb") == "withdraw":
            if tracker.get_slot("transfer_purse_type") == "wmb":
                dispatcher.utter_message(response="utter_transfer_form_withdraw_transfer_method_wmb")

        if tracker.get_slot("transfer_verb") == "withdraw":
            if tracker.get_slot("transfer_purse_type") == "wmk":
                dispatcher.utter_message(response="utter_transfer_form_withdraw_transfer_method_wmk")

        if tracker.get_slot("transfer_verb") == "withdraw":
            if tracker.get_slot("transfer_purse_type") == "wmy":
                dispatcher.utter_message(response="utter_transfer_form_withdraw_transfer_method_wmy")

        if tracker.get_slot("transfer_verb") == "withdraw":
            if tracker.get_slot("transfer_purse_type") == "wmx":
                dispatcher.utter_message(response="utter_transfer_form_withdraw_transfer_method_wmx")

        if tracker.get_slot("transfer_verb") == "withdraw":
            if tracker.get_slot("transfer_purse_type") == "wmh":
                dispatcher.utter_message(response="utter_transfer_form_withdraw_transfer_method_wmh")

        if tracker.get_slot("transfer_verb") == "withdraw":
            if tracker.get_slot("transfer_purse_type") == "wml":
                dispatcher.utter_message(response="utter_transfer_form_withdraw_transfer_method_wml")

        if tracker.get_slot("transfer_verb") == "withdraw":
            if tracker.get_slot("transfer_purse_type") == "wmg":
                dispatcher.utter_message(response="utter_transfer_form_withdraw_transfer_method_wmg")

        if tracker.get_slot("transfer_verb") == "topup":
            if tracker.get_slot("transfer_purse_type") == "wmz":
                dispatcher.utter_message(response="utter_transfer_form_topup_transfer_method_wmz")

        if tracker.get_slot("transfer_verb") == "topup":
            if tracker.get_slot("transfer_purse_type") == "wme":
                dispatcher.utter_message(response="utter_transfer_form_topup_transfer_method_wme")
            
        if tracker.get_slot("transfer_verb") == "topup":
            if tracker.get_slot("transfer_purse_type") == "wmb":
                dispatcher.utter_message(response="utter_transfer_form_topup_transfer_method_wmb")
            
        if tracker.get_slot("transfer_verb") == "topup":
            if tracker.get_slot("transfer_purse_type") == "wmk":
                dispatcher.utter_message(response="utter_transfer_form_topup_transfer_method_wmk")

        if tracker.get_slot("transfer_verb") == "topup":
            if tracker.get_slot("transfer_purse_type") == "wmx":
                dispatcher.utter_message(response="utter_transfer_form_topup_transfer_method_wmx")

        if tracker.get_slot("transfer_verb") == "topup":
            if tracker.get_slot("transfer_purse_type") == "wmh":
                dispatcher.utter_message(response="utter_transfer_form_topup_transfer_method_wmh")

        if tracker.get_slot("transfer_verb") == "topup":
            if tracker.get_slot("transfer_purse_type") == "wml":
                dispatcher.utter_message(response="utter_transfer_form_topup_transfer_method_wml")

        if tracker.get_slot("transfer_verb") == "topup":
            if tracker.get_slot("transfer_purse_type") == "wmg":
                dispatcher.utter_message(response="utter_transfer_form_topup_transfer_method_wmg")
        return []



class ActionTransferFormMessage(Action):
    def name(self) -> Text:
        return "action_transfer_form_message"


    async def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        if tracker.get_slot("transfer_verb") == "exchange":
            dispatcher.utter_message(response="utter_transfer_form_transfer_method_exchange")

        if tracker.get_slot("transfer_verb") == "transfer":
            dispatcher.utter_message(response="utter_transfer_form_transfer_method_transfer")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wmz" \
        and tracker.get_slot("transfer_method") == "bank_card":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wmz_bank_card")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wmz" \
        and tracker.get_slot("transfer_method") == "bank_account":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wmz_bank_account")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wmz" \
        and tracker.get_slot("transfer_method") == "electronic_money":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wmz_electronic_money")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wmz" \
        and tracker.get_slot("transfer_method") == "cash":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wmz_cash")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wme" \
        and tracker.get_slot("transfer_method") == "bank_card":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wme_bank_card")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wme" \
        and tracker.get_slot("transfer_method") == "bank_account":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wme_bank_account")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wme" \
        and tracker.get_slot("transfer_method") == "electronic_money":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wme_electronic_money")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wme" \
        and tracker.get_slot("transfer_method") == "cash":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wme_cash")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wmb" \
        and tracker.get_slot("transfer_method") == "bank_card":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wmb_bank_card")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wmb" \
        and tracker.get_slot("transfer_method") == "bank_account":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wmb_bank_account")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wmb" \
        and tracker.get_slot("transfer_method") == "electronic_money":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wmb_electronic_money")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wmb" \
        and tracker.get_slot("transfer_method") == "cash":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wmb_cash")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wmk" \
        and tracker.get_slot("transfer_method") == "bank_card":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wmk_bank_card")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wmk" \
        and tracker.get_slot("transfer_method") == "bank_account":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wmk_bank_account")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wmk" \
        and tracker.get_slot("transfer_method") == "electronic_money":
            dispatcher.utter_message("Ответ")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wmk" \
        and tracker.get_slot("transfer_method") == "cash":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wmk_cash")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wmy" \
        and tracker.get_slot("transfer_method") == "bank_card":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wmy_bank_card")    

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wmx" \
        and tracker.get_slot("transfer_method") == "electronic_money":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wmx_electronic_money")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wmx" \
        and tracker.get_slot("transfer_method") == "from_storage_with_the_guarantor":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wmx_from_storage_with_the_guarantor")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wmh" \
        and tracker.get_slot("transfer_method") == "electronic_money":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wmh_electronic_money")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wmh" \
        and tracker.get_slot("transfer_method") == "from_storage_with_the_guarantor":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wmh_from_storage_with_the_guarantor")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wml" \
        and tracker.get_slot("transfer_method") == "electronic_money":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wml_electronic_money")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wml" \
        and tracker.get_slot("transfer_method") == "from_storage_with_the_guarantor":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wml_from_storage_with_the_guarantor")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wmg" \
        and tracker.get_slot("transfer_method") == "bank_account":
            dispatcher.utter_message("Ответ")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wmg" \
        and tracker.get_slot("transfer_method") == "electronic_money":
            dispatcher.utter_message("Ответ")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wmg" \
        and tracker.get_slot("transfer_method") == "cash":
            dispatcher.utter_message(response="utter_transfer_form_withdraw_wmg_cash")

        if tracker.get_slot("transfer_verb") == "withdraw" \
        and tracker.get_slot("transfer_purse_type") == "wmg" \
        and tracker.get_slot("transfer_method") == "from_storage_with_the_guarantor":
            dispatcher.utter_message("Ответ")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wmz" \
        and tracker.get_slot("transfer_method") == "bank_card":
            dispatcher.utter_message(response="utter_transfer_form_topup_wmz_bank_card")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wmz" \
        and tracker.get_slot("transfer_method") == "bank_account":
            dispatcher.utter_message(response="utter_transfer_form_topup_wmz_bank_account")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wmz" \
        and tracker.get_slot("transfer_method") == "electronic_money":
            dispatcher.utter_message(response="utter_transfer_form_topup_wmz_electronic_money")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wmz" \
        and tracker.get_slot("transfer_method") == "cash":
            dispatcher.utter_message(response="utter_transfer_form_topup_wmz_cash")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wme" \
        and tracker.get_slot("transfer_method") == "bank_card":
            dispatcher.utter_message(response="utter_transfer_form_topup_wme_bank_card")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wme" \
        and tracker.get_slot("transfer_method") == "bank_account":
            dispatcher.utter_message(response="utter_transfer_form_topup_wme_bank_account")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wme" \
        and tracker.get_slot("transfer_method") == "electronic_money":
            dispatcher.utter_message(response="utter_transfer_form_topup_wme_electronic_money")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wme" \
        and tracker.get_slot("transfer_method") == "cash":
            dispatcher.utter_message(response="utter_transfer_form_topup_wme_cash")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wmb" \
        and tracker.get_slot("transfer_method") == "bank_card":
            dispatcher.utter_message(response="utter_transfer_form_topup_wmb_bank_card")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wmb" \
        and tracker.get_slot("transfer_method") == "bank_account":
            dispatcher.utter_message(response="utter_transfer_form_topup_wmb_bank_account")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wmb" \
        and tracker.get_slot("transfer_method") == "electronic_money":
            dispatcher.utter_message(response="utter_transfer_form_topup_wmb_electronic_money")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wmb" \
        and tracker.get_slot("transfer_method") == "cash":
            dispatcher.utter_message(response="utter_transfer_form_topup_wmb_cash")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wmk" \
        and tracker.get_slot("transfer_method") == "bank_card":
            dispatcher.utter_message(response="utter_transfer_form_topup_wmk_bank_card")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wmk" \
        and tracker.get_slot("transfer_method") == "bank_account":
            dispatcher.utter_message(response="utter_transfer_form_topup_wmk_bank_account")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wmk" \
        and tracker.get_slot("transfer_method") == "electronic_money":
            dispatcher.utter_message("Ответ") 

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wmk" \
        and tracker.get_slot("transfer_method") == "cash":
            dispatcher.utter_message(response="utter_transfer_form_topup_wmk_cash")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wmk" \
        and tracker.get_slot("transfer_method") == "from_storage_with_the_guarantor":
            dispatcher.utter_message("Ответ")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wmy" \
        and tracker.get_slot("transfer_method") == "bank_card":
            dispatcher.utter_message(response="utter_transfer_form_topup_wmy_bank_card")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wmx" \
        and tracker.get_slot("transfer_method") == "electronic_money":
            dispatcher.utter_message(response="utter_transfer_form_topup_wmx_electronic_money")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wmx" \
        and tracker.get_slot("transfer_method") == "from_storage_with_the_guarantor":
            dispatcher.utter_message(response="utter_transfer_form_topup_wmx_from_storage_with_the_guarantor")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wmh" \
        and tracker.get_slot("transfer_method") == "electronic_money":
            dispatcher.utter_message(response="utter_transfer_form_topup_wmh_electronic_money")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wmh" \
        and tracker.get_slot("transfer_method") == "from_storage_with_the_guarantor":
            dispatcher.utter_message(response="utter_transfer_form_topup_wmh_from_storage_with_the_guarantor")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wml" \
        and tracker.get_slot("transfer_method") == "electronic_money":
            dispatcher.utter_message(response="utter_transfer_form_topup_wml_electronic_money")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wml" \
        and tracker.get_slot("transfer_method") == "from_storage_with_the_guarantor":
            dispatcher.utter_message(response="utter_transfer_form_topup_wml_from_storage_with_the_guarantor")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wmg" \
        and tracker.get_slot("transfer_method") == "bank_account":
            dispatcher.utter_message(response="utter_transfer_form_topup_wmg_bank_account")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wmg" \
        and tracker.get_slot("transfer_method") == "electronic_money":
            dispatcher.utter_message(response="utter_transfer_form_topup_wmg_electronic_money")

        if tracker.get_slot("transfer_verb") == "topup" \
        and tracker.get_slot("transfer_purse_type") == "wmg" \
        and tracker.get_slot("transfer_method") == "cash":
            dispatcher.utter_message(response="utter_transfer_form_topup_wmg_cash")
        return [SlotSet("transfer_verb", None), SlotSet("transfer_purse_type", None), SlotSet("transfer_method", None)]



class ValidatePassportForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_passport_form"


    def validate_passport_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if slot_value == "alias" \
        or slot_value == "formal" \
        or slot_value == "initial" \
        or slot_value == "personal":
            return {"transfer_purse_type": slot_value}
        else:
            return {"transfer_purse_type": None}



class ActionPassportFormMessage(Action):
    def name(self) -> Text:
        return "action_passport_form_message"


    async def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        if tracker.get_slot("passport_type") == "alias":
            dispatcher.utter_message(response="utter_passport.how_get_passport_alias")

        if tracker.get_slot("passport_type") == "formal":
            dispatcher.utter_message(response="utter_passport.how_get_passport_formal")

        if tracker.get_slot("passport_type") == "initial":
            dispatcher.utter_message(response="utter_passport.how_get_passport_initial")

        if tracker.get_slot("passport_type") == "personal":
            dispatcher.utter_message(response="utter_passport.how_get_passport_personal")
        return []




# class ValidateTransferForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_transfer_form"

#     def validate_transfer_verb(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:

#         transfer_verb = slot_value
#         if transfer_verb == "withdraw" or transfer_verb == "topup" or transfer_verb == "exchange" or transfer_verb == "transfer":
#             return {"transfer_verb": transfer_verb}
#         else:
#             return {"transfer_verb": None}


#     def validate_transfer_purse_type(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:

#         transfer_purse_type = slot_value
#         if transfer_purse_type == "wmp" \
#         or transfer_purse_type == "wme" \
#         or transfer_purse_type == "wmb" \
#         or transfer_purse_type == "wmg" \
#         or transfer_purse_type == "wmz" \
#         or transfer_purse_type == "wmk" \
#         or transfer_purse_type == "wmv" \
#         or transfer_purse_type == "wmx" \
#         or transfer_purse_type == "wmh" \
#         or transfer_purse_type == "wml" \
#         or transfer_purse_type == "wmy" \
#         or transfer_purse_type == "wmr" \
#         or transfer_purse_type == "wmc" \
#         or transfer_purse_type == "wmd" \
#         or transfer_purse_type == "wmu":
#             return {"transfer_purse_type": transfer_purse_type}
#         else:
#             return {"transfer_purse_type": None}


#     def validate_transfer_method(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:

#         transfer_method = slot_value
#         if transfer_method == "bank_card" \
#         or transfer_method == "bank_account" \
#         or transfer_method == "electronic_money" \
#         or transfer_method == "qiwi" \
#         or transfer_method == "юmoney" \
#         or transfer_method == "cash" \
#         or transfer_method == "from_storage_with_the_guarantor" \
#         or transfer_method == "telephone_number":
#             return {"transfer_method": transfer_method}
#         else:
#             return {"transfer_method": None}



# class AskForSlotAction(Action):
#     def name(self) -> Text:
#         return "action_ask_transfer_verb"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         dispatcher.utter_message(text="Скажи действие")
#         return []



# class AskForSlotAction(Action):
#     def name(self) -> Text:
#         return "action_ask_transfer_purse_type"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         dispatcher.utter_message(text="Скажи тип кошелька")
#         return []



# class AskForSlotAction(Action):
#     def name(self) -> Text:
#         return "action_ask_transfer_method"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         dispatcher.utter_message(text="Скажи метод")
#         return []
