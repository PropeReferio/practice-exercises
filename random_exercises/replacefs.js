// Replace consecutive f's with 'cd'

function ff2cd(stg){
    return stg.replace(/f{2,}/g , 'cd')
}

ff2cd('ffgotof34')