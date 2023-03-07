<template>

    <div>
        <p class="logo">SecondChance</p>
        <h1>This is a h1 header.</h1>
        <h2>This is a h2 header.</h2>
        <h3>This is a h3 header.</h3>
        <h4>This is a h4 header.</h4>

        <p>This is a paragraph of text. Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatibus error hic molestias quibusdam dolores natus labore illum minus quae corrupti ipsa eum consequuntur, sapiente sint! Nobis maiores id vero quaerat!</p>

        <small>This is a small text.</small>

        <h3>Form Inputs</h3>
        <form class="mt-4">
            <div class="group">      
              <input type="text" required>
              <span class="highlight"></span>
              <span class="bar"></span>
              <label>Name</label>
            </div>
              
            <div class="group">      
              <input type="text" required>
              <span class="highlight"></span>
              <span class="bar"></span>
              <label>Email</label>
            </div>
        </form>

        <h3>Marketplace Search</h3>
        <ul id="growing-search-freebie" style="background-color:#c5dad2">
            <li>
              <!-- Start Freebie Markup -->
              <div class="growing-search">
                <div class="input">
                  <input type="text" placeholder="Search item"/>
                </div><!-- Space hack --><div class="submit">
                  <button type="submit" name="go_search">
                    <span class="fa fa-search"></span>
                  </button>
                </div>
              </div>
              <!-- End Freebie Markup -->
            </li>
          </ul>
        
        <h3>Buttons</h3>
        <div>
            <button class="btn btn-light"><span>Light</span></button>
            <button class="btn btn-dark"><span>Dark</span></button>
            <button class="btn btn-none">No Background</button>
        </div>

        <h3>Colour Scheme</h3>
        <div class="row my-2">
            <div class="col-3 p-3" style="background-color:#c5dad2">
                <p>Main colour</p>
            </div>
            <div class="col-3 p-3" style="background-color:#5c7266">
                <p>Accent colour 1</p>
            </div>
            <div class="col-3 p-3" style="background-color:#6e9190">
                <p>Accent colour 2</p>
            </div>
            <div class="col-3 p-3" style="background-color:#a3a0a0">
                <p>Grey</p>
            </div>
        </div>

    </div>




</template>
