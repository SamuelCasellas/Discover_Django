from datetime import datetime

from django.shortcuts import render
from django.http import Http404

from .models import ToDo, SingleInstruction

# Create your views here.

# Showcase all of the to-dos here in a list
def index(request):
    """The todo_id does not come from the url,
    rather, if the steps view finds that all
    of the steps have been completed and marks
    the to-do as completed.
    """
    try:
        todos = ToDo.objects.all()
        # Check if there is a task that was completed
        todo_completed_id = request.POST.get("task-complete", default=None)

        if todo_completed_id is not None: 

            task_name = ToDo.objects.get(pk=todo_completed_id).todo_description

            # Delete the task form database
            ToDo.objects.filter(pk=todo_completed_id).delete()

            context = {
                "todos": todos, 
                "task_completed": True, 
                "completed_task": task_name
            }

        else:
            context = {
                "todos": todos
            }
        return render(request, "todo/index.html", context=context)
    except ToDo.DoesNotExist:
        raise Http404("Object \"ToDo\" does not exist.")

def add_todo(request):
    context = {}
    new_todo_text = request.POST.get("to-do", default=None)
    if new_todo_text is not None:
        datetime_conversion = request.POST.get("time")
        try:
            datetime_conversion = datetime.strptime(datetime_conversion, '%b %d %Y %I:%M %p')

        except ValueError:
            # The context to display an error on the page for invalid time format
            context = {"time_formatting_error": True}
            return render(request, "todo/add_todo.html", context=context)
        
        new_todo = ToDo(
        todo_description = new_todo_text,
        scheduled_time = datetime_conversion
        )

        steps = list()
        for i in range(1,11):
            step_text = request.POST.get("step{}".format(i), None)
            if step_text is not None:
                steps.append(SingleInstruction(
                    todo=new_todo,
                    instruction_step=step_text,
                    step_number=i
                ))

        # Save to the database
        new_todo.save()
        for step in steps:
            step.save()

        # Print success screen to user
        context = {"item_saved": True, 
        "item": new_todo.todo_description}


    return render(request, "todo/add_todo.html", context=context)

def steps(request, todo_id):

    # Check if a step has been complete
    step_completed_id = request.POST.get("step-complete", default=None)
    if step_completed_id is not None:
        
        # Delete the step from the database
        SingleInstruction.objects.filter(pk=step_completed_id).delete()

    associated_todo = ToDo.objects.get(pk=todo_id)

    associated_steps = SingleInstruction.objects.filter(
        todo=associated_todo
    )
    context = {
        "todo": associated_todo,
        "steps": associated_steps
    }

    return render(request, "todo/steps.html", context=context)
            