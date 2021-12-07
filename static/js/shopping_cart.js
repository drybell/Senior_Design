const add = (event) => { 
	let id = event.target.id.split("_")[1];
	let target_id = document.getElementById("q_" + id);
	let target_val = Number(target_id.innerText);
	let price_elem = document.getElementById("price_" + id);
	let price = Number(document.getElementById("indprice_" + id).innerText.split(' ')[1]);
	target_id.innerText = String(target_val + 1);
	price_elem.innerText = "$ " + String(price * (target_val + 1));
	document.getElementById('update_' + id).hidden = false;
}

const subtract = (event) => { 
	let id = event.target.id.split("_")[1];
	let target_id  = document.getElementById("q_" + id);
	let target_val = Number(target_id.innerText);

	let price_elem = document.getElementById("price_" + id);
	let price = Number(document.getElementById("indprice_" + id).innerText.split(' ')[1]);
	if (target_val !== 0) {
		target_id.innerText  = String(target_val - 1);
		price_elem.innerText = "$ " + String(price * (target_val - 1));
	}
	document.getElementById('update_' + id).hidden = false;
}

const checkout_page = (event) => {

	document.location.href = "/checkout"; 
}

const update = (event) => {
	let id = event.target.id.split('_')[1];
	let new_quantity = Number(document.getElementById('q_' + id).innerText);
	let button = document.getElementById('update_' + id);
	$.post({
		type: "POST",
		url: "/update/item",
		contentType: "application/json",
		data: JSON.stringify({'name': id, 'quantity': new_quantity}),
		success: function(res) { 
			button.hidden = true;
		}
	})
}

const remove = (event) => { 
	let id = event.target.id.split("_")[1];

	$.post({
		type: "POST",
		url: "/remove/item",
		contentType: "application/json",
		data: JSON.stringify({'name': id}),
		success: function(res) { 
			let item_container = document.getElementById("container_" + id);
			let content = document.getElementById("content");
			content.removeChild(item_container);

			if (content.children.length === 3) { 
				while (content.firstChild) {
					content.removeChild(content.firstChild);
				}

				let header    = document.createElement('h2');
				header.innerText = "Your Shopping Cart";

				let empty = document.createElement("p");
				empty.setAttribute('class', 'empty_message');
				empty.innerText = "Looks like your shopping cart is empty.";
				content.appendChild(header);
				content.appendChild(empty);
				}
		}
	})
}

const removeall = (event) => { 
	$.post({
		type: "POST",
		url: "/remove/all",
		contentType: "application/json",
		data: JSON.stringify({'msg': 'remove'}),
		success: function(res) { 
			let content = document.getElementById("content");

			while (content.firstChild) {
				content.removeChild(content.firstChild);
			}

			let header    = document.createElement('h2');
			header.innerText = "Your Shopping Cart";

			let empty = document.createElement("p");
			empty.setAttribute('class', 'empty_message');
			empty.innerText = "Looks like your shopping cart is empty.";
			content.appendChild(header);
			content.appendChild(empty);
		}
	})
}

const postData = (data) => { 
	let container = document.getElementById('content');
	let header    = document.createElement('h2');
	header.innerText = "Your Shopping Cart";

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
		for (let i = 0; i < keys.length; i ++) { 
			let key   = keys[i];
			let dict  = data[key];
			let quantity_ = dict.length;
			if (quantity_ > 0) { 
				let name  = dict[0]['name'];
				let image_name = '/static/images/' + name + '.png';
				let price_ = dict[0]['price'];
				let total_price = price_ * quantity_;

				let item_div = document.createElement('div');
				item_div.setAttribute('class', "item_container");
				item_div.setAttribute('id', 'container_' + name);

				let modify_div = document.createElement('div');
				modify_div.setAttribute('class', 'quantity_container');

				let item_name = document.createElement('h3');
				item_name.setAttribute('class', 'item_cart');
				item_name.innerText = name;

				let price_name = document.createElement('p');
				price_name.setAttribute('class', 'item_header');
				price_name.innerText = "Total Price";

				let price  = document.createElement('p');
				price.setAttribute('id', "price_" + name);
				price.setAttribute('class', 'price');
				price.innerText = "$ " + total_price;

				let ind_price_name = document.createElement('p');
				ind_price_name.setAttribute('class', 'item_header');
				ind_price_name.innerText = "Price per Item";

				let ind_price = document.createElement('p');
				ind_price.setAttribute('id', 'indprice_' + name);
				ind_price.setAttribute('class', 'indprice');
				ind_price.innerText = "$ " + price_;

				let image = document.createElement('img');
				image.setAttribute('src', image_name);
				image.setAttribute('width', '50vw');
				image.setAttribute('height', '50vw');
				image.setAttribute('class', 'item_image');

				let add_button = document.createElement('button');
				add_button.setAttribute("id", "add_" + name);
				add_button.setAttribute("class", "modify_button");
				add_button.innerHTML = "+";
				add_button.addEventListener('click', add);

				let quantity  = document.createElement('p');
				quantity.setAttribute("id", "q_" + name);
				quantity.setAttribute("class", "quantity");
				quantity.innerText = quantity_;

				let minus_button = document.createElement('button');
				minus_button.setAttribute("id", "minus_" + name);
				minus_button.setAttribute("class", "modify_button");
				minus_button.innerHTML = "-";
				minus_button.addEventListener('click', subtract);

				let update_button = document.createElement('button');
				update_button.setAttribute('id', 'update_' + name);
				update_button.setAttribute('class', 'update_button');
				update_button.addEventListener('click', update);
				update_button.innerHTML = "Update Item";
				update_button.hidden = true;

				let remove_button = document.createElement('button');
				remove_button.setAttribute('id', 'remove_' + name);
				remove_button.setAttribute('class', 'remove_button');
				remove_button.innerHTML = "Remove This Item";
				remove_button.addEventListener('click', remove);
				item_div.appendChild(item_name);
				item_div.appendChild(price_name);
				item_div.appendChild(price);
				item_div.appendChild(ind_price_name);
				item_div.appendChild(ind_price);
				item_div.appendChild(image);

				modify_div.appendChild(minus_button);
				modify_div.appendChild(quantity);
				modify_div.appendChild(add_button);
				modify_div.appendChild(update_button)
				modify_div.appendChild(remove_button);

				item_div.appendChild(modify_div)
				container.appendChild(item_div);
			}
		}

		let remove_all = document.createElement('button');
		remove_all.setAttribute('id', 'removeall');
		remove_all.setAttribute('class', 'remove_all_button');
		remove_all.innerHTML = "Remove All Items";
		remove_all.addEventListener('click', removeall);

		let checkout = document.createElement('button');
		checkout.setAttribute('id', 'checkout_');
		checkout.setAttribute('class', 'checkout_button');
		checkout.innerHTML = "Checkout!";
		checkout.addEventListener('click', checkout_page);

		container.appendChild(checkout);
		container.appendChild(remove_all);
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