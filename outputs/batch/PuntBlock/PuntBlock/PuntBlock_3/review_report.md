# Play-Annotation-Generator Annotation Review — PuntBlock_3

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_3`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 57
- **Ball Tracks:** 0
- **Action Segments:** 158
- **Validation Warnings:** 202
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 143
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `16` | `16` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `15` | `15` |
| ✅ EXACT | `Action_BlockPunt` | Position_Unknown | Team_Unknown | `22` | `22` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `0` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `10` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `14` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `15` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `16` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `18` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `2` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `5` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `6` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `7` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `8` | `Group` | 0 | START | 0 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `16` | `16` | 44 | START | 44 | 67 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `15` | `15` | 74 | END | 74 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `15` | `15` | 96 | START | 96 | 123 |
| ✅ EXACT | `Action_BlockPunt` | Position_Unknown | `22` | `22` | 108 | START | 108 | 108 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 74 | 31 | inferred_complete_timeline |
| `Action_None` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_None` | 79 | 231 | 153 | inferred_complete_timeline |
| `Action_None` | 235 | 247 | 13 | inferred_complete_timeline |
| `Action_None` | 250 | 251 | 2 | inferred_complete_timeline |
| `Action_None` | 254 | 299 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 299 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 73 | 30 | inferred_complete_timeline |
| `Action_None` | 76 | 179 | 104 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 194 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 67 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_LongSnap` | 44 | 67 | 24 | inferred_complete_timeline |
| `Action_LongSnap` | 71 | 95 | 25 | inferred_complete_timeline |
| `Action_None` | 96 | 179 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 101 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 103 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_SnapReceive` | 74 | 74 | 1 | inferred_complete_timeline |
| `Action_None` | 75 | 95 | 21 | inferred_complete_timeline |
| `Action_PuntBall` | 96 | 123 | 28 | inferred_complete_timeline |
| `Action_PuntBall` | 127 | 129 | 3 | inferred_complete_timeline |
| `Action_PuntBall` | 141 | 147 | 7 | inferred_complete_timeline |
| `Action_PuntBall` | 151 | 159 | 9 | inferred_complete_timeline |
| `Action_PuntBall` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_PuntBall` | 168 | 213 | 46 | inferred_complete_timeline |
| `Action_PuntBall` | 215 | 225 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 86 | 43 | inferred_complete_timeline |
| `Action_None` | 94 | 100 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 111 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 69 | 26 | inferred_complete_timeline |
| `Action_None` | 73 | 76 | 4 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 79 | 36 | inferred_complete_timeline |
| `Action_None` | 84 | 103 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 101 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 101 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 56 | 13 | inferred_complete_timeline |
| `Action_None` | 60 | 65 | 6 | inferred_complete_timeline |
| `Action_None` | 76 | 202 | 127 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |
| `Action_None` | 220 | 224 | 5 | inferred_complete_timeline |
| `Action_None` | 231 | 245 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 54 | 11 | inferred_complete_timeline |
| `Action_None` | 57 | 67 | 11 | inferred_complete_timeline |
| `Action_None` | 92 | 299 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 68 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 73 | 30 | inferred_complete_timeline |
| `Action_None` | 75 | 102 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 101 | 58 | inferred_complete_timeline |
| `Action_None` | 105 | 110 | 6 | inferred_complete_timeline |
| `Action_None` | 114 | 172 | 59 | inferred_complete_timeline |
| `Action_None` | 174 | 179 | 6 | inferred_complete_timeline |
| `Action_None` | 182 | 186 | 5 | inferred_complete_timeline |
| `Action_None` | 188 | 243 | 56 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 251 | 252 | 2 | inferred_complete_timeline |
| `Action_None` | 257 | 299 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 70 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 299 | 256 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 77–79 | 3 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 80–108 | 29 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 84–116 | 20 | 5 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 84–95 | 12 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 99–210 | 106 | 4 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 109–110 | 2 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 114–115 | 2 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 116–299 | 179 | 2 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 116–159 | 33 | 3 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 126–299 | 166 | 3 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 136–224 | 84 | 3 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 136–299 | 153 | 3 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 142–198 | 55 | 2 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 147–148 | 2 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 153–183 | 29 | 2 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 156–226 | 57 | 5 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 156–236 | 75 | 3 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 156–299 | 113 | 7 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 158–280 | 123 | 1 | Undefined position; Undefined team |
| `40` | `45` | Position_Unknown | Team_Unknown | 171–202 | 9 | 3 | Undefined position; Undefined team |
| `41` | `49` | Position_Unknown | Team_Unknown | 172–173 | 2 | 1 | Undefined position; Undefined team |
| `42` | `50` | Position_Unknown | Team_Unknown | 173–193 | 5 | 2 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 176–294 | 95 | 2 | Undefined position; Undefined team |
| `44` | `55` | Position_Unknown | Team_Unknown | 179–202 | 21 | 2 | Undefined position; Undefined team |
| `45` | `57` | Position_Unknown | Team_Unknown | 200–212 | 7 | 2 | Undefined position; Undefined team |
| `46` | `61` | Position_Unknown | Team_Unknown | 207–208 | 2 | 1 | Undefined position; Undefined team |
| `47` | `62` | Position_Unknown | Team_Unknown | 212–290 | 70 | 2 | Undefined position; Undefined team |
| `48` | `63` | Position_Unknown | Team_Unknown | 227–243 | 6 | 2 | Undefined position; Undefined team |
| `49` | `64` | Position_Unknown | Team_Unknown | 237–238 | 2 | 1 | Undefined position; Undefined team |
| `50` | `65` | Position_Unknown | Team_Unknown | 244–253 | 10 | 1 | Undefined position; Undefined team |
| `51` | `67` | Position_Unknown | Team_Unknown | 258–259 | 2 | 1 | Undefined position; Undefined team |
| `52` | `68` | Position_Unknown | Team_Unknown | 260–288 | 26 | 3 | Undefined position; Undefined team |
| `53` | `69` | Position_Unknown | Team_Unknown | 262–264 | 3 | 1 | Undefined position; Undefined team |
| `54` | `72` | Position_Unknown | Team_Unknown | 283–297 | 14 | 2 | Undefined position; Undefined team |
| `55` | `73` | Position_Unknown | Team_Unknown | 285–286 | 2 | 1 | Undefined position; Undefined team |
| `56` | `74` | Position_Unknown | Team_Unknown | 299–299 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PuntBall` and target `15` (7 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_SecureRecovery' at frame 234 targets track ID '[?]', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 128 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [44-299] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-79] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-103] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-111] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-101] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-101] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-110] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-172] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-179] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-186] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-243] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-73] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-179] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-103] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-86] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-100] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-74] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-231] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-247] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-73] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-101] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-70] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-101] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-69] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-76] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [96-123] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [127-129] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [141-147] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [151-159] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [162-163] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [168-213] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [215-225] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [44-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-179] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-68] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-67] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-54] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-67] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-65] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-202] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-245] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-107] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockPunt' for track '22' starts at frame 108, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BlockPunt' range [108-108] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-88] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-96] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-95] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-180] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-202] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-124] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-119] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-159] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-129] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-262] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-139] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-215] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-162] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-270] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-194] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-172] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-183] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-194] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-212] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-226] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-236] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-171] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-213] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-243] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-269] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-299] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-280] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-261] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-294] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-195] for track '44' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-272] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-290] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-253] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-278] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-288] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-294] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '55' has 1 frames without a visible bounding box.
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

</details>