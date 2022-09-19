var isIsomorphic = function(s,t){
    function getKeyByValue(obj, value){
        return Object.keys(obj).find(key => obj[key] === value);
    }

    letra = [...t];
    dict = {};
    for(let i = 0; i <  letra.length; i++){
        if(s[i] in dict && dict[s[i]] === letra[i]){
            letra[i] = s[i].toString();
        }else if(s[i] in dict && dict[s[i]] != letra[i]){
            letra[i] = '';
        }else if(!(s[i] in dict)){
            const hasKey = getKeyByValue(dict, letra[i]);
            if(hasKey === undefined){
                dict[s[i]] = letra[i];
                letra[i] = s[i].toString();
            }else{
                letra[i] = '';
            }
        }
    }
    return letra.join('') === s;


};


console.log(isIsomorphic("aa", "ab"));