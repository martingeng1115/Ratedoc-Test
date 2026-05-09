import pytest
import requests
import time
from playwright.sync_api import Page, expect

BASE_URL = "http://159.89.231.16:3000"
API_URL = f"{BASE_URL}/api/v1"

@pytest.fixture
def test_department():

    unique_id = str(int(time.time()))
    dept_name = f"QA Dept {unique_id}"
    
    res = requests.post(f"{API_URL}/departments", json={"name": dept_name})
    dept_id = res.json().get("id")
    
    yield dept_name 
    
    if dept_id:
        requests.delete(f"{API_URL}/departments/{dept_id}")

@pytest.fixture
def test_hospital():

    unique_id = str(int(time.time()))
    hosp_name = f"QA Hospital {unique_id}"
    
    res = requests.post(f"{API_URL}/hospitals", json={"name": hosp_name})
    hosp_id = res.json().get("id")
    
    yield hosp_name
    
    if hosp_id:
        requests.delete(f"{API_URL}/hospitals/{hosp_id}")

@pytest.fixture
def pending_doctor():
 
    unique_id = str(int(time.time()))
    doctor_data = {"name": f"Dr. QA {unique_id}", "status": "pending"}
    
    res = requests.post(f"{API_URL}/doctors", json=doctor_data)
    doctor_slug = res.json().get("slug")
    
    yield doctor_data["name"]
    
    if doctor_slug:
        requests.delete(f"{API_URL}/doctors/{doctor_slug}")



def test_suggest_departments_ui(page: Page, test_department):
  
    page.goto(BASE_URL)
    

    search_input = page.locator("input[placeholder='Search departments...']")
    search_input.fill(test_department)
    

    suggestion_item = page.locator(f"text={test_department}")
    expect(suggestion_item).to_be_visible(timeout=5000)

def test_list_hospitals_ui(page: Page, test_hospital):

    page.goto(f"{BASE_URL}/hospitals")
    
 
    hospital_card = page.locator(f"text={test_hospital}")
    expect(hospital_card).to_be_visible(timeout=5000)

def test_admin_approve_doctor_ui(page: Page, pending_doctor):

    page.goto(f"{BASE_URL}/admin/doctors")
    

    doctor_row = page.locator(f"tr:has-text('{pending_doctor}')")
    
 
    approve_button = doctor_row.locator("button:has-text('Approve')")
    approve_button.click()
   
    approved_badge = doctor_row.locator("span:has-text('Approved')")
    expect(approved_badge).to_be_visible(timeout=5000)