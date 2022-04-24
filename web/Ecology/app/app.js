const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const path = require("path");

const app = express();
app.use(express.json())
app.set('view engine', 'ejs');
const port = 1337

app.use(cors())

const users = [
    { name: 'user', password: 'user12345' },
    { name: 'admin', password: Math.random().toString(32), isAdmin: true },
];


app.use(bodyParser.json());


app.get('/', (req, res) => {
    res.status(200).sendFile(path.join(__dirname, 'views', 'index.html'));
});

const mySecret = "shellmates{Pr0T0TyP3_p0lLU710N_c4n_B3_V3Ry_d4n93r0U2}" 


var merge = function (target, source) {
    for (var attr in source) {
        if (typeof (target[attr]) === "object" && typeof (source[attr]) === "object") {
            merge(target[attr], source[attr]);
        } else {
            target[attr] = source[attr];
        }
    }

    return target;
};

function authUser(body) {
    return users.find((u) =>
        u.name === body.name &&
        u.password === body.password);
}


app.post('/', (req, res) => {

    const User = {
        date:new Date()
    }
    var user = Object.create(User);
    

    // Input validation?
    for (var attr in req.body) {
        if (attr == 'isAdmin') {
            res.status(403).send({ ok: false, error: 'Access denied, you sussy baka' })
            return;
        }
    }

    merge(user, req.body)
    const isAuthenticated = authUser(user || {});

    if (!isAuthenticated) {
        res.status(403).send({ ok: false, error: 'Access denied' });
        return;
    }

    if (user.isAdmin == true) {
        res.status(200).send(`Congrats! you found my secret app at: ${user.date}\n${mySecret}\n`)

    } else {
        res.status(200).send("You're not an admin you can't see the secret")
    }
})

app.listen(port);