# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_96

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_96`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 111
- **Ball Tracks:** 0
- **Action Segments:** 429
- **Validation Warnings:** 608
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 417
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `7` | `7` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `7` | `7` |
| ⚠️ START CHANGED | `Action_CatchKick` | Position_Unknown | Team_Unknown | `81` | `62` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `81` | `62` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `81` | `62` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `0` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `1` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `12` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `3` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `4` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `6` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `7` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `9` | `Group` | 0 | START | 0 | 16 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `7` | `7` | 17 | START | 17 | 58 |
| ✅ EXACT | `Action_KickBall` | Kicker | `7` | `7` | 59 | START | 59 | 64 |
| ⚠️ START CHANGED | `Action_CatchKick` | Position_Unknown | `81` | `62` | 172 | START | 185 | 185 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `81` | `62` | 189 | START | 189 | 198 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `81` | `62` | 622 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_KickApproach` | 17 | 58 | 42 | inferred_complete_timeline |
| `Action_KickBall` | 59 | 64 | 6 | inferred_complete_timeline |
| `Action_None` | 65 | 100 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 32 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–29
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 29 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 97 | 81 | inferred_complete_timeline |
| `Action_None` | 130 | 134 | 5 | inferred_complete_timeline |
| `Action_None` | 171 | 188 | 18 | inferred_complete_timeline |
| `Action_None` | 191 | 196 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 100 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 85 | 69 | inferred_complete_timeline |
| `Action_None` | 88 | 97 | 10 | inferred_complete_timeline |
| `Action_None` | 100 | 108 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 100 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 100 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 100 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 73 | 57 | inferred_complete_timeline |
| `Action_None` | 75 | 94 | 20 | inferred_complete_timeline |
| `Action_None` | 97 | 100 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 100 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 100 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–44 | 45 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 12–13 | 2 | 1 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 12–34 | 9 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 42–135 | 42 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 49–100 | 34 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 58–59 | 2 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 65–71 | 7 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 81–83 | 3 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 81–83 | 3 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 81–91 | 11 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 82–93 | 5 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 82–135 | 4 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 90–100 | 11 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 90–91 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 99–100 | 2 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 101–113 | 7 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 101–104 | 4 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 101–193 | 81 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 101–288 | 132 | 10 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 101–104 | 4 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 101–104 | 4 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 101–440 | 340 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 101–390 | 286 | 4 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 101–104 | 4 | 1 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 101–116 | 10 | 3 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 101–104 | 4 | 1 | Undefined position; Undefined team |
| `38` | `42` | Position_Unknown | Team_Unknown | 101–104 | 4 | 1 | Undefined position; Undefined team |
| `39` | `43` | Position_Unknown | Team_Unknown | 101–157 | 33 | 7 | Undefined position; Undefined team |
| `40` | `44` | Position_Unknown | Team_Unknown | 101–131 | 21 | 3 | Undefined position; Undefined team |
| `41` | `45` | Position_Unknown | Team_Unknown | 101–108 | 6 | 2 | Undefined position; Undefined team |
| `42` | `47` | Position_Unknown | Team_Unknown | 105–368 | 263 | 2 | Undefined position; Undefined team |
| `43` | `48` | Position_Unknown | Team_Unknown | 105–120 | 15 | 2 | Undefined position; Undefined team |
| `44` | `49` | Position_Unknown | Team_Unknown | 105–629 | 416 | 18 | Undefined position; Undefined team |
| `45` | `50` | Position_Unknown | Team_Unknown | 105–346 | 228 | 6 | Undefined position; Undefined team |
| `46` | `51` | Position_Unknown | Team_Unknown | 105–629 | 464 | 17 | Undefined position; Undefined team |
| `47` | `52` | Position_Unknown | Team_Unknown | 105–328 | 220 | 4 | Undefined position; Undefined team |
| `48` | `53` | Position_Unknown | Team_Unknown | 105–106 | 2 | 1 | Undefined position; Undefined team |
| `49` | `54` | Position_Unknown | Team_Unknown | 105–180 | 52 | 4 | Undefined position; Undefined team |
| `50` | `55` | Position_Unknown | Team_Unknown | 105–161 | 57 | 1 | Undefined position; Undefined team |
| `51` | `56` | Position_Unknown | Team_Unknown | 105–159 | 52 | 2 | Undefined position; Undefined team |
| `52` | `58` | Position_Unknown | Team_Unknown | 107–113 | 5 | 2 | Undefined position; Undefined team |
| `53` | `59` | Position_Unknown | Team_Unknown | 109–386 | 178 | 9 | Undefined position; Undefined team |
| `54` | `60` | Position_Unknown | Team_Unknown | 112–209 | 92 | 5 | Undefined position; Undefined team |
| `55` | `61` | Position_Unknown | Team_Unknown | 112–118 | 6 | 2 | Undefined position; Undefined team |
| `56` | `62` | Position_Unknown | Team_Unknown | 117–123 | 6 | 2 | Undefined position; Undefined team |
| `57` | `64` | Position_Unknown | Team_Unknown | 121–477 | 290 | 14 | Undefined position; Undefined team |
| `58` | `65` | Position_Unknown | Team_Unknown | 125–130 | 5 | 2 | Undefined position; Undefined team |
| `59` | `67` | Position_Unknown | Team_Unknown | 132–301 | 147 | 2 | Undefined position; Undefined team |
| `60` | `78` | Position_Unknown | Team_Unknown | 171–321 | 135 | 6 | Undefined position; Undefined team |
| `61` | `80` | Position_Unknown | Team_Unknown | 173–585 | 363 | 5 | Undefined position; Undefined team |
| `62` | `81` | Position_Unknown | Team_Unknown | 185–198 | 14 | 3 | Undefined position; Undefined team |
| `63` | `83` | Position_Unknown | Team_Unknown | 192–209 | 18 | 1 | Undefined position; Undefined team |
| `64` | `86` | Position_Unknown | Team_Unknown | 198–355 | 102 | 5 | Undefined position; Undefined team |
| `65` | `87` | Position_Unknown | Team_Unknown | 202–629 | 374 | 6 | Undefined position; Undefined team |
| `66` | `88` | Position_Unknown | Team_Unknown | 205–221 | 8 | 2 | Undefined position; Undefined team |
| `67` | `90` | Position_Unknown | Team_Unknown | 210–212 | 3 | 1 | Undefined position; Undefined team |
| `68` | `93` | Position_Unknown | Team_Unknown | 220–290 | 70 | 2 | Undefined position; Undefined team |
| `69` | `94` | Position_Unknown | Team_Unknown | 222–557 | 262 | 12 | Undefined position; Undefined team |
| `70` | `96` | Position_Unknown | Team_Unknown | 226–306 | 74 | 3 | Undefined position; Undefined team |
| `71` | `97` | Position_Unknown | Team_Unknown | 226–253 | 23 | 2 | Undefined position; Undefined team |
| `72` | `98` | Position_Unknown | Team_Unknown | 226–578 | 257 | 19 | Undefined position; Undefined team |
| `73` | `99` | Position_Unknown | Team_Unknown | 226–229 | 4 | 1 | Undefined position; Undefined team |
| `74` | `101` | Position_Unknown | Team_Unknown | 233–266 | 34 | 1 | Undefined position; Undefined team |
| `75` | `105` | Position_Unknown | Team_Unknown | 275–619 | 333 | 7 | Undefined position; Undefined team |
| `76` | `106` | Position_Unknown | Team_Unknown | 280–348 | 69 | 1 | Undefined position; Undefined team |
| `77` | `108` | Position_Unknown | Team_Unknown | 287–629 | 290 | 8 | Undefined position; Undefined team |
| `78` | `110` | Position_Unknown | Team_Unknown | 304–629 | 295 | 9 | Undefined position; Undefined team |
| `79` | `112` | Position_Unknown | Team_Unknown | 314–574 | 239 | 10 | Undefined position; Undefined team |
| `80` | `113` | Position_Unknown | Team_Unknown | 318–406 | 83 | 3 | Undefined position; Undefined team |
| `81` | `115` | Position_Unknown | Team_Unknown | 327–629 | 290 | 5 | Undefined position; Undefined team |
| `82` | `116` | Position_Unknown | Team_Unknown | 332–333 | 2 | 1 | Undefined position; Undefined team |
| `83` | `118` | Position_Unknown | Team_Unknown | 344–373 | 28 | 3 | Undefined position; Undefined team |
| `84` | `119` | Position_Unknown | Team_Unknown | 344–463 | 113 | 6 | Undefined position; Undefined team |
| `85` | `120` | Position_Unknown | Team_Unknown | 349–350 | 2 | 1 | Undefined position; Undefined team |
| `86` | `122` | Position_Unknown | Team_Unknown | 363–621 | 175 | 20 | Undefined position; Undefined team |
| `87` | `124` | Position_Unknown | Team_Unknown | 379–421 | 28 | 6 | Undefined position; Undefined team |
| `88` | `125` | Position_Unknown | Team_Unknown | 386–392 | 7 | 1 | Undefined position; Undefined team |
| `89` | `126` | Position_Unknown | Team_Unknown | 390–391 | 2 | 1 | Undefined position; Undefined team |
| `90` | `127` | Position_Unknown | Team_Unknown | 390–596 | 181 | 8 | Undefined position; Undefined team |
| `91` | `128` | Position_Unknown | Team_Unknown | 395–629 | 216 | 11 | Undefined position; Undefined team |
| `92` | `131` | Position_Unknown | Team_Unknown | 406–629 | 161 | 11 | Undefined position; Undefined team |
| `93` | `132` | Position_Unknown | Team_Unknown | 443–571 | 103 | 10 | Undefined position; Undefined team |
| `94` | `134` | Position_Unknown | Team_Unknown | 457–460 | 4 | 1 | Undefined position; Undefined team |
| `95` | `135` | Position_Unknown | Team_Unknown | 470–471 | 2 | 1 | Undefined position; Undefined team |
| `96` | `137` | Position_Unknown | Team_Unknown | 476–479 | 4 | 1 | Undefined position; Undefined team |
| `97` | `138` | Position_Unknown | Team_Unknown | 476–480 | 5 | 1 | Undefined position; Undefined team |
| `98` | `139` | Position_Unknown | Team_Unknown | 477–482 | 6 | 1 | Undefined position; Undefined team |
| `99` | `140` | Position_Unknown | Team_Unknown | 483–627 | 34 | 7 | Undefined position; Undefined team |
| `100` | `141` | Position_Unknown | Team_Unknown | 485–561 | 67 | 4 | Undefined position; Undefined team |
| `101` | `142` | Position_Unknown | Team_Unknown | 498–499 | 2 | 1 | Undefined position; Undefined team |
| `102` | `143` | Position_Unknown | Team_Unknown | 500–629 | 111 | 4 | Undefined position; Undefined team |
| `103` | `144` | Position_Unknown | Team_Unknown | 500–629 | 77 | 12 | Undefined position; Undefined team |
| `104` | `145` | Position_Unknown | Team_Unknown | 586–588 | 3 | 1 | Undefined position; Undefined team |
| `105` | `147` | Position_Unknown | Team_Unknown | 593–601 | 7 | 2 | Undefined position; Undefined team |
| `106` | `148` | Position_Unknown | Team_Unknown | 594–624 | 7 | 2 | Undefined position; Undefined team |
| `107` | `149` | Position_Unknown | Team_Unknown | 601–629 | 20 | 3 | Undefined position; Undefined team |
| `108` | `151` | Position_Unknown | Team_Unknown | 614–629 | 15 | 2 | Undefined position; Undefined team |
| `109` | `152` | Position_Unknown | Team_Unknown | 620–621 | 2 | 1 | Undefined position; Undefined team |
| `110` | `153` | Position_Unknown | Team_Unknown | 622–624 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_CatchKick` for actor_track_id `81` (Position_Unknown): Annotated start 172 != Inferred start 185
- ❌ Missing segment for action `Action_CrossGoalLine` on target `81` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ 99 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 99 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 198 |
| Missing visible bounding boxes during action | 406 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 193: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Segment 'Action_CatchKick' for track '62' has invalid range: start=185, end=177. Clamping end to start.
- ⚠️ Segment 'Action_CrossGoalLine' for track '62' has invalid range: start=622, end=198. Clamping end to start.
- ⚠️ Action 'Action_None' range [17-100] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-97] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-134] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-188] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-196] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-100] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-100] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-100] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-100] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-85] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-108] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [59-64] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-100] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-73] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-94] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-100] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-29] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-100] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-44] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-32] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-34] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-44] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-53] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-100] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-75] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-83] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-100] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-71] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-91] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-100] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-178] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-122] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-158] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-163] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-185] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-274] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-440] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-193] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-286] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-390] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-113] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-114] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-135] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-124] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-365] for track '42' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-111] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-120] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-167] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-271] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-293] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-319] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-368] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-471] for track '44' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-487] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-509] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-519] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-534] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-557] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-565] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-578] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-617] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-118] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-125] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-135] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-337] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-150] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-158] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-171] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-237] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-261] for track '46' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-288] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-322] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-382] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-492] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-536] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-587] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-609] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-624] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-629] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-307] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-316] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-322] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-328] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-122] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-139] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-163] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-161] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-147] for track '51' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-159] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-120] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-167] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-183] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-275] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-305] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-317] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-386] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-123] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-131] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-209] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-123] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-124] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-153] for track '57' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-170] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-199] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-358] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-373] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-379] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-398] for track '57' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-413] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-441] for track '57' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-458] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-477] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-271] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-301] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-196] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-204] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-312] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-321] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-501] for track '61' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-509] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-541] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-578] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-585] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [189-198] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-209] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-203] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-286] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-291] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-337] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-264] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-291] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-399] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-463] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-552] for track '65' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-287] for track '68' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-276] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-312] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-359] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-380] for track '69' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-385] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-394] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-466] for track '69' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-501] for track '69' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-531] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-543] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-549] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-557] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-280] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-306] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-242] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-253] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-260] for track '72' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-277] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-390] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-398] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-418] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-421] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-440] for track '72' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-457] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-474] for track '72' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-484] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-490] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-501] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-509] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-520] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-529] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-537] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-554] for track '72' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-570] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-578] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-266] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-313] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-519] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-525] for track '75' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-609] for track '75' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-613] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-619] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-348] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-521] for track '77' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-527] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-532] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-542] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-551] for track '77' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-563] for track '77' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-595] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-629] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-310] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-452] for track '78' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-541] for track '78' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-581] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-587] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-590] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-617] for track '78' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-624] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-629] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-331] for track '79' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-480] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-490] for track '79' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-497] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-501] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-523] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-548] for track '79' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-555] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-568] for track '79' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-574] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-350] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-392] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-406] for track '80' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-493] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-509] for track '81' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-546] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-609] for track '81' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-365] for track '83' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-370] for track '83' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-360] for track '84' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-376] for track '84' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-386] for track '84' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-393] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-463] for track '84' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-417] for track '86' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-442] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-450] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-464] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-467] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-482] for track '86' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-487] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-495] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-504] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-509] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-547] for track '86' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-557] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-561] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-566] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-570] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-593] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-598] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-601] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-608] for track '86' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-621] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-381] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-394] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-407] for track '87' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-415] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-421] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-392] for track '88' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-391] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-497] for track '90' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-504] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-521] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-541] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-548] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-555] for track '90' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-581] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-596] for track '90' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-422] for track '91' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-428] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-479] for track '91' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-486] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-492] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-557] for track '91' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-564] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-588] for track '91' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-617] for track '91' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-624] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-454] for track '92' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-464] for track '92' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-471] for track '92' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-490] for track '92' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-509] for track '92' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-545] for track '92' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-555] for track '92' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-584] for track '92' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-599] for track '92' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-608] for track '92' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-629] for track '92' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-452] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-480] for track '93' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-486] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-490] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-495] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-503] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-516] for track '93' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-557] for track '93' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-564] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-571] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-460] for track '94' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '95' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-479] for track '96' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-480] for track '97' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-482] for track '98' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-490] for track '99' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-503] for track '99' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-506] for track '99' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-516] for track '99' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-528] for track '99' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-547] for track '99' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-627] for track '99' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-489] for track '100' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-501] for track '100' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-551] for track '100' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-561] for track '100' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-499] for track '101' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-501] for track '102' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-504] for track '102' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-509] for track '102' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-509] for track '103' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-519] for track '103' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-540] for track '103' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-560] for track '103' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-566] for track '103' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-570] for track '103' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-578] for track '103' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-587] for track '103' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-599] for track '103' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-615] for track '103' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-621] for track '103' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-588] for track '104' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-597] for track '105' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-601] for track '105' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-596] for track '106' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-624] for track '106' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-611] for track '107' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-621] for track '107' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-624] for track '108' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-621] for track '109' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-624] for track '110' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '67' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '67' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '68' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '68' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '69' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '69' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '70' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '70' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '71' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '71' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '72' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '72' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '73' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '73' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '74' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '74' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '75' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '75' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '76' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '76' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '77' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '77' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '78' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '78' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '79' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '79' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '80' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '80' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '81' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '81' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '82' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '82' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '83' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '83' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '84' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '84' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '85' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '85' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '86' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '86' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '87' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '87' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '88' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '88' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '89' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '89' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '90' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '90' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '91' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '91' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '92' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '92' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '93' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '93' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '94' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '94' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '95' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '95' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '96' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '96' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '97' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '97' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '98' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '98' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '99' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '99' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '100' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '100' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '101' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '101' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '102' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '102' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '103' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '103' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '104' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '104' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '105' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '105' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '106' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '106' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '107' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '107' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '108' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '108' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '109' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '109' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '110' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '110' has undefined team_side. Will map to Team_Unknown.

</details>