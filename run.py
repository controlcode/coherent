import os
from coherent.application import app

PORT = os.getenv('PORT', 5052)
app.run(debug=True, host='0.0.0.0', port=int(PORT))
