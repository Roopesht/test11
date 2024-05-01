from flask_sqlalchemy import SQLAlchemy

# Assuming you have already initialized your Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the database connection object
db = SQLAlchemy(app)

# Model class for the provisioning_req_history table
class ProvisioningReqHistory(db.Model):
    __tablename__ = 'provisioning_req_history'

    provision_req_history_id = db.Column(db.BigInteger, primary_key=True)
    provision_request_id = db.Column(db.BigInteger, nullable=False)
    app_env_id = db.Column(db.BigInteger, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    task_id = db.Column(db.String)
    comp_type_master_id = db.Column(db.BigInteger)
    values_json = db.Column(db.JSON)
    terraform_json = db.Column(db.JSON)
    output_json = db.Column(db.JSON)
    provision_status_master_id = db.Column(db.BigInteger)
    created_by = db.Column(db.String)
    created_timestamp = db.Column(db.TIMESTAMP)
    updated_by = db.Column(db.String)
    updated_timestamp = db.Column(db.TIMESTAMP)
    sn_ticket_number = db.Column(db.String)
    sn_state = db.Column(db.String)
    product_type_master_id = db.Column(db.BigInteger)
    revised_input_json = db.Column(db.JSON)
