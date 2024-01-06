import frappe
from frappe.utils import now, date_diff, time_diff_in_hours
from datetime import datetime
 
# path - vg_custom.override.di_payment.di_payment_request_form 

def di_payment_request_form(doc,method=None):
	if doc.workflow_state == "Pending from Accounts":
		create_todo(doc, "accountant", doc.accounts_approval)
	elif doc.workflow_state == "pending from HO":
		closing_todo(doc)
		create_todo(doc, "head_office",doc.ho_approval)
	elif doc.workflow_state == "Payment Pending":
		closing_todo(doc)
		create_todo(doc, "accountant",doc.transaction_date)
	elif doc.workflow_state == "Payment Done":
		closing_todo(doc)
def create_todo(doc, role, due_date):
	todo_doc = frappe.get_doc({
		'doctype': 'ToDo',
		'allocated_to':frappe.db.get_single_value('Di Payments settings', role),
		'description': doc.title_short_description +'-'+ doc.workflow_state,
		'reference_name': doc.name,
		'reference_type': 'DI Payment Request Form',
		'date': due_date
	})
	todo_doc.insert()
	frappe.db.set_value('DI Payment Request Form',doc.name,'todo_reference', todo_doc.name)
def closing_todo(doc): 
	frappe.db.set_value('ToDo', doc.todo_reference, {
    'status': 'Closed',
    'custom_completion_date': now(),
	'custom_days_duration':date_diff(now(), frappe.get_value('ToDo',doc.todo_reference,'date')) 
	})
	
	