from django import forms


class SalaryValidationMixin:
    MAX_SALARY = None

    def clean_salary(self):
        salary = self.cleaned_data.get("salary")

        if salary and self.MAX_SALARY:
            if salary > self.MAX_SALARY:
                raise forms.ValidationError(
                    f"Salary cannot exceed ${self.MAX_SALARY:,.0f}"
                )

        return salary