# Play-Annotation-Generator Annotation Review — PuntBlock_29

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_29`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 329
- **Player Tracks:** 62
- **Ball Tracks:** 0
- **Action Segments:** 147
- **Validation Warnings:** 209
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 1
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 133
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `8` | `8` |
| ❌ MISSING SEGMENT | `Action_PuntBall` | Punter | offense | `8` | `8` |
| ⚠️ START CHANGED | `Action_BlockPunt` | Position_Unknown | Team_Unknown | `41` | `31` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `1` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `12` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `13` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `14` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `15` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `17` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `18` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `4` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `7` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `8` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `9` | `Group` | 0 | START | 0 | 22 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `9` | `9` | 23 | START | 23 | 40 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `8` | `8` | 56 | END | 56 | 56 |
| ❌ MISSING SEGMENT | `Action_PuntBall` | Punter | `8` | `8` | 128 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_BlockPunt` | Position_Unknown | `41` | `31` | 134 | START | 151 | 151 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 50 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 185 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 88 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_LongSnap` | 23 | 40 | 18 | inferred_complete_timeline |
| `Action_LongSnap` | 49 | 69 | 21 | inferred_complete_timeline |
| `Action_LongSnap` | 71 | 72 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 61 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 64 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 58 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_SnapReceive` | 56 | 56 | 1 | inferred_complete_timeline |
| `Action_None` | 57 | 94 | 38 | inferred_complete_timeline |
| `Action_None` | 98 | 102 | 5 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 46 | 24 | inferred_complete_timeline |
| `Action_None` | 51 | 64 | 14 | inferred_complete_timeline |
| `Action_None` | 66 | 203 | 138 | inferred_complete_timeline |
| `Action_None` | 206 | 212 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 65 | 43 | inferred_complete_timeline |
| `Action_None` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_None` | 74 | 93 | 20 | inferred_complete_timeline |
| `Action_None` | 95 | 152 | 58 | inferred_complete_timeline |
| `Action_None` | 154 | 158 | 5 | inferred_complete_timeline |
| `Action_None` | 161 | 192 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–56
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 56 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–181
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 181 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 22 | 17 | inferred_complete_timeline |
| `Action_None` | 23 | 66 | 44 | inferred_complete_timeline |
| `Action_None` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_None` | 71 | 72 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 64 | 42 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_None` | 71 | 74 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 149 | 127 | inferred_complete_timeline |
| `Action_None` | 151 | 157 | 7 | inferred_complete_timeline |
| `Action_None` | 159 | 173 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 72 | 50 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 53 | 31 | inferred_complete_timeline |
| `Action_None` | 57 | 182 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 198 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 67 | 45 | inferred_complete_timeline |
| `Action_None` | 71 | 72 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 159 | 137 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 14–130 | 104 | 8 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 65–97 | 33 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 68–69 | 2 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 81–198 | 105 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 84–247 | 164 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 117–119 | 3 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 119–123 | 5 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 125–329 | 204 | 2 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 141–192 | 46 | 3 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 143–147 | 5 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 145–147 | 3 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 151–158 | 7 | 3 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 164–171 | 8 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 173–329 | 141 | 4 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 173–329 | 153 | 2 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 176–268 | 88 | 3 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 178–198 | 21 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 178–205 | 14 | 2 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 180–282 | 84 | 4 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 181–212 | 30 | 2 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 182–246 | 7 | 2 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 183–193 | 10 | 2 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 183–195 | 10 | 3 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 185–198 | 14 | 1 | Undefined position; Undefined team |
| `44` | `60` | Position_Unknown | Team_Unknown | 190–329 | 129 | 4 | Undefined position; Undefined team |
| `45` | `63` | Position_Unknown | Team_Unknown | 194–197 | 4 | 1 | Undefined position; Undefined team |
| `46` | `65` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 200–329 | 110 | 5 | Undefined position; Undefined team |
| `48` | `67` | Position_Unknown | Team_Unknown | 203–233 | 11 | 2 | Undefined position; Undefined team |
| `49` | `69` | Position_Unknown | Team_Unknown | 206–329 | 124 | 1 | Undefined position; Undefined team |
| `50` | `71` | Position_Unknown | Team_Unknown | 215–225 | 11 | 1 | Undefined position; Undefined team |
| `51` | `73` | Position_Unknown | Team_Unknown | 233–253 | 12 | 2 | Undefined position; Undefined team |
| `52` | `75` | Position_Unknown | Team_Unknown | 244–256 | 13 | 1 | Undefined position; Undefined team |
| `53` | `76` | Position_Unknown | Team_Unknown | 249–289 | 25 | 3 | Undefined position; Undefined team |
| `54` | `77` | Position_Unknown | Team_Unknown | 265–329 | 65 | 1 | Undefined position; Undefined team |
| `55` | `78` | Position_Unknown | Team_Unknown | 271–287 | 17 | 1 | Undefined position; Undefined team |
| `56` | `79` | Position_Unknown | Team_Unknown | 276–329 | 54 | 1 | Undefined position; Undefined team |
| `57` | `80` | Position_Unknown | Team_Unknown | 285–322 | 27 | 2 | Undefined position; Undefined team |
| `58` | `82` | Position_Unknown | Team_Unknown | 308–309 | 2 | 1 | Undefined position; Undefined team |
| `59` | `83` | Position_Unknown | Team_Unknown | 308–329 | 22 | 1 | Undefined position; Undefined team |
| `60` | `84` | Position_Unknown | Team_Unknown | 311–321 | 6 | 2 | Undefined position; Undefined team |
| `61` | `85` | Position_Unknown | Team_Unknown | 313–314 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `9` (3 segments found)
- ❌ Missing segment for action `Action_PuntBall` on target `8` (Punter)
- ⚠️ `Action_BlockPunt` for actor_track_id `41` (Position_Unknown): Annotated start 134 != Inferred start 151

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ 42 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 42 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_SecureRecovery' at frame 208 targets track ID '224', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 84 |
| Missing visible bounding boxes during action | 121 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_PuntBall' for track '8' has invalid range: start=128, end=111. Clamping end to start.
- ⚠️ Segment 'Action_BlockPunt' for track '31' has invalid range: start=151, end=143. Clamping end to start.
- ⚠️ Action 'Action_None' range [23-53] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-182] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-65] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-93] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-152] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-158] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-192] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-72] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-149] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-157] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-173] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-185] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-159] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-181] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-58] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-94] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-102] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [23-40] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [49-69] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [71-72] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-67] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-198] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-46] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-64] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-203] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-212] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-61] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-64] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-56] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-64] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-74] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-50] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-88] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-66] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-22] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '20' starts at frame 23, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [23-23] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-69] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-81] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-108] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-116] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-97] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-94] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-133] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-198] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-247] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-123] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-253] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-182] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-192] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-147] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-171] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-285] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-301] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-329] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-242] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-268] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-198] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-188] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-189] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-240] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-256] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-282] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-208] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-246] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-190] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-198] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-203] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-219] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-225] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-211] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-225] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-246] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-323] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-209] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-329] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-225] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-253] for track '51' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-256] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-254] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-265] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-289] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-287] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-309] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-329] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-313] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.

</details>