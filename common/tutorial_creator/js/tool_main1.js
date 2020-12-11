"use strict";

// This array defines which page should load when the top navigation buttons are clicked
const nav_pages = [{ id: '#btn_home', html: 'home1.html' }];

let images_md = [], images_dir = [];

// document.ready function
$(() => {
    $('#lastmodified').text(document.lastModified); //sets the value for the last modified date in the HTML output
    $('.card-body').hide();

    //the actual image button is hidden. The actual image button is #image_files
    //the button that is displayed for image upload is #btn_image_files. When this button is clicked, the #image_files button click is triggered
    $('#main').on('change', '#image_files', readImageContent); //event listener for change image button
    $('#main').on('click', '#btn_image_files', () => {  //event to trigger the actual image upload button
        $('#image_files')[0].click();
    });

    $('#main').on('click', '#import_md', function () { //event listener for import MD
        $('#upload_md').click();
    });

    $('#main').on('change', '#upload_md', enterMdData); //event listener for upload MD
});

let loadFile = filename => { //function to load file
    let xhr = new XMLHttpRequest();
    xhr.open('GET', filename, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            $('#main').html(xhr.responseText);
        }
    }
    xhr.send();
}

let enterMdData = evt => {
    let files = evt.target.files;
    let file = files[0];
    let reader = new FileReader();
    let md;

    images_md = [];
    reader.onload = (function (theFile) {
        return function (e) {
            md = e.target.result;
        };
    })(file);
    reader.onloadend = function () {
        $('.card-body').hide();
        let imagesRegExp = new RegExp(/!\[.*?\]\((.*?)\)/g);
        let matches;

        do {
            matches = imagesRegExp.exec(md);
            if (matches !== null) 
                images_md.push(matches[1].substring(matches[1].lastIndexOf('/')).replace('/', '').split(' ')[0]);
        } while(matches);

        images_md = sort_unique(images_md);
        $('#import_md').text('[1 MD file with ' + images_md.length + ' image references uploaded for check]');
        $('#import_md').attr('title', "Click here to upload another MD file"); 
    
        checkDiff();
    }
    reader.readAsText(file);
}

//reads image content. Function is used for viewing images locally.
let readImageContent = (evt) => {
    let files = evt.target.files; // FileList object
    let uploaded_images = [];
    let total = 0, check = 0;
    $.each(files, function () {
        let file = $(this)[0];
        if (file.type.match('image.*')) {
            let reader = new FileReader();
            reader.onload = (function (theFile) {    
                $('.card-body').hide();                            
                return function (e) {
                    total++;
                    uploaded_images.push(escape(theFile.name));
                };
            })(file);            
                        
            reader.onloadend = function () {
                check++;                
                if (check == total) {                      
                    $('#btn_image_files').text('[' + uploaded_images.length + ' image(s) uploaded for check]');
                    $('#btn_image_files').attr('title', uploaded_images.join('\n') + "\n\nClick here to upload another image(s)"); 
                    images_dir = uploaded_images;       
                    checkDiff();                
                }
            };
            reader.readAsDataURL(file);
        }
    });
}

let checkDiff = () => {
    let missing = [], extra = [];

    if (images_md.length > 0 && images_dir.length > 0) {
        $(images_md).each(function() {
            let found = false;
            for (let i = 0; i < images_dir.length; i++) {
                if (this == images_dir[i]) {
                    found = true;
                    break;
                }
            }
            if(found == false) {
                missing.push(this);
            }
        });

        $(images_dir).each(function() {
            let found = false;
            for (let i = 0; i < images_md.length; i++) {
                if (this == images_md[i]) {
                    found = true;
                    break;
                }
            }
            if(found == false) {
                extra.push(this);
            }
        });
        $('.card-body').show();
    }

    if (missing.length === 0) {
        $('#missing').text('None');
    } else {
        $('#missing').html('<ol><li>' + missing.join('</li><li>') + '</ol>');
    }

    if (extra.length === 0) {
        $('#extra').text('None');
    } else {
        $('#extra').html('<ol><li>' + extra.join('</li><li>') + '</ol>');
    }
}

function sort_unique(arr) {
    //retrieved from: https://stackoverflow.com/questions/4833651/javascript-array-sort-and-unique
    if (arr.length === 0) return arr;
    arr = arr.sort(function (a, b) { return a*1 - b*1; });
    var ret = [arr[0]];
    for (var i = 1; i < arr.length; i++) { //Start loop at 1: arr[0] can never be a duplicate
      if (arr[i-1] !== arr[i]) {
        ret.push(arr[i]);
      }
    }
    return ret;
  }