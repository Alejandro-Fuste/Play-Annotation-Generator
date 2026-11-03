# Play-Annotation-Generator Annotation Review — PuntBlock_73

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_73`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 145
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 106
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `16` | `16` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `8` | `8` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `8` | `8` |
| ❌ MISSING SEGMENT | `Action_BlockPunt` | Position_Unknown | Team_Unknown | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Left_Gunner | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `0` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `10` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `11` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `12` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `15` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `16` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `17` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `18` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `2` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `5` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `8` | `Group` | 0 | START | 0 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `16` | `16` | 7 | START | 7 | 58 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `8` | `8` | 33 | END | 33 | 33 |
| ✅ EXACT | `Action_PuntBall` | Punter | `8` | `8` | 65 | START | 65 | 132 |
| ❌ MISSING SEGMENT | `Action_BlockPunt` | Position_Unknown | `19` | `19` | 74 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Left_Gunner | `2` | `2` | 241 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 58 | 52 | inferred_complete_timeline |
| `Action_None` | 62 | 134 | 73 | inferred_complete_timeline |
| `Action_None` | 139 | 147 | 9 | inferred_complete_timeline |
| `Action_None` | 152 | 273 | 122 | inferred_complete_timeline |
| `Action_None` | 277 | 280 | 4 | inferred_complete_timeline |
| `Action_None` | 284 | 289 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–285
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 40 | 34 | inferred_complete_timeline |
| `Action_None` | 42 | 172 | 131 | inferred_complete_timeline |
| `Action_None` | 175 | 285 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 143 | 137 | inferred_complete_timeline |
| `Action_None` | 150 | 254 | 105 | inferred_complete_timeline |
| `Action_None` | 257 | 299 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_LongSnap` | 7 | 58 | 52 | inferred_complete_timeline |
| `Action_LongSnap` | 64 | 64 | 1 | inferred_complete_timeline |
| `Action_None` | 65 | 65 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 113 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 140 | 134 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_None` | 183 | 204 | 22 | inferred_complete_timeline |
| `Action_None` | 207 | 245 | 39 | inferred_complete_timeline |
| `Action_None` | 248 | 250 | 3 | inferred_complete_timeline |
| `Action_None` | 254 | 257 | 4 | inferred_complete_timeline |
| `Action_None` | 265 | 286 | 22 | inferred_complete_timeline |
| `Action_None` | 288 | 299 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_SnapReceive` | 33 | 33 | 1 | inferred_complete_timeline |
| `Action_None` | 34 | 64 | 31 | inferred_complete_timeline |
| `Action_PuntBall` | 65 | 132 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–31
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 31 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 155 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–54
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 46 | 40 | inferred_complete_timeline |
| `Action_None` | 50 | 54 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 34 | 28 | inferred_complete_timeline |
| `Action_None` | 37 | 60 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 127 | 121 | inferred_complete_timeline |
| `Action_None` | 130 | 133 | 4 | inferred_complete_timeline |
| `Action_None` | 135 | 141 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 207 | 201 | inferred_complete_timeline |
| `Action_None` | 217 | 228 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 130 | 124 | inferred_complete_timeline |
| `Action_None` | 139 | 150 | 12 | inferred_complete_timeline |
| `Action_None` | 179 | 181 | 3 | inferred_complete_timeline |
| `Action_None` | 186 | 219 | 34 | inferred_complete_timeline |
| `Action_None` | 222 | 273 | 52 | inferred_complete_timeline |
| `Action_None` | 286 | 299 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 186 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–285
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 218 | 212 | inferred_complete_timeline |
| `Action_None` | 220 | 228 | 9 | inferred_complete_timeline |
| `Action_None` | 231 | 285 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 54 | 48 | inferred_complete_timeline |
| `Action_None` | 58 | 59 | 2 | inferred_complete_timeline |
| `Action_None` | 65 | 67 | 3 | inferred_complete_timeline |
| `Action_None` | 82 | 186 | 105 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–135 | 124 | 5 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 2–58 | 52 | 4 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 6–10 | 5 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 31–139 | 109 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 36–37 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 41–299 | 256 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 58–136 | 79 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 61–183 | 123 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 66–118 | 51 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 73–86 | 14 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 75–220 | 143 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 77–78 | 2 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 103–104 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 112–299 | 170 | 3 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 168–173 | 6 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 180–299 | 120 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 190–297 | 104 | 3 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 198–238 | 40 | 2 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 201–299 | 88 | 2 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 203–299 | 66 | 7 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 241–299 | 59 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 284–288 | 5 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 285–297 | 13 | 1 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 292–299 | 8 | 1 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 297–299 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `16` (2 segments found)
- ❌ Missing segment for action `Action_BlockPunt` on target `19` (Position_Unknown)
- ❌ Missing segment for action `Action_SecureRecovery` on target `2` (Left_Gunner)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Guard` position mapped to `offense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 90 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 148: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureRecovery' for track '2' has invalid range: start=241, end=143. Clamping end to start.
- ⚠️ Segment 'Action_BlockPunt' for track '19' has invalid range: start=74, end=58. Clamping end to start.
- ⚠️ Action 'Action_None' range [7-155] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-54] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-67] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-186] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-143] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-75] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-124] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-130] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-130] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-219] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-273] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-143] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-254] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-186] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-127] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-141] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [65-132] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-34] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-60] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-140] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-204] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-245] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-257] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-286] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-46] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-54] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-113] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-218] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-228] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-285] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-207] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-228] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-40] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-172] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-285] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [7-58] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 65, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [65-65] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-31] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-58] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-134] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-147] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-273] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-280] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-289] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-18] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-27] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-30] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-58] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-10] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-139] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-37] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-286] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-136] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-183] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-110] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-118] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-86] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-184] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-214] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-220] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-136] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-174] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-299] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-173] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-299] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-264] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-279] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-297] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-207] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-238] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-223] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-222] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-280] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-288] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-297] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>