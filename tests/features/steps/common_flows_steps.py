from behave import then

@then("the response status should be 201")
def step_impl(context):
    assert context.status == 201

@then("the response status should be 200")
def step_impl(context):
    assert context.status == 200

@then("the response status should be 204")
def step_impl(context):
    assert context.status == 204

@then("the response status should be one of:")
def step_impl(context):
    expected = {int(row.cells[0]) for row in context.table}
    assert context.status in expected

@then('the response body should contain "id"')
def step_impl(context):
    assert "id" in context.body

@then('the response body should not contain "id"')
def step_impl(context):
    assert "id" not in context.body

@then('the field "{field_name}" should equal saved "{var_name}"')
def step_impl(context, field_name, var_name):
    assert context.body.get(field_name) == getattr(context, var_name)