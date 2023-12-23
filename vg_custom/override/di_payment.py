import frappe
# path - vg_custom.override.di_payment.di_payment_request_form

def di_payment_request_form(doc,method=None):
    if doc.workflow_state == "Pending from Accounts":
        account_action_doc = frappe.get_doc({
                'doctype': 'ToDo',
                'allocated_to':"avnimistry01@gmail.com",
                'description': doc.message,
                'reference_name': doc.name,
                'reference_type': 'DI Payment Request Form',
            })
        account_action_doc.insert()
    if doc.workflow_state == "pending from HO":
            ho_action_doc = frappe.get_doc({
                'doctype': 'ToDo',
                'allocated_to':"12345.samir@gmail.com",
                'description': doc.message,
                'reference_name': doc.name,
                'reference_type': 'DI Payment Request Form',
            })
            ho_action_doc.insert()
    if doc.workflow_state == "Payment Pending":
            paymet_action_doc = frappe.get_doc({
                'doctype': 'ToDo',
                'allocated_to':"avnimistry01@gmail.com",
                'description': doc.message,
                'reference_name': doc.name,
                'reference_type': 'DI Payment Request Form',
            })
            paymet_action_doc.insert()
        # if doc.workflow_state == "Payment Done":
        #     paymet_action_doc = frappe.get_doc({
        #         'doctype': 'ToDo',
        #         'allocated_to':"12345.samir@gmail.com",
        #         'description': doc.message,
        #         'reference_name': doc.name,
        #         'reference_type': 'DI Payment Request Form',
        #     })
        # paymet_action_doc.insert()