# api_training
## API Architecture:
|Functionality|Recommended RESTful Path|HTTP Method|Notes for Training Assignment|Status|
|-------------|------------------------|-----------|-----------------------------|------|
|Create Profile|/profiles|POST|Use status_code=200 (Created) on success.| Done |
|View Profile|/profile|GET|Use a Dependency to fetch the authenticated user's profile.| Done |
|Create Reservation|/reservations|POST|Must be Idempotent to prevent double-booking upon retry.| Done |
|View ALL Reservations|/reservations|GET|Mandatory: Must implement Pagination (e.g., ?limit=10&offset=0).| Done |
|View SINGLE Reservation|/reservations/{date}|GET|Use Path Parameters to identify a unique reservation.|  |
|Update Reservation|/reservations/{date}|PUT or PATCH|Use Path Parameters to identify the resource. PUT for complete replacement, PATCH for partial update.|  |
|Cancel Reservation|/reservations/{date}|DELETE|Use status_code=204 (No Content) on success.|  |
|Check Profile Status|/profile-check/{phone_number}|GET|Use a separate endpoint to satisfy the requirement to "Check if the user has an account or not first - using Phone Number and Name".|  |

## Recommended Additions
The following elements should be added:
* **Pydantic Models for Data Schemas:** Developers should use Pydantic to strictly define the Profile and Reservation data structures for both requests and responses.
  * **Data Validation:** The Profile model should enforce the rule that Age is "always greater than 21 years old" using Pydantic's validators.
  * **Response Models:** Define explicit Response Models for all GET and POST operations to control the data returned and enhance automatic OpenAPI documentation.
* **Structured Error Handling:** Define a consistent, custom exception handler (e.g., for 404 Not Found or 400 Bad Request) to ensure all API services return error messages in the same structured format.
* **Enum Usage (optional):** Developers should be required to use a Python Enum with Pydantic for fields with restricted values, such as Occasion (e.g., "Birthday," "Anniversary," "Other"), for strong typing.

## Params for API
* Profile Creation
  * Full Name
  * Phone Number
  * Email
  * Postal Code
  * Age (always greater than 21 years old)
* Profile Fetch (Any of 1)
  * Email
  * Phone Number
* Create Reservation
  * Name
  * Phone Number
  * Number of guests
  * Occasion (optional)
  * Date
  * Time
* Cancel Reservation
  * Name
  * Date (optional)
* View Reservation
  * Name
  * Date (optional)
* Update Reservation
  * Name
  * Date
  * Time
  * Number of Guests (optional)
