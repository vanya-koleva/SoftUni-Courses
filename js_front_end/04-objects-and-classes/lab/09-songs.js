function solve(input) {
    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;
        }

        print() {
            console.log(this.name);
        }
    }

    const count = input.shift();
    const playlist = input.pop();
    const songLibrary = [];

    for (let i = 0; i < count; i++) {
        const [typeList, name, time] = input.shift().split('_');
        songLibrary.push(new Song(typeList, name, time));
    }

    if (playlist === 'all') {
        songLibrary.forEach(song => song.print());
    } else {
        songLibrary.filter(song => song.typeList == playlist).forEach(song => song.print());
    }
}

solve([
    3,
    'favourite_DownTown_3:14',
    'favourite_Kiss_4:16',
    'favourite_Smooth Criminal_4:01',
    'favourite',
]);

solve([
    4,
    'favourite_DownTown_3:14',
    'listenLater_Andalouse_3:24',
    'favourite_In To The Night_3:58',
    'favourite_Live It Up_3:48',
    'listenLater',
]);

solve([2, 'like_Replay_3:15', 'ban_Photoshop_3:48', 'all']);
