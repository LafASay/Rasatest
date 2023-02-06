from typing import Text, List, Any, Dict
from rasa_sdk import Tracker, FormValidationAction,Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import EventType, SlotSet, SessionStarted, ActionExecuted



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

PASSPORT_TYPE = {
        "alias_passport",
        "formal_passport",
        "initial_passport",
        "personal_passport",
        "merchant_passport",
        "capitaller_passport",
        "transact_automation_tool_passport",
        "developer_passport",
        "registrar_passport",
        "service_passport",
        "guarantor_passport",
        "operator_passport"}



class ValidateHowGetPassportForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_how_get_passport_form"

    def validate_passport_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        if slot_value in PASSPORT_TYPE:
            return {"passport_type": slot_value}
        else:
            dispatcher.utter_message(response="utter_passport_type_does_not_exist")
            return {"passport_type": None}



class ActionHowGetPassportFormMessage(Action):
    def name(self) -> Text:
        return "action_how_get_passport_form_message"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[Dict[Text, Any]]:
        passport_type = tracker.get_slot("passport_type")
        dispatcher.utter_message(response=f"utter_passport.how_get_passport_{passport_type}")
        return []



class ValidatePurseRequirementForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_purse_requirement_form"

    def validate_purse_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if slot_value in PURSE_TYPE:
            return {"purse_type": slot_value}
        else:
            dispatcher.utter_message(response="utter_purse_does_not_exist")
            return {"purse_type": None}



class ActionPurseRequirementFormMessage(Action):
    def name(self) -> Text:
        return "action_purse_requirement_form_message"

    async def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        purse_type = tracker.get_slot("purse_type")
        dispatcher.utter_message(response=f"utter_purses.purse_requirement_{purse_type}")
        return []



class ValidatePurseDisappearedForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_purse_disappeared_form"

    def validate_purse_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if slot_value in PURSE_TYPE:
            return {"purse_type": slot_value}
        else:
            dispatcher.utter_message(response="utter_purse_does_not_exist")
            return {"purse_type": None}



class ActionPurseDisappearedFormMessage(Action):
    def name(self) -> Text:
        return "action_purse_disappeared_form_message"

    async def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        purse_type = tracker.get_slot("purse_type")
        dispatcher.utter_message(response=f"utter_purses.purse_disappeared_{purse_type}")
        return []









































# class ActionAskTransferWithdrawFormTransferPurseType(Action):
#     def name(self) -> Text:
#         return "action_ask_transfer.withdraw_form_transfer_purse_type"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         dispatcher.utter_message(response="utter_ask_transfer.withdraw_form_transfer_purse_type")
#         return []


# class ActionAskTransferWithdrawFormTransferMethod(Action):
#     def name(self) -> Text:
#         return "action_ask_transfer.withdraw_form_transfer_method"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         transfer_purse_type = tracker.get_slot("transfer_purse_type")
#         dispatcher.utter_message(response=f"utter_ask_transfer_withdraw_form_{transfer_purse_type}_transfer_method")
#         return []


# class ActionAskTransferTopupFormTransferPurseType(Action):
#     def name(self) -> Text:
#         return "action_ask_transfer.topup_form_transfer_purse_type"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         dispatcher.utter_message(response="utter_ask_transfer.topup_form_transfer_purse_type")
#         return []


# class ActionAskTransferTopupFormTransferMethod(Action):
#     def name(self) -> Text:
#         return "action_ask_transfer.topup_form_transfer_method"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         transfer_purse_type = tracker.get_slot("transfer_purse_type")
#         dispatcher.utter_message(response=f"utter_ask_transfer_topup_form_{transfer_purse_type}_transfer_method")
#         return []


# class ActionTransferWithdrawFormMessage(Action):
#     def name(self) -> Text:
#         return "action_transfer.withdraw_form_message"

#     async def run(
#         self,
#         dispatcher,
#         tracker: Tracker,
#         domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:
#         transfer_purse_type = tracker.get_slot("transfer_purse_type")
#         transfer_method = tracker.get_slot("transfer_method")
#         dispatcher.utter_message(response=f"utter_transfer_withdraw_form_{transfer_purse_type}_{transfer_method}")
#         return []


# class ValidateTransferWithdrawForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_transfer.withdraw_form"

#     def validate_transfer_purse_type(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         if slot_value in PURSE_TYPE:
#             if slot_value in {"wmp", "wmr", "wmu", "wmc", "wmd", "mdl"}:
#                 return {"transfer_purse_type": slot_value, "transfer_method": None, "requested_slot": None}
#             return {"transfer_purse_type": slot_value}
#         else:
#             return {"transfer_purse_type": None}

#     def validate_transfer_method(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         transfer_purse_type = tracker.get_slot("transfer_purse_type")
#         latest_intent_name = tracker.latest_message["intent"].get("name")

#         if latest_intent_name == "transfer.telephone_number" or slot_value == "telephone_number":
#             return {"transfer_method": 'transfer_telephone_number', "transfer_purse_type": None, "requested_slot": None}

#         if transfer_purse_type == None:

#             if latest_intent_name in {"transfer.banks", "transfer.bank_card"} or slot_value in {"bank_card", "bank"}:
#                 return {"transfer_method": 'transfer_bank'}

#             elif latest_intent_name == "transfer.electronic_money" or slot_value in {"electronic_money", "qiwi", "юmoney"}:
#                 return {"transfer_method": 'transfer_electronic_money'}

#             elif latest_intent_name == "transfer.guarant" or slot_value == "guarant":
#                 return {"transfer_method": 'transfer_guarant'}

#             elif latest_intent_name == "transfer.cash" or slot_value == "cash":
#                 return {"transfer_method": 'transfer_cash'}

#             else:
#                 dispatcher.utter_message(response="utter_this_withdraw_method_is_not_possible")
#                 return {"transfer_method": None, }

#         elif transfer_purse_type in {"wmx", "wmf", "wmh", "wml", "wmt"}:

#             if latest_intent_name == "transfer.electronic_money" or slot_value in {"electronic_money", "qiwi", "юmoney"}:
#                 return {"transfer_method": 'transfer_electronic_money'}

#             elif latest_intent_name == "transfer.guarant" or slot_value == "guarant":
#                 return {"transfer_method": 'transfer_guarant'}

#             else:
#                 dispatcher.utter_message(response="utter_this_withdraw_method_is_not_possible")
#                 return {"transfer_method": None}

#         elif transfer_purse_type in {"wmz", "wme", "wmb", "wmk"}:

#             if latest_intent_name in {"transfer.banks", "transfer.bank_card"} or slot_value in {"bank_card", "bank"}:
#                 return {"transfer_method": 'transfer_bank'}

#             elif latest_intent_name == "transfer.electronic_money" or slot_value in {"electronic_money", "qiwi", "юmoney"}:
#                 return {"transfer_method": 'transfer_electronic_money'}

#             elif latest_intent_name == "transfer.cash" or slot_value == "cash":
#                 return {"transfer_method": 'transfer_cash'}

#             else:
#                 dispatcher.utter_message(response="utter_this_withdraw_method_is_not_possible")
#                 return {"transfer_method": None}

#         elif transfer_purse_type == "wmg":

#             if latest_intent_name in {"transfer.banks", "transfer.bank_card"} or slot_value in {"bank_card", "bank"}:
#                 return {"transfer_method": 'transfer_bank'}

#             elif latest_intent_name == "transfer.guarant" or slot_value == "guarant":
#                 return {"transfer_method": None}

#             elif latest_intent_name == "transfer.cash" or slot_value == "cash":
#                 return {"transfer_method": 'transfer_cash'}

#             else:
#                 dispatcher.utter_message(response="utter_this_withdraw_method_is_not_possible")
#                 return {"transfer_method": None}

#         elif transfer_purse_type == "wmy":

#             if latest_intent_name in {"transfer.banks", "transfer.bank_card"} or slot_value in {"bank_card", "bank"}:
#                 return {"transfer_method": 'transfer_bank'}

#             else:
#                 dispatcher.utter_message(response="utter_this_withdraw_method_is_not_possible")
#                 return {"transfer_method": None}

#         elif transfer_purse_type in {"wmp", "wmr", "wmu", "wmc", "wmd", "mdl"}:
#             return {"transfer_method": None, "requested_slot": None}

#         else:
#             return {"transfer_method": slot_value, "transfer_purse_type": None, "requested_slot": 'transfer_purse_type'}
































# class ValidateTransferTopupForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_transfer.topup_form"

#     # def validate_transfer_purse_type(
#     #     self,
#     #     slot_value: Any,
#     #     dispatcher: CollectingDispatcher,
#     #     tracker: Tracker,
#     #     domain: DomainDict,
#     # ) -> Dict[Text, Any]:
#     #     if slot_value in PURSE_TYPE:
#     #         if slot_value in {"wmp", "wmr", "wmu", "wmc", "wmd", "mdl"}:
#     #             return {"transfer_purse_type": slot_value, "transfer_method": None, "requested_slot": None}
#     #         return {"transfer_purse_type": slot_value}
#     #     else:
#     #         return {"transfer_purse_type": None}

#     def validate_transfer_method(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         transfer_purse_type = tracker.get_slot("transfer_purse_type")
#         latest_intent_name = tracker.latest_message["intent"].get("name")

#         if latest_intent_name == "transfer.telephone_number" or slot_value == "telephone_number":
#             return {"transfer_method": 'transfer_telephone_number', "transfer_purse_type": None, "requested_slot": None}

#         if transfer_purse_type == None:

#             if latest_intent_name in {"transfer.banks", "transfer.bank_card"} or slot_value in {"bank_card", "bank"}:
#                 return {"transfer_method": 'transfer_bank'}

#             elif latest_intent_name == "transfer.electronic_money" or slot_value in {"electronic_money", "qiwi", "юmoney"}:
#                 return {"transfer_method": 'transfer_electronic_money'}

#             elif latest_intent_name == "transfer.guarant" or slot_value == "guarant":
#                 return {"transfer_method": 'transfer_guarant'}

#             elif latest_intent_name == "transfer.cash" or slot_value == "cash":
#                 return {"transfer_method": 'transfer_cash'}

#             else:
#                 dispatcher.utter_message(response="utter_this_topup_method_is_not_possible")
#                 return {"transfer_method": None, }

#         elif transfer_purse_type in {"wmx", "wmf", "wmh", "wml", "wmt"}:

#             if latest_intent_name == "transfer.electronic_money" or slot_value in {"electronic_money", "qiwi", "юmoney"}:
#                 return {"transfer_method": 'transfer_electronic_money'}

#             elif latest_intent_name == "transfer.guarant" or slot_value == "guarant":
#                 return {"transfer_method": 'transfer_guarant'}

#             else:
#                 dispatcher.utter_message(response="utter_this_topup_method_is_not_possible")
#                 return {"transfer_method": None}

#         elif transfer_purse_type in {"wmz", "wme", "wmb", "wmk"}:

#             if latest_intent_name in {"transfer.banks", "transfer.bank_card"} or slot_value in {"bank_card", "bank"}:
#                 return {"transfer_method": 'transfer_bank'}

#             elif latest_intent_name == "transfer.electronic_money" or slot_value in {"electronic_money", "qiwi", "юmoney"}:
#                 return {"transfer_method": 'transfer_electronic_money'}

#             elif latest_intent_name == "transfer.cash" or slot_value == "cash":
#                 return {"transfer_method": 'transfer_cash'}

#             else:
#                 dispatcher.utter_message(response="utter_this_topup_method_is_not_possible")
#                 return {"transfer_method": None}

#         elif transfer_purse_type == "wmg":

#             if latest_intent_name in {"transfer.banks", "transfer.bank_card"} or slot_value in {"bank_card", "bank"}:
#                 return {"transfer_method": 'transfer_bank'}

#             elif latest_intent_name == "transfer.electronic_money" or slot_value in {"electronic_money", "qiwi", "юmoney"}:
#                 return {"transfer_method": 'transfer_electronic_money'}

#             elif latest_intent_name == "transfer.cash" or slot_value == "cash":
#                 return {"transfer_method": 'transfer_cash'}

#             else:
#                 dispatcher.utter_message(response="utter_this_topup_method_is_not_possible")
#                 return {"transfer_method": None}

#         elif transfer_purse_type == "wmy":

#             if latest_intent_name in {"transfer.banks", "transfer.bank_card"} or slot_value in {"bank_card", "bank"}:
#                 return {"transfer_method": 'transfer_bank'}

#             else:
#                 dispatcher.utter_message(response="utter_this_topup_method_is_not_possible")
#                 return {"transfer_method": None}

#         elif transfer_purse_type in {"wmp", "wmr", "wmu", "wmc", "wmd", "mdl"}:
#             return {"transfer_method": None, "requested_slot": None}

#         else:
#             return {"transfer_method": slot_value, "transfer_purse_type": None, "requested_slot": 'transfer_purse_type'}






# class ActionTransferTopupFormMessage(Action):
#     def name(self) -> Text:
#         return "action_transfer.topup_form_message"

#     async def run(
#         self,
#         dispatcher,
#         tracker: Tracker,
#         domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:
#         transfer_purse_type = tracker.get_slot("transfer_purse_type")
#         transfer_method = tracker.get_slot("transfer_method")
#         dispatcher.utter_message(response=f"utter_transfer_topup_form_{transfer_purse_type}_{transfer_method}")
#         return []


















# # class ActionSayHello(Action): 
# #     def name(self) -> Text:
# #         return "action_say_hello"

# #     def run(self,
# #             dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]):

# #         events = [SessionStarted()]

# #         dispatcher.utter_message(response="utter_hi_bye.greet")
# #         print(SessionStarted())

# #         return events


# # class ActionPassportFormMessage(Action):
# #     def name(self) -> Text:
# #         return "action_passport_form_message"

# #     async def run(
# #         self,
# #         dispatcher,
# #         tracker: Tracker,
# #         domain: "DomainDict",
# #     ) -> List[Dict[Text, Any]]:
# #         passport_type = tracker.get_slot("passport_type")
# #         dispatcher.utter_message(response=f"utter_passport.how_get_passport_{passport_type}")
# #         return []


# # class ActionSayHello(Action):

# #     def name(self) -> Text:
# #         return "action_say_hello"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
# #         purse_number = tracker.get_slot("purse_number")
# #         purse_type = purse_number[0]
# #         return [SlotSet("purse_type", purse_type)]





















































































class ValidateTransferForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_transfer_form"

    async def required_slots(
        self,
        slots_mapped_in_domain: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        purse_type = next(tracker.get_latest_entity_values("purse_type"), None)
        purse_type_from = next(tracker.get_latest_entity_values("purse_type", entity_role = "from"), None)
        purse_type_to = next(tracker.get_latest_entity_values("purse_type", entity_role = "to"), None)
        fee = tracker.get_slot("fee")
        # protected_payment = tracker.get_slot("protected_payment")



        if purse_type != None and purse_type_from == None:
            purse_type_from = purse_type
            purse_type = None



        required_slots = ["transfer_direction"] + ["transfer_purse_type"] + ["transfer_method"]
        required_slots_2 = ["transfer_direction"]
        required_slots_fee = ["transfer_direction"] + ["transfer_purse_type"]

        print (f'purse_type = {purse_type}')
        print (f'purse_type_from = {purse_type_from}')
        print (f'purse_type_to = {purse_type_to}')

        if tracker.latest_message["intent"].get("name") == "transfer.transfer" and next(tracker.get_latest_entity_values("verb"), None) == None and next(tracker.get_latest_entity_values("bank_card"), None) == None and next(tracker.get_latest_entity_values("bank_card", "from"), None) == None and next(tracker.get_latest_entity_values("bank_card", "to"), None) == None and next(tracker.get_latest_entity_values("bank_card", "through"), None) == None and next(tracker.get_latest_entity_values("bank"), None) == None and next(tracker.get_latest_entity_values("bank", "from"), None) == None and next(tracker.get_latest_entity_values("bank", "to"), None) == None and next(tracker.get_latest_entity_values("bank", "through"), None) == None and next(tracker.get_latest_entity_values("electronic_money"), None) == None and next(tracker.get_latest_entity_values("electronic_money", "from"), None) == None and next(tracker.get_latest_entity_values("electronic_money", "to"), None) == None and next(tracker.get_latest_entity_values("electronic_money", "through"), None) == None and next(tracker.get_latest_entity_values("cash"), None) == None and next(tracker.get_latest_entity_values("cash", "from"), None) == None and next(tracker.get_latest_entity_values("cash", "to"), None) == None and next(tracker.get_latest_entity_values("cash", "through"), None) == None and next(tracker.get_latest_entity_values("telephone_number"), None) == None and next(tracker.get_latest_entity_values("telephone_number", "from"), None) == None and next(tracker.get_latest_entity_values("telephone_number", "to"), None) == None and next(tracker.get_latest_entity_values("telephone_number", "through"), None) == None and next(tracker.get_latest_entity_values("guarant"), None) == None and next(tracker.get_latest_entity_values("guarant", "from"), None) == None and next(tracker.get_latest_entity_values("guarant", "to"), None) == None and next(tracker.get_latest_entity_values("guarant", "through"), None) == None:
            return required_slots_2
        
        elif tracker.latest_message["intent"].get("name") == "transfer.transfer" and next(tracker.get_latest_entity_values("verb"), None) == "exchange" and next(tracker.get_latest_entity_values("bank_card"), None) == None and next(tracker.get_latest_entity_values("bank"), None) == None and next(tracker.get_latest_entity_values("electronic_money"), None) == None and next(tracker.get_latest_entity_values("cash"), None) == None and next(tracker.get_latest_entity_values("telephone_number"), None) == None and next(tracker.get_latest_entity_values("guarant"), None) == None:
            return required_slots_2

        elif fee != None and next(tracker.get_latest_entity_values("bank_card"), None) == None and next(tracker.get_latest_entity_values("bank"), None) == None and next(tracker.get_latest_entity_values("electronic_money"), None) == None and next(tracker.get_latest_entity_values("cash"), None) == None and next(tracker.get_latest_entity_values("telephone_number"), None) == None and next(tracker.get_latest_entity_values("guarant"), None) == None:
            return required_slots_fee

        else:
            return required_slots


    async def extract_transfer_direction(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:
        
        if next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("bank_card", "from"), None) != None:
            return {"transfer_direction": "topup"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("bank_card", "through"), None) != None:
            return {"transfer_direction": "withdraw"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("bank_card", "from"), None) != None:
            return {"transfer_direction": "topup"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("bank_card", "through"), None) != None:
            return {"transfer_direction": "topup"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("bank_card", None), None) != None:
            return {"transfer_direction": "withdraw"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("bank_card"), None) != None:
            return {"transfer_direction": "withdraw"}


        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("bank", "from"), None) != None:
            return {"transfer_direction": "topup"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("bank", "from"), None) != None:
            return {"transfer_direction": "topup"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("bank", "through"), None) != None:
            return {"transfer_direction": "topup"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("bank", "through"), None) != None:
            return {"transfer_direction": "withdraw"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("bank", None), None) != None:
            return {"transfer_direction": "withdraw"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("bank", None), None) != None:
            return {"transfer_direction": "withdraw"}


        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("telephone_number", "from"), None) != None:
            return {"transfer_direction": "topup"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("telephone_number", "from"), None) != None:
            return {"transfer_direction": "topup"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("telephone_number", "through"), None) != None:
            return {"transfer_direction": "withdraw"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("telephone_number", "through"), None) != None:
            return {"transfer_direction": "topup"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("telephone_number", None), None) != None:
            return {"transfer_direction": "withdraw"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("telephone_number", None), None) != None:
            return {"transfer_direction": "withdraw"}


        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("cash", "from"), None) != None:
            return {"transfer_direction": "topup"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("cash", "from"), None) != None:
            return {"transfer_direction": "topup"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("cash", "through"), None) != None:
            return {"transfer_direction": "withdraw"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("cash", "through"), None) != None:
            return {"transfer_direction": "topup"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("cash", None), None) != None:
            return {"transfer_direction": "withdraw"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("cash", None), None) != None:
            return {"transfer_direction": "topup"}


        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("electronic_money", "from"), None) != None:
            return {"transfer_direction": "topup"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("electronic_money", "from"), None) != None:
            return {"transfer_direction": "topup"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("electronic_money", "through"), None) != None:
            return {"transfer_direction": "withdraw"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("electronic_money", "through"), None) != None:
            return {"transfer_direction": "topup"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("electronic_money", None), None) != None:
            return {"transfer_direction": "withdraw"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("electronic_money", None), None) != None:
            return {"transfer_direction": "withdraw"}


        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("transfer_purse_type", None), None) == None:
            return {"transfer_direction": "topup"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("transfer_purse_type", None), None) == None:
            return {"transfer_direction": "withdraw"}


        if next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("name", "to"), None) != None:
            return {"transfer_direction": "topup"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("name", "to"), None) != None:
            return {"transfer_direction": "topup"}






        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("name", "from"), None) != None:
            return {"transfer_direction": "withdraw"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("name", "from"), None) != None:
            return {"transfer_direction": "withdraw"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "topup" and next(tracker.get_latest_entity_values("name", None), None) != None:
            return {"transfer_direction": "topup"}

        elif next(tracker.get_latest_entity_values("verb"), None) == "withdraw" and next(tracker.get_latest_entity_values("name", None), None) != None:
            return {"transfer_direction": "withdraw"}



        elif next(tracker.get_latest_entity_values("verb"), None) == "exchange":
            if next(tracker.get_latest_entity_values("bank_card", "from"), None) != None or next(tracker.get_latest_entity_values("bank", "from"), None) != None or next(tracker.get_latest_entity_values("electronic_money", "from"), None) != None or next(tracker.get_latest_entity_values("cash", "from"), None) != None or next(tracker.get_latest_entity_values("telephone_number", "from"), None) != None or next(tracker.get_latest_entity_values("guarant", "from"), None) != None:
                return {"transfer_direction": "topup"}

            elif next(tracker.get_latest_entity_values("bank_card", "to"), None) != None or next(tracker.get_latest_entity_values("bank", "to"), None) != None or next(tracker.get_latest_entity_values("electronic_money", "to"), None) != None or next(tracker.get_latest_entity_values("cash", "to"), None) != None or next(tracker.get_latest_entity_values("telephone_number", "to"), None) != None or next(tracker.get_latest_entity_values("guarant", "to"), None) != None:
                return {"transfer_direction": "withdraw"}
            else:
                return {"transfer_direction": "exchange"}



        elif next(tracker.get_latest_entity_values("bank_card", "from"), None) or next(tracker.get_latest_entity_values("bank", "from"), None) or next(tracker.get_latest_entity_values("electronic_money", "from"), None) or next(tracker.get_latest_entity_values("cash", "from"), None) or next(tracker.get_latest_entity_values("telephone_number", "from"), None) or next(tracker.get_latest_entity_values("guarant", "from"), None) != None:
            return {"transfer_direction": "topup"}

        elif next(tracker.get_latest_entity_values("bank_card", "to"), None) or next(tracker.get_latest_entity_values("bank", "to"), None) or next(tracker.get_latest_entity_values("electronic_money", "to"), None) or next(tracker.get_latest_entity_values("cash", "to"), None) or next(tracker.get_latest_entity_values("telephone_number", "to"), None) or next(tracker.get_latest_entity_values("guarant", "to"), None) != None:
            return {"transfer_direction": "withdraw"}

        elif next(tracker.get_latest_entity_values("cash"), None) != None:
            return {"transfer_direction": "withdraw"}


        elif tracker.latest_message["intent"].get("name") == "transfer.transfer" and next(tracker.get_latest_entity_values("verb"), None) == None and next(tracker.get_latest_entity_values("bank_card"), None) == None and next(tracker.get_latest_entity_values("bank"), None) == None and next(tracker.get_latest_entity_values("electronic_money"), None) == None and next(tracker.get_latest_entity_values("cash"), None) == None and next(tracker.get_latest_entity_values("telephone_number"), None) == None and next(tracker.get_latest_entity_values("guarant"), None) == None:
            return {"transfer_direction": "transfer"}

        elif tracker.latest_message["intent"].get("name") == "transfer.transfer" and next(tracker.get_latest_entity_values("name", "to"), None) or next(tracker.get_latest_entity_values("name", "from"), None) != None:
            return {"transfer_direction": "transfer"}








    async def extract_transfer_purse_type(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:
        transfer_purse_type = next(tracker.get_latest_entity_values("purse_type"), None) or next(tracker.get_latest_entity_values("purse_type", "to"), None) or next(tracker.get_latest_entity_values("purse_type", "from"), None)
        if transfer_purse_type != None:
            return {"transfer_purse_type": transfer_purse_type}


    async def extract_transfer_method(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:

        if next(tracker.get_latest_entity_values("bank_card"), None) or next(tracker.get_latest_entity_values("bank_card", "to"), None) or next(tracker.get_latest_entity_values("bank_card", "from"), None) or next(tracker.get_latest_entity_values("bank_card", "through"), None) or next(tracker.get_latest_entity_values("bank"), None) or next(tracker.get_latest_entity_values("bank", "to"), None) or next(tracker.get_latest_entity_values("bank", "from"), None) or next(tracker.get_latest_entity_values("bank", "through"), None) != None:
            return {"transfer_method": "transfer_bank"}

        elif next(tracker.get_latest_entity_values("electronic_money"), None) or next(tracker.get_latest_entity_values("electronic_money", "to"), None) or next(tracker.get_latest_entity_values("electronic_money", "from"), None) or next(tracker.get_latest_entity_values("electronic_money", "through"), None) != None:
            return {"transfer_method": "transfer_electronic_money"}

        elif next(tracker.get_latest_entity_values("cash"), None) or next(tracker.get_latest_entity_values("cash", "to"), None) or next(tracker.get_latest_entity_values("cash", "from"), None) or next(tracker.get_latest_entity_values("cash", "through"), None) != None:
            return {"transfer_method": "transfer_cash"}

        elif next(tracker.get_latest_entity_values("telephone_number"), None) or next(tracker.get_latest_entity_values("telephone_number", "to"), None) or next(tracker.get_latest_entity_values("telephone_number", "from"), None) or next(tracker.get_latest_entity_values("telephone_number", "through"), None) != None:
            return {"transfer_method": "transfer_telephone_number"}

        elif next(tracker.get_latest_entity_values("guarant"), None) or next(tracker.get_latest_entity_values("guarant", "to"), None) or next(tracker.get_latest_entity_values("guarant", "from"), None) or next(tracker.get_latest_entity_values("guarant", "through"), None) != None:
            return {"transfer_method": "transfer_guarant"}


    def validate_transfer_direction(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        if slot_value in {"topup", "withdraw", "exchange", "transfer"}:
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
                    # dispatcher.utter_message("-1")
                    return {"transfer_purse_type": slot_value, "transfer_method": None}
            
            elif transfer_method == "transfer_guarant":
                if slot_value in {"wmy", "wmz", "wme", "wmb", "wmk"}:
                    dispatcher.utter_message(response="utter_this_method_is_not_possible")
                    # dispatcher.utter_message("-1")
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
                # dispatcher.utter_message("0")
                return {"transfer_method": None}


        elif transfer_purse_type in {"wmx", "wmf", "wmh", "wml", "wmt", "btc", "bch", "ltc", "eth", "usdt"}:

            if latest_intent_name == "transfer.electronic_money" or slot_value == "transfer_electronic_money":
                return {"transfer_method": 'transfer_electronic_money'}

            elif latest_intent_name == "transfer.guarant" or slot_value == "transfer_guarant":
                return {"transfer_method": 'transfer_guarant'}

            else:
                dispatcher.utter_message(response="utter_this_method_is_not_possible")
                # dispatcher.utter_message("1")
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
                # dispatcher.utter_message("2")
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
                # dispatcher.utter_message("3")
                return {"transfer_method": None}


        elif transfer_purse_type == "wmy":

            if latest_intent_name in {"transfer.banks", "transfer.bank_card"} or slot_value == "transfer_bank":
                return {"transfer_method": 'transfer_bank'}
            else:
                dispatcher.utter_message(response="utter_this_method_is_not_possible")
                # dispatcher.utter_message("4")
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



class ActionAskTransferFormTransferTransferDirection(Action):
    def name(self) -> Text:
        return "action_ask_transfer_form_transfer_direction"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message("Что именно Вы хотите сделать?")
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
        transfer_direction = tracker.get_slot("transfer_direction")
        transfer_purse_type = tracker.get_slot("transfer_purse_type")
        transfer_method = tracker.get_slot("transfer_method")
        fee = tracker.get_slot("fee")
        protected_payment = tracker.get_slot("protected_payment")


        purse_type = next(tracker.get_latest_entity_values("purse_type"), None)
        purse_type_from = next(tracker.get_latest_entity_values("purse_type", entity_role = "from"), None)
        purse_type_to = next(tracker.get_latest_entity_values("purse_type", entity_role = "to"), None)

        if purse_type != None and purse_type_from == None:
            purse_type_from = purse_type
            purse_type = None

        if transfer_direction == "exchange":
            if fee == None:
                if purse_type_from == "wmp" or purse_type_to == "wmp":
                    dispatcher.utter_message(response="utter_transfer_form_exchange_wmp") 

                elif purse_type_from == "wmr" or purse_type_to == "wmr":
                        dispatcher.utter_message(response="utter_transfer_form_exchange_wmr")

                elif purse_type_from == "wmu" or purse_type_to == "wmu":
                        dispatcher.utter_message(response="utter_transfer_form_exchange_wmu")

                elif purse_type_from == "wmc" or purse_type_to == "wmc":
                        dispatcher.utter_message(response="utter_transfer_form_exchange_wmc")

                elif purse_type_from == "wmd" or purse_type_to == "wmd":
                        dispatcher.utter_message(response="utter_transfer_form_exchange_wmd")

                elif purse_type_from == "mdl" or purse_type_to == "mdl":
                        dispatcher.utter_message(response="utter_transfer_form_exchange_mdl")

                else:
                    # dispatcher.utter_message("1")
                    dispatcher.utter_message(response="utter_transfer.exchange")

            elif fee != None:

                if purse_type_from == "wmp" or purse_type_to == "wmp":
                    dispatcher.utter_message(response="utter_transfer_form_wmp")

                elif purse_type_from == "wmr" or purse_type_to == "wmr":
                        dispatcher.utter_message(response="utter_transfer_form_wmr")

                elif purse_type_from == "wmu" or purse_type_to == "wmu":
                        dispatcher.utter_message(response="utter_transfer_form_wmu")

                elif purse_type_from == "wmc" or purse_type_to == "wmc":
                        dispatcher.utter_message(response="utter_transfer_form_wmc")

                elif purse_type_from == "wmd" or purse_type_to == "wmd":
                        dispatcher.utter_message(response="utter_transfer_form_wmd")

                elif purse_type_from == "mdl" or purse_type_to == "mdl":
                        dispatcher.utter_message(response="utter_transfer_form_mdl")

                else:
                    # dispatcher.utter_message("2")
                    dispatcher.utter_message(response="utter_transfer.exchange_min_fee")


        elif transfer_direction == "transfer":
            if purse_type_from == "wmp" or purse_type_to == "wmp":
                    dispatcher.utter_message(response="utter_transfer_form_wmp")

            elif purse_type_from == "wmr" or purse_type_to == "wmr":
                    dispatcher.utter_message(response="utter_transfer_form_wmr")

            elif purse_type_from == "wmu" or purse_type_to == "wmu":
                    dispatcher.utter_message(response="utter_transfer_form_wmu")

            elif purse_type_from == "wmc" or purse_type_to == "wmc":
                    dispatcher.utter_message(response="utter_transfer_form_wmc")

            elif purse_type_from == "wmd" or purse_type_to == "wmd":
                    dispatcher.utter_message(response="utter_transfer_form_wmd")

            elif purse_type_from == "mdl" or purse_type_to == "mdl":
                    dispatcher.utter_message(response="utter_transfer_form_mdl")

            else:
                if purse_type_from != None and purse_type_to != None and purse_type_from != purse_type_to:
                    if fee != None:
                        # dispatcher.utter_message("3")
                        dispatcher.utter_message(response="utter_transfer_form_None_None_None_min_fee")

                    elif protected_payment != None:
                        dispatcher.utter_message(response="utter_transfer_form_None_None_None_with_protected_payment")

                    else:
                        # dispatcher.utter_message("4")
                        dispatcher.utter_message(response="utter_transfer_form_transfer_after_exchange")


                elif purse_type_from != None and purse_type_to != None and purse_type_from == purse_type_to:
                    if fee != None:
                        # dispatcher.utter_message("5")
                        dispatcher.utter_message(response="utter_transfer.exchange_min_fee")
                    
                    elif protected_payment != None:
                        dispatcher.utter_message(response="utter_transfer_form_None_None_None_with_protected_payment")

                    else:
                        # dispatcher.utter_message("6")
                        dispatcher.utter_message(response="utter_transfer.exchange")

                else:
                    if fee != None:
                        # dispatcher.utter_message("7")
                        dispatcher.utter_message(response="utter_transfer_form_None_None_None_min_fee")

                    elif protected_payment != None:
                        dispatcher.utter_message(response="utter_transfer_form_None_None_None_with_protected_payment")

                    else:
                        # dispatcher.utter_message("8")
                        dispatcher.utter_message(response="utter_transfer_form_None_None_None")
                

        else:
            if fee != None:
                # dispatcher.utter_message("9")
                # dispatcher.utter_message(response=f"utter_transfer_form_{transfer_direction}_{transfer_purse_type}_{transfer_method}_min_fee")
                dispatcher.utter_message(response=f"utter_transfer_form_{transfer_direction}_{transfer_purse_type}_min_fee")

            else:
                # dispatcher.utter_message("10")
                dispatcher.utter_message(response=f"utter_transfer_form_{transfer_direction}_{transfer_purse_type}_{transfer_method}")

        return [SlotSet("fee", None), SlotSet("protected_payment", None), SlotSet("transfer_method", None)]



class Action(Action):
    def name(self) -> Text:
        return "action_slots_restart"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        return [SlotSet("transfer_direction", None), SlotSet("transfer_purse_type", None), SlotSet("transfer_method", None), SlotSet("verb", None) ]



class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # dispatcher.utter_message(response="utter_session_start")
        dispatcher.utter_message("сессия старт!")
        return [SessionStarted(), ActionExecuted("action_listen")]
