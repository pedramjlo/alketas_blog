import axios from 'axios';
import Cookies from 'js-cookie';

// Get CSRF token from the cookie
const csrfToken = Cookies.get('csrftoken');

// Configure Axios to include the CSRF token in the headers for all requests
axios.defaults.headers.common['X-CSRFToken'] = csrfToken;

