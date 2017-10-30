class TripManager(models.Manager):
    def validator(self, destination, description, start_date, end_date):
        errors = []
        if len(destination < 1:
            errors.append("Destination Can't Be Blank!"
        if len(description) < 1:
            error.append("Description Can't Be Blank!")
        if len(start_date) < 1:
            errors.append("Start Date Can't Be Blank!")
        if len(end_date) < 1:
            errors.append("End Date Can't Be Blank...you gotta come back!")
        if start_date > end_date:
            errors.append("Start Date has to come BEFORE End Date!")
        
        if len(errors) > 0:
            return (False, errors)

        request.session['name'] = User.userManager.get(name=request.POST['name'])
        request.session['user_id'] = User.userManager.get(name=request.POST['name']).id