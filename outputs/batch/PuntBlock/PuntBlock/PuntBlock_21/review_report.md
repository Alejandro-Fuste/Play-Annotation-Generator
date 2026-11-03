# Play-Annotation-Generator Annotation Review — PuntBlock_21

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_21`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 51
- **Ball Tracks:** 0
- **Action Segments:** 123
- **Validation Warnings:** 146
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 109
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `7` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | offense | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_BlockPunt` | Punt_Support2 | defense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `11` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `12` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `14` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `16` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `17` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `18` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `20` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `4` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `6` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `7` | `Group` | 0 | START | 0 | 32 |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | `11` | `11` | 33 | START | 33 | 52 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `6` | `6` | 62 | END | 62 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `6` | `6` | 88 | START | 88 | 230 |
| ✅ EXACT | `Action_BlockPunt` | Punt_Support2 | `3` | `3` | 100 | START | 100 | 106 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 151 | 119 | inferred_complete_timeline |
| `Action_None` | 156 | 163 | 8 | inferred_complete_timeline |
| `Action_None` | 166 | 187 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 183 | 151 | inferred_complete_timeline |
| `Action_None` | 187 | 205 | 19 | inferred_complete_timeline |
| `Action_None` | 207 | 299 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 145 | 113 | inferred_complete_timeline |
| `Action_None` | 147 | 218 | 72 | inferred_complete_timeline |
| `Action_None` | 220 | 299 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 242 | 210 | inferred_complete_timeline |
| `Action_None` | 247 | 299 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 101 | 69 | inferred_complete_timeline |
| `Action_None` | 118 | 224 | 107 | inferred_complete_timeline |
| `Action_None` | 233 | 299 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 97 | 65 | inferred_complete_timeline |
| `Action_None` | 101 | 122 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_SnapReceive` | 62 | 62 | 1 | inferred_complete_timeline |
| `Action_None` | 63 | 87 | 25 | inferred_complete_timeline |
| `Action_PuntBall` | 88 | 230 | 143 | inferred_complete_timeline |
| `Action_PuntBall` | 233 | 299 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_LongSnap` | 33 | 52 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 130 | 98 | inferred_complete_timeline |
| `Action_None` | 132 | 295 | 164 | inferred_complete_timeline |
| `Action_None` | 297 | 298 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 70 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 230 | 198 | inferred_complete_timeline |
| `Action_None` | 233 | 284 | 52 | inferred_complete_timeline |
| `Action_None` | 287 | 299 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 59 | 27 | inferred_complete_timeline |
| `Action_None` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_None` | 112 | 113 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 66 | 34 | inferred_complete_timeline |
| `Action_None` | 72 | 299 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 122 | 90 | inferred_complete_timeline |
| `Action_None` | 134 | 237 | 104 | inferred_complete_timeline |
| `Action_None` | 239 | 299 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_BlockPunt` | 100 | 106 | 7 | inferred_complete_timeline |
| `Action_None` | 107 | 214 | 108 | inferred_complete_timeline |
| `Action_None` | 222 | 299 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 213 | 181 | inferred_complete_timeline |
| `Action_None` | 218 | 299 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 299 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 299 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support6 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 240 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 299 | 267 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–115 | 115 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 56–257 | 201 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 64–266 | 183 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 76–299 | 224 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 98–101 | 4 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 126–132 | 6 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 136–299 | 145 | 9 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 139–141 | 3 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 142–143 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 142–147 | 5 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 144–146 | 3 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 144–274 | 111 | 5 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 147–149 | 3 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 150–261 | 112 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 152–299 | 148 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 180–201 | 17 | 2 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 183–285 | 84 | 3 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 195–229 | 35 | 1 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 199–202 | 4 | 1 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 210–218 | 7 | 2 | Undefined position; Undefined team |
| `40` | `48` | Position_Unknown | Team_Unknown | 212–213 | 2 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 244–299 | 56 | 1 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 245–262 | 16 | 2 | Undefined position; Undefined team |
| `43` | `55` | Position_Unknown | Team_Unknown | 246–247 | 2 | 1 | Undefined position; Undefined team |
| `44` | `56` | Position_Unknown | Team_Unknown | 263–287 | 25 | 1 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 266–299 | 34 | 1 | Undefined position; Undefined team |
| `46` | `62` | Position_Unknown | Team_Unknown | 277–288 | 10 | 2 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 292–299 | 8 | 1 | Undefined position; Undefined team |
| `48` | `67` | Position_Unknown | Team_Unknown | 293–299 | 7 | 1 | Undefined position; Undefined team |
| `49` | `69` | Position_Unknown | Team_Unknown | 297–298 | 2 | 1 | Undefined position; Undefined team |
| `50` | `70` | Position_Unknown | Team_Unknown | 299–299 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Punt_Support6` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Punt_Support5` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Punt_Support4` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Punt_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Right_Tackle` position mapped to `offense` team
- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 81 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 44: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [33-66] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-240] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-214] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-97] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-122] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-230] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-284] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [88-230] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [233-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-70] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-59] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [33-52] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-183] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-205] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-97] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-151] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-163] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-187] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-122] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-237] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-145] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-218] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-242] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-224] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-213] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-130] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-295] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-227] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-257] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-70] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-95] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-244] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-176] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-222] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-252] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-291] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-166] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-187] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-230] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-260] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-274] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-261] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-192] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-192] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-218] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-285] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-229] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-256] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-262] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-287] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-282] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-299] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>