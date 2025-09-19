document.addEventListener('DOMContentLoaded', function(){
    if (window.autoFillPriceInitialized) {
        console.log('auto_fill_price: already initialized, skipping');
        return;
    }
    window.autoFillPriceInitialized = true;
    console.log('auto_fill_price.js loaded');
    function setPriceForTest(testId){
        console.log('setPriceForTest called with', testId);
        if(!testId) return;
        var url = '/analyses/test-price/' + testId + '/';
        fetch(url).then(function(res){
            if(!res.ok) throw new Error('No price');
            return res.json();
        }).then(function(data){
            var priceField = document.getElementById('id_price');
            if(priceField && data.price!==null){
                console.log('setting price to', data.price);
                priceField.value = data.price;
            }
        }).catch(function(e){
            // ignore
            console.error('price fetch error', e);
        });
    }

    function extractAndSetFromHidden(){
        // some admin widgets put the actual PK in a hidden input named 'test' or with id 'id_test'
        var hidden = document.querySelector('input[type=hidden]#id_test, input[type=hidden][name=test], input[type=hidden][name="test"]');
        if(hidden && hidden.value){
            setPriceForTest(hidden.value);
            return true;
        }
        return false;
    }

    // Try to find standard selects or inputs that represent the `test` field by name/id or data-field
    var selectors = [
        "select[name$='test']",
        "select[id$='_test']",
        "select[name*='test']",
        "input[name$='test']",
        "input[id$='_test']",
        "input[data-field='test']",
    ];
    var found = [];
    selectors.forEach(function(s){
        document.querySelectorAll(s).forEach(function(el){ if(found.indexOf(el)===-1) found.push(el); });
    });

    if(found.length){
        console.log('auto_fill_price: found test inputs/selects', found);
        found.forEach(function(el){
            // also attach select2/select handlers if jQuery/select2 present
            try {
                if (window.jQuery && jQuery(el).data && jQuery(el).data('select2')){
                    jQuery(el).on('select2:select', function(e){
                        var val = jQuery(el).val();
                        console.log('auto_fill_price: select2:select value', val);
                        if(val) setPriceForTest(val);
                    });
                }
            } catch(err){ console.error('auto_fill_price select2 hook error', err); }
            if(el.tagName && el.tagName.toLowerCase() === 'select'){
                el.addEventListener('change', function(e){ console.log('auto_fill_price: change event', e.target.value); setPriceForTest(e.target.value); });
                if(el.value) setPriceForTest(el.value);
                // polling fallback: in some select2 setups change event isn't fired reliably
                try{
                    (function(target){
                        var prev = target.value;
                        var pollCount = 0;
                        var poll = setInterval(function(){
                            var cur = target.value;
                            if(cur && cur !== prev){
                                console.log('auto_fill_price: poll detected value change', prev, '->', cur);
                                prev = cur;
                                setPriceForTest(cur);
                                clearInterval(poll);
                            }
                            pollCount++;
                            if(pollCount > 50){ // stop after ~15s
                                clearInterval(poll);
                            }
                        }, 300);
                    })(el);
                } catch(e){ /* ignore */ }
                // observe attribute changes on the select in case select2 updates value programmatically
                try{
                    var attrObserver = new MutationObserver(function(muts){
                        muts.forEach(function(m){
                            if(m.type === 'attributes' && m.attributeName === 'value'){
                                var v = el.value;
                                console.log('auto_fill_price: mutation observed value', v);
                                if(v) setPriceForTest(v);
                            }
                        });
                    });
                    attrObserver.observe(el, {attributes: true, attributeFilter: ['value']});
                } catch(e){ /* ignore */ }
            } else {
                // input - try to extract hidden or observe changes
                extractAndSetFromHidden();
                el.addEventListener('change', function(e){
                    // if value is numeric id, use it
                    console.log('auto_fill_price: input change', e.target.value);
                    if(e.target.value && /^\d+$/.test(e.target.value)) setPriceForTest(e.target.value);
                });
                // polling fallback for inputs too
                try{
                    (function(target){
                        var prev = target.value;
                        var pollCount = 0;
                        var poll = setInterval(function(){
                            var cur = target.value;
                            if(cur && cur !== prev){
                                console.log('auto_fill_price: poll detected input change', prev, '->', cur);
                                prev = cur;
                                if(/^\d+$/.test(cur)) setPriceForTest(cur);
                                clearInterval(poll);
                            }
                            pollCount++;
                            if(pollCount > 50) clearInterval(poll);
                        }, 300);
                    })(el);
                } catch(e){ }
            }
        });
    } else {
        // fallback to autocomplete/hidden extraction and observer
        extractAndSetFromHidden();
        var observer = new MutationObserver(function(mutations){ extractAndSetFromHidden(); });
        observer.observe(document.body, {childList: true, subtree: true, attributes: true});
    }

    // Delegated handlers (catch dynamically-initialized select2 widgets and dynamic changes)
    function delegatedHandler(ev){
        try{
            var t = ev.target;
            if(!t) return;
            var id = t.id || t.name || '';
            if(/test/i.test(id) || (t.getAttribute && t.getAttribute('data-field') === 'test')){
                var v = null;
                if(window.jQuery){
                    try{ v = jQuery(t).val(); } catch(e){ v = t.value; }
                } else {
                    v = t.value;
                }
                console.log('auto_fill_price: delegated change detected', id, v);
                if(v) setPriceForTest(v);
            }
        }catch(e){console.error(e)}
    }
    document.addEventListener('change', delegatedHandler, true);
    // if select2 present, listen for select2:select on document
    // prefer Django's bundled jQuery (django.jQuery) then window.jQuery
    var $ = (window.django && window.django.jQuery) || window.jQuery || window.$;
    if($){
        try{
            $(document).on('select2:select', 'select, input', function(e){
                var el = e.target || this;
                var id = el.id || el.name || '';
                if(/test/i.test(id) || (el.getAttribute && el.getAttribute('data-field') === 'test')){
                    var val = $(el).val();
                    console.log('auto_fill_price: select2:select', id, val);
                    if(val) setPriceForTest(val);
                }
            });
            // also jQuery delegated change
            $(document).on('change', 'select, input', function(e){ delegatedHandler(e); });
        }catch(err){ console.error('auto_fill_price jQuery hooks error', err); }
    }
});
