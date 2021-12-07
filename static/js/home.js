

const add = (event) => { 
	let id = event.target.id.split("_")[1];
	let target_id = document.getElementById("q_" + id);
	let target_val = Number(target_id.innerText);
	target_id.innerText = String(target_val + 1);
}

const subtract = (event) => { 
	let id = event.target.id.split("_")[1];
	let target_id = document.getElementById("q_" + id);
	let target_val = Number(target_id.innerText);
	if (target_val !== 0) {
		target_id.innerText = String(target_val - 1);
	}
}

const add_to_cart = (event) => { 
	let id = event.target.id.split("_")[1];
	let add_div = document.getElementById('addcontainer_' + id);
	let target_id = document.getElementById("q_" + id);
	let quantity = Number(target_id.innerText);
	let price = Number(document.getElementById(id + "_price").innerText.split(' ')[1]);
	if (quantity > 0) {
		$.post({
			type: "POST",
			url: "/add/items",
			contentType: "application/json",
			data: JSON.stringify({"name": id, "quantity": quantity, "price": price}),
			success: function(res) {
				let added = document.createElement('p');
				added.setAttribute('class', 'added_to_cart');
				// added.innerText = "Added To Cart!";

				if (add_div.children.length === 1) { 
					add_div.appendChild(added);
				}
			}
		})
	}
}

const postData = (data) => { 
	let container = document.getElementById("content");
	let items = data['items'];

	for (let i = 0; i < items.length; i ++) { 
		let dict   = items[i];
		let name   = dict['name'];
		let price_  = dict['price'];
		let image_name = '/static/images/' + dict['name'] + '.png';

		let div_wrapper = document.createElement('div');
		div_wrapper.setAttribute('class', 'item_wrapper');

		let item_div = document.createElement('div');
		item_div.setAttribute('class', "item_container");

		let quantity_div = document.createElement('div');
		quantity_div.setAttribute('class', "quantity_container");

		let header = document.createElement('h3');
		header.setAttribute('id', name);
		header.setAttribute('class', 'item');
		header.innerText = name;

		let price  = document.createElement('p');
		price.setAttribute('id', name + "_price");
		price.setAttribute('class', 'price');
		price.innerText = "$ " + price_;

		let image = document.createElement('img');
		image.setAttribute('src', image_name);
		image.setAttribute('width', '100vw');
		image.setAttribute('height', '100vw')
		image.setAttribute('class', 'item_image');

		let add_button = document.createElement('button');
		add_button.setAttribute("id", "add_" + name);
		add_button.setAttribute("class", "modify_button");
		add_button.innerHTML = "+";
		add_button.addEventListener('click', add);

		let quantity  = document.createElement('p');
		quantity.setAttribute("id", "q_" + name);
		quantity.setAttribute("class", "quantity");
		quantity.innerText = "0";

		let minus_button = document.createElement('button');
		minus_button.setAttribute("id", "minus_" + name);
		minus_button.setAttribute("class", "modify_button");
		minus_button.innerHTML = "-";
		minus_button.addEventListener('click', subtract);

		let add_div = document.createElement('div');
		add_div.setAttribute('id', 'addcontainer_' + name);
		add_div.setAttribute('class', 'addcontainer');

		let add_item = document.createElement('button');
		add_item.setAttribute("id", "get_" + name);
		add_item.setAttribute("class", "add_to_cart");
		add_item.innerHTML = "Add To Cart!";
		add_item.addEventListener('click', add_to_cart);

		item_div.appendChild(header);
		item_div.appendChild(image);
		item_div.appendChild(price);

		quantity_div.appendChild(minus_button);
		quantity_div.appendChild(quantity);
		quantity_div.appendChild(add_button);

		div_wrapper.appendChild(item_div);
		div_wrapper.appendChild(quantity_div);
		add_div.appendChild(add_item);
		div_wrapper.appendChild(add_div);

		container.appendChild(div_wrapper);
	}
}

const getInventory = () => {
	return new Promise(function (resolve, reject) { 
		$.get({
			type: "GET",
			url: "/get/inventory",
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
	getInventory().then(function(data) {
		postData(data);
	});
});