from app import app, api, db, ma, Resource, request, images_schema, image_schema, ImageData, json, jsonify

class AllImage(Resource):
    def get(self):
        images = ImageData.query.all()
        print(images)
        return images_schema.dump(images)
    def post(self):
        if 'image' in request.files:
            imagedata = request.files['image']
            imageD = imagedata.read()
        image = ImageData(
            uname = request.form['uname'],
            fname = request.form['fname'],
            lname = request.form['lname'],
            email = request.form['email'],
            image = imageD
        )
        db.session.add(image)
        db.session.commit()
        return image_schema.dump(image)
api.add_resource(AllImage,'/image/data')
