# Play-Annotation-Generator Annotation Review — PuntCoverage_39

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntCoverage_39`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_PuntCoverage`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 155
- **Validation Warnings:** 162
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 139
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `12` | `12` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `18` | `18` |
| ❌ MISSING SEGMENT | `Action_PuntBall` | Punter | offense | `18` | `18` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `38` | `29` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `38` | `29` |
| ⚠️ AMBIGUOUS MATCH | `Action_Tackle` | Position_Unknown | Team_Unknown | `45` | `34` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `0` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `12` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `16` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `17` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `18` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `2` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `3` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `5` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `8` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `9` | `Group` | 0 | START | 0 | 25 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `12` | `12` | 26 | START | 26 | 47 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `18` | `18` | 52 | END | 52 | 52 |
| ❌ MISSING SEGMENT | `Action_PuntBall` | Punter | `18` | `18` | 84 | START | N/A | N/A |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `38` | `29` | 205 | START | 205 | 218 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `38` | `29` | 231 | START | 231 | 276 |
| ⚠️ AMBIGUOUS MATCH | `Action_Tackle` | Position_Unknown | `45` | `34` | 251 | START | 251 | 266 |

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
- **Visible Frames:** 0–299
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 70 | 45 | inferred_complete_timeline |
| `Action_None` | 76 | 91 | 16 | inferred_complete_timeline |
| `Action_None` | 94 | 101 | 8 | inferred_complete_timeline |
| `Action_None` | 105 | 149 | 45 | inferred_complete_timeline |
| `Action_None` | 160 | 186 | 27 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_None` | 204 | 216 | 13 | inferred_complete_timeline |
| `Action_None` | 222 | 235 | 14 | inferred_complete_timeline |
| `Action_None` | 237 | 299 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 110 | 85 | inferred_complete_timeline |
| `Action_None` | 115 | 117 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_LongSnap` | 26 | 47 | 22 | inferred_complete_timeline |
| `Action_LongSnap` | 53 | 55 | 3 | inferred_complete_timeline |
| `Action_LongSnap` | 72 | 83 | 12 | inferred_complete_timeline |
| `Action_None` | 84 | 162 | 79 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 121 | 96 | inferred_complete_timeline |
| `Action_None` | 123 | 208 | 86 | inferred_complete_timeline |
| `Action_None` | 212 | 299 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 104 | 79 | inferred_complete_timeline |
| `Action_None` | 106 | 108 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 137 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 51 | 7 | inferred_complete_timeline |
| `Action_SnapReceive` | 52 | 52 | 1 | inferred_complete_timeline |
| `Action_None` | 53 | 53 | 1 | inferred_complete_timeline |
| `Action_None` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_None` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_None` | 63 | 67 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 50 | 25 | inferred_complete_timeline |
| `Action_None` | 52 | 59 | 8 | inferred_complete_timeline |
| `Action_None` | 62 | 159 | 98 | inferred_complete_timeline |
| `Action_None` | 161 | 178 | 18 | inferred_complete_timeline |
| `Action_None` | 182 | 184 | 3 | inferred_complete_timeline |
| `Action_None` | 187 | 191 | 5 | inferred_complete_timeline |
| `Action_None` | 199 | 207 | 9 | inferred_complete_timeline |
| `Action_None` | 215 | 222 | 8 | inferred_complete_timeline |
| `Action_None` | 224 | 299 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 128 | 103 | inferred_complete_timeline |
| `Action_None` | 132 | 160 | 29 | inferred_complete_timeline |
| `Action_None` | 164 | 166 | 3 | inferred_complete_timeline |
| `Action_None` | 171 | 174 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 169 | 144 | inferred_complete_timeline |
| `Action_None` | 172 | 175 | 4 | inferred_complete_timeline |
| `Action_None` | 180 | 201 | 22 | inferred_complete_timeline |
| `Action_None` | 204 | 206 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 164 | 139 | inferred_complete_timeline |
| `Action_None` | 169 | 180 | 12 | inferred_complete_timeline |
| `Action_None` | 183 | 299 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 62 | 37 | inferred_complete_timeline |
| `Action_None` | 74 | 127 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 86 | 61 | inferred_complete_timeline |
| `Action_None` | 88 | 299 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 72 | 47 | inferred_complete_timeline |
| `Action_None` | 81 | 84 | 4 | inferred_complete_timeline |
| `Action_None` | 93 | 151 | 59 | inferred_complete_timeline |
| `Action_None` | 153 | 161 | 9 | inferred_complete_timeline |
| `Action_None` | 163 | 174 | 12 | inferred_complete_timeline |
| `Action_None` | 181 | 184 | 4 | inferred_complete_timeline |
| `Action_None` | 186 | 191 | 6 | inferred_complete_timeline |
| `Action_None` | 202 | 205 | 4 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 220 | 221 | 2 | inferred_complete_timeline |
| `Action_None` | 232 | 299 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 158 | 133 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 176 | 5 | inferred_complete_timeline |
| `Action_None` | 181 | 184 | 4 | inferred_complete_timeline |
| `Action_None` | 189 | 299 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 74 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 132 | 107 | inferred_complete_timeline |
| `Action_None` | 134 | 157 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 202 | 177 | inferred_complete_timeline |
| `Action_None` | 204 | 299 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 160 | 135 | inferred_complete_timeline |
| `Action_None` | 162 | 179 | 18 | inferred_complete_timeline |
| `Action_None` | 181 | 299 | 119 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–80 | 79 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 33–299 | 261 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 81–130 | 35 | 5 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 89–299 | 202 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 104–176 | 63 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 127–128 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 133–299 | 103 | 10 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 140–299 | 159 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 145–166 | 11 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 160–161 | 2 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 166–294 | 116 | 6 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 170–172 | 3 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 170–299 | 119 | 3 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 172–299 | 91 | 5 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 183–184 | 2 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 190–299 | 98 | 3 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 206–299 | 88 | 3 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 223–299 | 74 | 2 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 235–299 | 65 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 283–299 | 17 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `12` (3 segments found)
- ❌ Missing segment for action `Action_PuntBall` on target `18` (Punter)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `38` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Tackle` and target `45` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 118 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 79: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_PuntBall' for track '18' has invalid range: start=84, end=67. Clamping end to start.
- ⚠️ Action 'Action_None' range [26-128] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-160] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-160] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-179] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-299] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-110] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-137] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-74] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-121] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-208] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-202] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-132] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-157] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-104] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-169] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-201] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-164] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-299] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-62] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-127] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [26-47] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [53-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-162] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-86] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-158] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-184] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-299] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-71] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-80] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-50] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-59] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-159] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-178] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-207] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-222] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-299] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-70] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-91] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-101] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-149] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-186] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-216] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-235] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '18' starts at frame 53, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [53-53] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-67] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-72] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-151] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-161] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-174] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-184] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-191] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-37] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-94] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-103] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-111] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-148] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-218] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-109] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-171] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-143] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-233] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-221] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-204] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [231-276] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [289-291] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [293-294] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-225] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-191] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' range [251-266] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' range [279-299] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-213] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-272] for track '35' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-236] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>