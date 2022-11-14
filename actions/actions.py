from typing import Dict, Text, List, Optional, Any
from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import SlotSet, AllSlotsReset, EventType



PURSE_TYPE = {
        "wmp",
        "wmr",
        "wmu",
        "wme",
        "wmb",
        "wmg",
        "wmz",
        "wmk",
        "wmx",
        "wmh",
        "wml",
        "wmy",
        "wmf",
        "wmt",
        "mdl",
        "wmc",
        "wmd",
        "btc",
        "bch",
        "ltc",
        "eth",
        "usdt"
        }



class ValidateTransferForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_transfer_form"

    async def required_slots(
        self,
        slots_mapped_in_domain: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> Optional[List[Text]]:
        required_slots = slots_mapped_in_domain + ["transfer_direction"] + ["transfer_purse_type"] + ["transfer_method"]
        return required_slots


    async def extract_transfer_direction(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:
        if next(tracker.get_latest_entity_values("bank_card", "from"), None) or next(tracker.get_latest_entity_values("bank", "from"), None) or next(tracker.get_latest_entity_values("electronic_money", "from"), None) or next(tracker.get_latest_entity_values("cash", "from"), None) or next(tracker.get_latest_entity_values("telephone_number", "from"), None) or next(tracker.get_latest_entity_values("guarant", "from"), None) or next(tracker.get_latest_entity_values("name", "to"), None) or next(tracker.get_latest_entity_values("purse_type", "to"), None) != None:
            return {"transfer_direction": "to"}

        elif next(tracker.get_latest_entity_values("bank_card", "to"), None) or next(tracker.get_latest_entity_values("bank", "to"), None) or next(tracker.get_latest_entity_values("electronic_money", "to"), None) or next(tracker.get_latest_entity_values("cash", "to"), None) or next(tracker.get_latest_entity_values("telephone_number", "to"), None) or next(tracker.get_latest_entity_values("guarant", "to"), None) or next(tracker.get_latest_entity_values("name", "from"), None) or next(tracker.get_latest_entity_values("purse_type", "from"), None) != None:
            return {"transfer_direction": "from"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("bank_card", None), None) != None:
            return {"transfer_direction": "from"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("bank", None), None) != None:
            return {"transfer_direction": "from"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("electronic_money", None), None) != None:
            return {"transfer_direction": "from"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("cash", None), None) != None:
            return {"transfer_direction": "from"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("telephone_number", None), None) != None:
            return {"transfer_direction": "from"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("transfer_purse_type", None), None) == None:
            return {"transfer_direction": "to"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("transfer_method", None), None) == None:
            return {"transfer_direction": "to"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("bank_card", None), None) != None:
            return {"transfer_direction": "from"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("bank", None), None) != None:
            return {"transfer_direction": "from"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("electronic_money", None), None) != None:
            return {"transfer_direction": "from"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("cash", None), None) != None:
            return {"transfer_direction": "from"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("telephone_number", None), None) != None:
            return {"transfer_direction": "from"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("transfer_purse_type", None), None) == None:
            return {"transfer_direction": "from"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("transfer_method", None), None) == None:
            return {"transfer_direction": "from"}


    async def extract_transfer_purse_type(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:
        transfer_purse_type = next(tracker.get_latest_entity_values("purse_type"), None)
        if transfer_purse_type != None:
            return {"transfer_purse_type": transfer_purse_type}


    async def extract_transfer_method(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:
        if next(tracker.get_latest_entity_values("bank_card"), None) or next(tracker.get_latest_entity_values("bank"), None) != None:
            return {"transfer_method": "transfer_bank"}
        
        elif next(tracker.get_latest_entity_values("electronic_money"), None) != None:
            return {"transfer_method": "transfer_electronic_money"}
        
        elif next(tracker.get_latest_entity_values("cash"), None) != None:
            return {"transfer_method": "transfer_cash"}
        
        elif next(tracker.get_latest_entity_values("telephone_number"), None) != None:
            return {"transfer_method": "transfer_telephone_number"}
        
        elif next(tracker.get_latest_entity_values("guarant"), None) != None:
            return {"transfer_method": "transfer_guarant"}


    def validate_verb(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        transfer_direction = tracker.get_slot("transfer_direction")

        if transfer_direction == None and slot_value == None:
            return {"requested_slot": None, "transfer_purse_type": None}

        if transfer_direction != None:
            if transfer_direction == "from":
                return {"verb": "withdraw"}
            elif transfer_direction == "to":
                return {"verb": "topup"}

        if slot_value in {"topup", "withdraw"}:
            return {"verb": slot_value}
        else:
            return {"verb": None}

    def validate_transfer_direction(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        if slot_value in {"to", "from"}:
            return {"transfer_direction": slot_value}
        else:
            return {"transfer_direction": None}


    def validate_transfer_purse_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        transfer_method = tracker.get_slot("transfer_method")

        if slot_value in PURSE_TYPE:
            if slot_value in {"wmp", "wmr", "wmu", "wmc", "wmd", "mdl"}:
                return {"transfer_purse_type": slot_value, "transfer_method": None, "requested_slot": None}

            elif transfer_method in {"transfer_bank", "transfer_cash"}:
                if slot_value in {"wmx", "wmf", "wmh", "wml", "wmt", "btc", "bch", "ltc", "eth", "usdt"}:
                    dispatcher.utter_message(response="utter_this_method_is_not_possible")
                    dispatcher.utter_message("-1")
                    return {"transfer_purse_type": slot_value, "transfer_method": None}
            
            elif transfer_method == "transfer_guarant":
                if slot_value in {"wmy", "wmz", "wme", "wmb", "wmk"}:
                    dispatcher.utter_message(response="utter_this_method_is_not_possible")
                    dispatcher.utter_message("-1")
                    return {"transfer_purse_type": slot_value, "transfer_method": None}

            return {"transfer_purse_type": slot_value}
        else:
            dispatcher.utter_message(response="utter_purse_does_not_exist")
            return {"transfer_purse_type": None}


    def validate_transfer_method(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        transfer_purse_type = tracker.get_slot("transfer_purse_type")
        transfer_direction = tracker.get_slot("transfer_direction")
        verb = tracker.get_slot("verb")
        latest_intent_name = tracker.latest_message["intent"].get("name")

        if latest_intent_name == "transfer.telephone_number" or slot_value == "transfer_telephone_number":
            return {"transfer_method": 'transfer_telephone_number', "transfer_purse_type": None, "requested_slot": None}

        if transfer_purse_type == None:

            if latest_intent_name in {"transfer.banks", "transfer.bank_card"} or slot_value == "transfer_bank":
                return {"transfer_method": 'transfer_bank'}

            elif latest_intent_name == "transfer.electronic_money" or slot_value == "transfer_electronic_money":
                return {"transfer_method": 'transfer_electronic_money'}

            elif latest_intent_name == "transfer.guarant" or slot_value == "transfer_guarant":
                return {"transfer_method": 'transfer_guarant'}

            elif latest_intent_name == "transfer.cash" or slot_value == "transfer_cash":
                return {"transfer_method": 'transfer_cash'}

            else:
                dispatcher.utter_message(response="utter_this_method_is_not_possible")
                dispatcher.utter_message("0")
                return {"transfer_method": None}


        elif transfer_purse_type in {"wmx", "wmf", "wmh", "wml", "wmt", "btc", "bch", "ltc", "eth", "usdt"}:

            if latest_intent_name == "transfer.electronic_money" or slot_value == "transfer_electronic_money":
                return {"transfer_method": 'transfer_electronic_money'}

            elif latest_intent_name == "transfer.guarant" or slot_value == "transfer_guarant":
                return {"transfer_method": 'transfer_guarant'}

            else:
                dispatcher.utter_message(response="utter_this_method_is_not_possible")
                dispatcher.utter_message("1")
                return {"transfer_method": None}

        elif transfer_purse_type in {"wmz", "wme", "wmb", "wmk"}:

            if latest_intent_name in {"transfer.banks", "transfer.bank_card"} or slot_value == "transfer_bank":
                return {"transfer_method": 'transfer_bank'}

            elif latest_intent_name == "transfer.electronic_money" or slot_value == "transfer_electronic_money":
                return {"transfer_method": 'transfer_electronic_money'}

            elif latest_intent_name == "transfer.cash" or slot_value == "transfer_cash":
                return {"transfer_method": 'transfer_cash'}

            else:
                dispatcher.utter_message(response="utter_this_method_is_not_possible")
                dispatcher.utter_message("2")
                return {"transfer_method": None}


        elif transfer_purse_type == "wmg":

            if transfer_direction == "from" or verb == "withdraw":

                if latest_intent_name == "transfer.guarant" or slot_value == "guarant":
                    return {"transfer_method": 'transfer_guarant'}

            if latest_intent_name in {"transfer.banks", "transfer.bank_card"} or slot_value == "transfer_bank":
                return {"transfer_method": 'transfer_bank'}

            elif latest_intent_name == "transfer.electronic_money" or slot_value == "transfer_electronic_money":
                return {"transfer_method": 'transfer_electronic_money'}

            elif latest_intent_name == "transfer.cash" or slot_value == "transfer_cash":
                return {"transfer_method": 'transfer_cash'}

            else:
                dispatcher.utter_message(response="utter_this_method_is_not_possible")
                dispatcher.utter_message("3")
                return {"transfer_method": None}


        elif transfer_purse_type == "wmy":

            if latest_intent_name in {"transfer.banks", "transfer.bank_card"} or slot_value == "transfer_bank":
                return {"transfer_method": 'transfer_bank'}
            else:
                dispatcher.utter_message(response="utter_this_method_is_not_possible")
                dispatcher.utter_message("4")
                return {"transfer_method": None}


        elif transfer_purse_type in {"wmp", "wmr", "wmu", "wmc", "wmd", "mdl"}:
            return {"transfer_method": None, "requested_slot": None}

        else:
            return {"transfer_method": None}












class ActionAskTransferFormTransferPurseType(Action):
    def name(self) -> Text:
        return "action_ask_transfer_form_transfer_purse_type"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        transfer_direction = tracker.get_slot("transfer_direction")
        dispatcher.utter_message(response=f"utter_ask_transfer_form_{transfer_direction}_transfer_purse_type")
        return []



class ActionAskTransferFormTransferPurseTypeTransferMethod(Action):
    def name(self) -> Text:
        return "action_ask_transfer_form_transfer_method"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        transfer_direction = tracker.get_slot("transfer_direction")
        transfer_purse_type = tracker.get_slot("transfer_purse_type")
        dispatcher.utter_message(response=f"utter_ask_transfer_form_{transfer_direction}_{transfer_purse_type}_transfer_method")
        return []











class Action(Action):
    def name(self) -> Text:
        return "action_slots_restart"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        return [SlotSet("transfer_direction", None), SlotSet("transfer_purse_type", None), SlotSet("transfer_method", None), SlotSet("verb", None) ]






class ActionTransferFormMessage(Action):
    def name(self) -> Text:
        return "action_transfer_form_message"

    async def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        transfer_direction = tracker.get_slot("transfer_direction")
        transfer_purse_type = tracker.get_slot("transfer_purse_type")
        transfer_method = tracker.get_slot("transfer_method")
        dispatcher.utter_message(response=f"utter_transfer_form_{transfer_direction}_{transfer_purse_type}_{transfer_method}")
        return []
