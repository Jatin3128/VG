import frappe
# path - vg_custom.override.di_payment.di_payment_request_form

def di_payment_request_form(doc,method=None):
    if doc.workflow_state == "Pending from Accounts":
        qi_doc = frappe.get_doc({
                'doctype': 'Quality Inspection',
                'job_reference_number': self.reference_number,
                'service_reference_number': self.name,
                'inspection_details':inspection_item
            })
        qi_doc.insert()