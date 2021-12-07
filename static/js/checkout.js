
const submit = (event) => { 
	let name = document.getElementById('name_input').value;
	$.post({
		type: "POST",
		url: "/save",
		contentType: 'application/json',
		data: JSON.stringify({"name": name}),
		success: function(res) {
			let content = document.getElementById('content');
			while (content.firstChild) {
				content.removeChild(content.firstChild);
			}
			let vending = document.createElement('h3');
			vending.innerText = "Vending..."; 
			content.appendChild(vending);
		}
	})
}

const postData = (data) => { 
	let container = document.getElementById('content');
	let header    = document.createElement('h2');
	header.innerText = "Cart Overview:";

	let keys = Object.keys(data); 
	let empty_test = keys.map(function (key) { 
		return data[key].length;
	});

	let is_empty = empty_test.every(e => e === 0);

	container.appendChild(header);

	if (is_empty) { 
		let empty = document.createElement("p");
		empty.setAttribute('class', 'empty_message');
		empty.innerText = "Looks like your shopping cart is empty.";
		container.appendChild(empty);
	}
	else {
		let summary_price = 0;
		for (let i = 0; i < keys.length; i ++) { 
			let key       = keys[i];
			let dict      = data[key];
			let quantity_ = dict.length;
			if (quantity_ > 0) { 
				let name   = dict[0]['name'];
				let price_ = dict[0]['price'];
				let total_price = quantity_ * price_;
				summary_price += total_price;

				let item_summary = document.createElement('p');
				item_summary.setAttribute('class', 'checkout_summary');
				item_summary.innerText = String(quantity_) + " " + name + ": $ " + String(total_price);
				container.appendChild(item_summary);
			}
		}
		let total_summary = document.createElement('p');
		total_summary.setAttribute('class', 'total_summary');
		total_summary.innerText = "Grand Total: $ " + String(summary_price);
		container.appendChild(total_summary);


		let name_header = document.createElement('h3');
		name_header.setAttribute('class', 'validate');
		name_header.innerText = "Please Enter Your Name:";

		let name_input = document.createElement('input');
		name_input.setAttribute('id', 'name_input');
		
		let name_submit = document.createElement('button');
		name_submit.setAttribute('class', 'submit');
		name_submit.addEventListener('click', submit);
		name_submit.innerHTML = "Checkout!"

		container.appendChild(name_header);
		container.appendChild(name_input);
		container.appendChild(name_submit);
	}
}

const getShoppingCart = () => {
	return new Promise(function (resolve, reject) { 
		$.get({
			type: "GET",
			url: "/get/items",
			success: function(res) { 
				resolve(res);
			},
			error: function(r, s, e) {
				reject(e);
			}
		})
	});
}

$(document).ready(function() { 
	getShoppingCart().then(function(data) {
		postData(data);
	});
});