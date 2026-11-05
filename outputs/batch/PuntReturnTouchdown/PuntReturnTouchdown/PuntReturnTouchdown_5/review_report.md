# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_5

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_5`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 195
- **Validation Warnings:** 215
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 178
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `15` | `15` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `9` | `9` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `9` | `9` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `40` | `27` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `40` | `27` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `50` | `32` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `0` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `1` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `10` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `13` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `15` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `16` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `17` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `2` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `6` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `7` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `9` | `Group` | 0 | START | 0 | 79 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `15` | `15` | 54 | START | 54 | 99 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `9` | `9` | 80 | END | 80 | 80 |
| ✅ EXACT | `Action_PuntBall` | Punter | `9` | `9` | 100 | START | 100 | 122 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `40` | `27` | 185 | START | 185 | 198 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `40` | `27` | 211 | START | 211 | 219 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `50` | `32` | 549 | START | 549 | 555 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 558

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 172 | 119 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 569 | 379 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–531
- **Visible Samples:** 525

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 148 | 95 | inferred_complete_timeline |
| `Action_None` | 151 | 175 | 25 | inferred_complete_timeline |
| `Action_None` | 177 | 189 | 13 | inferred_complete_timeline |
| `Action_None` | 194 | 531 | 338 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 567

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 343 | 290 | inferred_complete_timeline |
| `Action_None` | 347 | 569 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–355
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_LongSnap` | 54 | 99 | 46 | inferred_complete_timeline |
| `Action_None` | 100 | 151 | 52 | inferred_complete_timeline |
| `Action_None` | 153 | 355 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–513
- **Visible Samples:** 504

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 234 | 181 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_None` | 242 | 247 | 6 | inferred_complete_timeline |
| `Action_None` | 250 | 255 | 6 | inferred_complete_timeline |
| `Action_None` | 259 | 513 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–555
- **Visible Samples:** 556

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 555 | 502 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 567

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 549 | 496 | inferred_complete_timeline |
| `Action_None` | 553 | 569 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–412
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_SnapReceive` | 80 | 80 | 1 | inferred_complete_timeline |
| `Action_None` | 81 | 99 | 19 | inferred_complete_timeline |
| `Action_PuntBall` | 100 | 122 | 23 | inferred_complete_timeline |
| `Action_None` | 123 | 383 | 261 | inferred_complete_timeline |
| `Action_None` | 386 | 397 | 12 | inferred_complete_timeline |
| `Action_None` | 407 | 412 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–313
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 229 | 176 | inferred_complete_timeline |
| `Action_None` | 240 | 243 | 4 | inferred_complete_timeline |
| `Action_None` | 248 | 313 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–339
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 268 | 215 | inferred_complete_timeline |
| `Action_None` | 272 | 278 | 7 | inferred_complete_timeline |
| `Action_None` | 286 | 339 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 249 | 196 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–377
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 377 | 324 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 70 | 17 | inferred_complete_timeline |
| `Action_None` | 72 | 179 | 108 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–307
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 155 | 102 | inferred_complete_timeline |
| `Action_None` | 159 | 164 | 6 | inferred_complete_timeline |
| `Action_None` | 166 | 174 | 9 | inferred_complete_timeline |
| `Action_None` | 176 | 178 | 3 | inferred_complete_timeline |
| `Action_None` | 180 | 187 | 8 | inferred_complete_timeline |
| `Action_None` | 191 | 203 | 13 | inferred_complete_timeline |
| `Action_None` | 206 | 227 | 22 | inferred_complete_timeline |
| `Action_None` | 231 | 237 | 7 | inferred_complete_timeline |
| `Action_None` | 239 | 241 | 3 | inferred_complete_timeline |
| `Action_None` | 243 | 245 | 3 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 250 | 254 | 5 | inferred_complete_timeline |
| `Action_None` | 256 | 260 | 5 | inferred_complete_timeline |
| `Action_None` | 269 | 270 | 2 | inferred_complete_timeline |
| `Action_None` | 295 | 299 | 5 | inferred_complete_timeline |
| `Action_None` | 302 | 303 | 2 | inferred_complete_timeline |
| `Action_None` | 306 | 307 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 90 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–416
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 278 | 225 | inferred_complete_timeline |
| `Action_None` | 281 | 365 | 85 | inferred_complete_timeline |
| `Action_None` | 414 | 416 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 564

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 185 | 132 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 201 | 10 | inferred_complete_timeline |
| `Action_None` | 203 | 206 | 4 | inferred_complete_timeline |
| `Action_None` | 208 | 569 | 362 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–316
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 316 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–460
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 257 | 204 | inferred_complete_timeline |
| `Action_None` | 261 | 262 | 2 | inferred_complete_timeline |
| `Action_None` | 265 | 268 | 4 | inferred_complete_timeline |
| `Action_None` | 275 | 279 | 5 | inferred_complete_timeline |
| `Action_None` | 287 | 340 | 54 | inferred_complete_timeline |
| `Action_None` | 343 | 460 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–363
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 213 | 160 | inferred_complete_timeline |
| `Action_None` | 228 | 363 | 136 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–399 | 191 | 21 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 78–212 | 73 | 12 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 97–569 | 473 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 134–438 | 167 | 19 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 136–139 | 4 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 136–138 | 3 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 144–424 | 272 | 6 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 170–219 | 50 | 4 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 206–261 | 6 | 3 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 207–208 | 2 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 233–569 | 329 | 2 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 235–422 | 187 | 2 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 250–569 | 251 | 9 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 255–502 | 248 | 1 | Undefined position; Undefined team |
| `34` | `59` | Position_Unknown | Team_Unknown | 339–372 | 20 | 3 | Undefined position; Undefined team |
| `35` | `71` | Position_Unknown | Team_Unknown | 368–387 | 20 | 1 | Undefined position; Undefined team |
| `36` | `72` | Position_Unknown | Team_Unknown | 368–387 | 11 | 3 | Undefined position; Undefined team |
| `37` | `78` | Position_Unknown | Team_Unknown | 392–395 | 4 | 1 | Undefined position; Undefined team |
| `38` | `81` | Position_Unknown | Team_Unknown | 414–415 | 2 | 1 | Undefined position; Undefined team |
| `39` | `87` | Position_Unknown | Team_Unknown | 427–443 | 7 | 3 | Undefined position; Undefined team |
| `40` | `89` | Position_Unknown | Team_Unknown | 439–442 | 4 | 1 | Undefined position; Undefined team |
| `41` | `90` | Position_Unknown | Team_Unknown | 439–440 | 2 | 1 | Undefined position; Undefined team |
| `42` | `94` | Position_Unknown | Team_Unknown | 472–473 | 2 | 1 | Undefined position; Undefined team |
| `43` | `97` | Position_Unknown | Team_Unknown | 494–495 | 2 | 1 | Undefined position; Undefined team |
| `44` | `106` | Position_Unknown | Team_Unknown | 541–542 | 2 | 1 | Undefined position; Undefined team |
| `45` | `107` | Position_Unknown | Team_Unknown | 548–551 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 160 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [54-148] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-175] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-189] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-531] for track '0' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-268] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-278] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-339] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-549] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-213] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-363] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-278] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-365] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-416] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-377] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-555] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-234] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-247] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-255] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-513] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-185] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-201] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-383] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-397] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-412] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-343] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-155] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-164] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-174] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-187] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-203] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-227] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-237] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-254] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-260] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-229] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-243] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-313] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-316] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-355] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-172] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-249] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-257] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-279] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-340] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-460] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-70] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-179] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-53] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-68] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-81] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-125] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-134] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-141] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-167] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-257] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-298] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-337] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-378] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-399] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-81] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-90] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-137] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-202] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-569] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-163] for track '23' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-196] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-203] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-238] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-246] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-254] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-438] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-139] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-259] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-280] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-294] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-424] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [211-219] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-271] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-413] for track '31' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-422] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-251] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-255] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-258] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-281] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-298] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-350] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-502] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-372] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-387] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-371] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-377] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-395] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-415] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-429] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-433] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-443] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-442] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-440] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-473] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-495] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-542] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-551] for track '45' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>