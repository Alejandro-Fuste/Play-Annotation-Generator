# Play-Annotation-Generator Annotation Review — PuntBlock_38

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_38`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 114
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 99
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `10` | `10` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `5` | `5` |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher2 | defense | `15` | `15` |
| ✅ EXACT | `Action_SecureRecovery` | Right_Edge_Rusher1 | defense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `0` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `1` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `10` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `17` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `18` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `2` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `5` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `6` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `7` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `8` | `Group` | 0 | START | 0 | 26 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `10` | `10` | 27 | START | 27 | 76 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `5` | `5` | 54 | END | 54 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `5` | `5` | 77 | START | 77 | 91 |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher2 | `15` | `15` | 87 | START | 87 | 94 |
| ✅ EXACT | `Action_SecureRecovery` | Right_Edge_Rusher1 | `3` | `3` | 223 | START | 223 | 234 |

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
- **Visible Frames:** 0–222
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 172 | 146 | inferred_complete_timeline |
| `Action_None` | 174 | 176 | 3 | inferred_complete_timeline |
| `Action_None` | 183 | 222 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 269 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 65 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_LongSnap` | 27 | 76 | 50 | inferred_complete_timeline |
| `Action_None` | 77 | 100 | 24 | inferred_complete_timeline |
| `Action_None` | 102 | 105 | 4 | inferred_complete_timeline |
| `Action_None` | 107 | 206 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 142 | 116 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_None` | 169 | 173 | 5 | inferred_complete_timeline |
| `Action_None` | 176 | 245 | 70 | inferred_complete_timeline |
| `Action_None` | 247 | 269 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 106 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_SnapReceive` | 54 | 54 | 1 | inferred_complete_timeline |
| `Action_None` | 55 | 76 | 22 | inferred_complete_timeline |
| `Action_PuntBall` | 77 | 91 | 15 | inferred_complete_timeline |
| `Action_PuntBall` | 106 | 269 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 31 | 5 | inferred_complete_timeline |
| `Action_None` | 34 | 101 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 112 | 86 | inferred_complete_timeline |
| `Action_None` | 118 | 233 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 88 | 62 | inferred_complete_timeline |
| `Action_None` | 90 | 202 | 113 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 69 | 43 | inferred_complete_timeline |
| `Action_None` | 75 | 78 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_BlockPunt` | 87 | 94 | 8 | inferred_complete_timeline |
| `Action_None` | 95 | 118 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 75 | 49 | inferred_complete_timeline |
| `Action_None` | 100 | 122 | 23 | inferred_complete_timeline |
| `Action_None` | 124 | 269 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 35 | 9 | inferred_complete_timeline |
| `Action_None` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_None` | 42 | 92 | 51 | inferred_complete_timeline |
| `Action_None` | 95 | 115 | 21 | inferred_complete_timeline |
| `Action_None` | 124 | 248 | 125 | inferred_complete_timeline |
| `Action_None` | 253 | 269 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 112 | 86 | inferred_complete_timeline |
| `Action_None` | 115 | 236 | 122 | inferred_complete_timeline |
| `Action_None` | 239 | 245 | 7 | inferred_complete_timeline |
| `Action_None` | 254 | 267 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 61 | 35 | inferred_complete_timeline |
| `Action_None` | 65 | 265 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 269 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 60 | 34 | inferred_complete_timeline |
| `Action_None` | 64 | 228 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 85 | 59 | inferred_complete_timeline |
| `Action_None` | 95 | 269 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 222 | 223 | inferred_complete_timeline |
| `Action_SecureRecovery` | 223 | 234 | 12 | inferred_complete_timeline |
| `Action_None` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_None` | 267 | 269 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–269 | 270 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 75–230 | 146 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 84–121 | 36 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 87–227 | 98 | 8 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 94–269 | 176 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 116–219 | 92 | 5 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 128–129 | 2 | 1 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 130–269 | 130 | 4 | Undefined position; Undefined team |
| `28` | `28` | Position_Unknown | Team_Unknown | 133–269 | 134 | 3 | Undefined position; Undefined team |
| `29` | `29` | Position_Unknown | Team_Unknown | 158–159 | 2 | 1 | Undefined position; Undefined team |
| `30` | `30` | Position_Unknown | Team_Unknown | 160–268 | 36 | 10 | Undefined position; Undefined team |
| `31` | `31` | Position_Unknown | Team_Unknown | 175–193 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 82 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [27-106] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-142] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-245] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-65] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-222] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [223-234] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-60] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-228] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [77-91] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [106-269] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-88] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-202] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-112] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-233] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-61] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-265] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-100] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-105] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-206] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-112] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-236] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-245] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-267] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-269] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-75] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-122] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-118] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-85] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-172] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-222] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-31] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-69] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-35] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-40] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-92] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-115] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-248] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-153] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-230] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-96] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-121] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-103] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-134] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-143] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-157] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-193] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-135] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-155] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-162] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-219] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-206] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-236] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-245] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-171] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>