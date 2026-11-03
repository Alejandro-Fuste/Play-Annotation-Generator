# Play-Annotation-Generator Annotation Review — PuntBlock_53

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_53`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 98
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `14` | `14` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `14` | `14` |
| ✅ EXACT | `Action_BlockPunt` | Position_Unknown | Team_Unknown | `22` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `11` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `13` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `14` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `16` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `17` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `18` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | `19` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `4` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `5` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `7` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `11` | `11` | 1 | START | 1 | 33 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `14` | `14` | 27 | END | 27 | 27 |
| ✅ EXACT | `Action_PuntBall` | Punter | `14` | `14` | 59 | START | 59 | 204 |
| ✅ EXACT | `Action_BlockPunt` | Position_Unknown | `22` | `21` | 66 | START | 66 | 71 |

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
- **Visible Frames:** 0–45
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 45 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 142 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 38 | 38 | inferred_complete_timeline |
| `Action_None` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_None` | 45 | 299 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 227 | 227 | inferred_complete_timeline |
| `Action_None` | 229 | 299 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–33
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_LongSnap` | 1 | 33 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 215 | 215 | inferred_complete_timeline |
| `Action_None` | 219 | 220 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 87 | 87 | inferred_complete_timeline |
| `Action_None` | 94 | 165 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 27 | 1 | inferred_complete_timeline |
| `Action_None` | 28 | 58 | 31 | inferred_complete_timeline |
| `Action_PuntBall` | 59 | 204 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 28 | 28 | inferred_complete_timeline |
| `Action_None` | 37 | 91 | 55 | inferred_complete_timeline |
| `Action_None` | 97 | 140 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–63
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 47 | 47 | inferred_complete_timeline |
| `Action_None` | 56 | 63 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–31
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 28 | 28 | inferred_complete_timeline |
| `Action_None` | 30 | 31 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 164 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 47 | 47 | inferred_complete_timeline |
| `Action_None` | 50 | 59 | 10 | inferred_complete_timeline |
| `Action_None` | 64 | 104 | 41 | inferred_complete_timeline |
| `Action_None` | 106 | 109 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 108 | 108 | inferred_complete_timeline |
| `Action_None` | 110 | 262 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 247 | 247 | inferred_complete_timeline |
| `Action_None` | 263 | 299 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 264 | 264 | inferred_complete_timeline |
| `Action_None` | 267 | 299 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 134 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 114 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–288
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |
| `Action_None` | 214 | 217 | 4 | inferred_complete_timeline |
| `Action_None` | 220 | 221 | 2 | inferred_complete_timeline |
| `Action_None` | 253 | 256 | 4 | inferred_complete_timeline |
| `Action_None` | 260 | 265 | 6 | inferred_complete_timeline |
| `Action_None` | 276 | 288 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 97 | 97 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–127 | 128 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 33–143 | 105 | 6 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 51–153 | 100 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 52–299 | 246 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 65–133 | 69 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 112–138 | 26 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 112–114 | 3 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 115–299 | 177 | 4 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 117–162 | 26 | 6 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 121–299 | 179 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 140–141 | 2 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 145–159 | 15 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 187–189 | 3 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 203–299 | 96 | 2 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 213–299 | 87 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 263–299 | 37 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Gunner2` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 108: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [1-264] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-256] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-265] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-288] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-247] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-108] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-262] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-227] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-28] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-91] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-140] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-114] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-215] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-28] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-31] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-127] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-47] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-59] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-104] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [1-33] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-97] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-47] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-63] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [59-204] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-134] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-87] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-165] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-38] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-41] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-45] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-142] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-164] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-97] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-124] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-143] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-122] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-153] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-108] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-299] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-133] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-116] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-138] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-221] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-246] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-299] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-129] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-162] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-159] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-284] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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

</details>