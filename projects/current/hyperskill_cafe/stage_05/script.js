document.getElementById("reviewButton").addEventListener("click", function (event) {
  event.preventDefault();

  addReview()
})


function addReview() {
  // Get review Form element.
  let reviewForm = document.forms.namedItem("reviewForm")
  // Get the review Forms input fields.
  let reviewTitle = reviewForm.elements.namedItem("reviewTitle")
  let reviewText = reviewForm.elements.namedItem("reviewText")
  let reviewName = reviewForm.elements.namedItem("reviewName")
  // Get the values of the review Forms input fields
  let reviewTitleValue = reviewTitle.value
  let reviewTextValue = reviewText.value
  let reviewNameValue = reviewName.value
  // Set reviewer name to "Anonymous" if reviewName is empty.
  if (reviewNameValue === "") {
    reviewNameValue = "Anonymous"
  }
  // Get the reviews Row element.
  let reviewsRow = document.getElementById("reviewsRow")
  // Append a deep clone of the first child element of the reviews Row to it's end
  // to be used as a base template for the new review.
  let reviewClone = reviewsRow.firstElementChild.cloneNode(true)
  reviewsRow.appendChild(reviewClone)
  // Get the child elements of the new review that need to be adjusted.
  // Avoid having to go through the sub-container <div> elements by using querySelector to find
  // the elements that contain the text that needs to be adjusted.
  // Title is in the <h4/> element.
  let newReviewTitle = reviewClone.querySelector("h4")
  // Text is in the <p/> element inside the <blockquoute/> element.
  let newReviewText = reviewClone.querySelector("p")  // Text is in the <p/> element.
  // Name is in the <I/> element inside the <footer/> element inside the <blockquoute/> element.
  let newReviewName = reviewClone.querySelector("I")  // Name is in <I/> in
  // Adjust the values of the child elements of the new review.
  newReviewTitle.textContent = reviewTitleValue
  newReviewText.textContent = reviewTextValue
  newReviewName.textContent = reviewNameValue

  // test/debug
  // console.log(newReviewTitle.textContent)
}