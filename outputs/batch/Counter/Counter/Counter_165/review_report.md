# Play-Annotation-Generator Annotation Review — Counter_165

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_165`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 88
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `19` | `17` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_PullLeadBlock` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | C | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 74 |
| ✅ EXACT | `Action_BallSnap` | RG | `14` | `13` | 73 | START | 73 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `14` | `13` | 75 | START | 75 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `15` | `14` | 75 | START | 75 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `19` | `17` | 75 | START | 75 | 78 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `16` | `15` | 75 | START | 75 | 96 |
| ✅ EXACT | `Action_PullLeadBlock` | QB | `9` | `8` | 75 | START | 75 | 161 |
| ✅ EXACT | `Action_SnapReceive` | C | `13` | `12` | 88 | END | 73 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | C | `13` | `12` | 110 | START | 110 | 134 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 161 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 75 | 161 | 87 | inferred_complete_timeline |
| `Action_None` | 162 | 228 | 67 | inferred_complete_timeline |
| `Action_None` | 232 | 269 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 196 | 124 | inferred_complete_timeline |
| `Action_None` | 202 | 208 | 7 | inferred_complete_timeline |
| `Action_None` | 223 | 269 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 269 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 269 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 269 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_SnapReceive` | 73 | 88 | 16 | inferred_complete_timeline |
| `Action_None` | 89 | 109 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 110 | 134 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 137 | 167 | 31 | inferred_complete_timeline |
| `Action_BallCarry` | 169 | 233 | 65 | inferred_complete_timeline |
| `Action_BallCarry` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 244 | 252 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 265 | 269 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_BallSnap` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 75 | 104 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 127 | 143 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 154 | 161 | 8 | inferred_complete_timeline |
| `Action_None` | 162 | 269 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 269 | 197 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 269 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 136 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 248 | 176 | inferred_complete_timeline |
| `Action_None` | 250 | 269 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 126 | 54 | inferred_complete_timeline |
| `Action_None` | 139 | 214 | 76 | inferred_complete_timeline |
| `Action_None` | 221 | 266 | 46 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 269 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 174 | 102 | inferred_complete_timeline |
| `Action_None` | 176 | 269 | 94 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–269 | 244 | 9 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–96 | 97 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 3–267 | 261 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 4–106 | 98 | 3 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 16–269 | 244 | 4 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 39–269 | 228 | 4 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 45–255 | 190 | 8 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 77–151 | 7 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 84–269 | 186 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 103–269 | 160 | 6 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 119–142 | 24 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 154–269 | 96 | 7 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 161–249 | 74 | 6 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 196–198 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (9 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 332: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [73-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-196] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-208] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-269] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-136] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-228] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-126] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-214] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-266] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-174] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-269] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-248] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [110-134] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [137-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [169-233] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [235-236] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [244-252] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [265-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [75-104] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [127-143] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [75-88] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [95-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [115-116] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [120-123] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [130-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [135-161] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-201] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [75-96] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-173] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-262] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [75-78] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [84-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-205] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-214] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-109] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-201] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-46] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-65] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-70] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-202] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-220] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-234] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-246] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-255] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-167] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-174] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-215] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-221] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-234] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-142] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-172] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-198] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-262] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-196] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-235] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-246] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '27' has 1 frames without a visible bounding box.
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

</details>