import requests
import json
import time

API_BASE_URL = "http://api:5000/api"

def wait_for_api():
    """Wait for API to be ready"""
    max_retries = 30
    for i in range(max_retries):
        try:
            response = requests.get(f"{API_BASE_URL}/health")
            if response.status_code == 200:
                print("✅ API is ready!")
                return True
        except requests.exceptions.RequestException:
            pass
        
        print(f"⏳ Waiting for API... ({i+1}/{max_retries})")
        time.sleep(2)
    
    print("❌ API not available")
    return False

def create_task(title, description="", completed=False):
    """Create a new task"""
    data = {
        "title": title,
        "description": description,
        "completed": completed
    }
    
    response = requests.post(f"{API_BASE_URL}/tasks", json=data)
    print(f"CREATE Task - Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    return response.json()

def get_all_tasks():
    """Get all tasks"""
    response = requests.get(f"{API_BASE_URL}/tasks")
    print(f"GET All Tasks - Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    return response.json()

def get_task(task_id):
    """Get specific task"""
    response = requests.get(f"{API_BASE_URL}/tasks/{task_id}")
    print(f"GET Task {task_id} - Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    return response.json()

def update_task(task_id, **kwargs):
    """Update a task"""
    response = requests.put(f"{API_BASE_URL}/tasks/{task_id}", json=kwargs)
    print(f"UPDATE Task {task_id} - Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    return response.json()

def delete_task(task_id):
    """Delete a task"""
    response = requests.delete(f"{API_BASE_URL}/tasks/{task_id}")
    print(f"DELETE Task {task_id} - Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    return response.json()

def main():
    """Demo script showing all REST operations"""
    if not wait_for_api():
        return
    
    print("\n" + "="*50)
    print("TASK MANAGEMENT API DEMO")
    print("="*50)
    
    # Create some tasks
    print("\n1. Creating tasks...")
    task1 = create_task("Learn Docker", "Complete Docker tutorial")
    task2 = create_task("Build REST API", "Create Flask API with CRUD operations")
    task3 = create_task("Write documentation", "Document the API endpoints")
    
    print("\n2. Getting all tasks...")
    get_all_tasks()
    
    print("\n3. Getting specific task...")
    get_task(1)
    
    print("\n4. Updating task...")
    update_task(1, completed=True, description="Docker tutorial completed!")
    
    print("\n5. Getting updated task...")
    get_task(1)
    
    print("\n6. Deleting task...")
    delete_task(3)
    
    print("\n7. Final tasks list...")
    get_all_tasks()
    
    print("\n✅ Demo completed!")

if __name__ == "__main__":
    main()
