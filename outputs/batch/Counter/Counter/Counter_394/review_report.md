# Play-Annotation-Generator Annotation Review — Counter_394

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_394`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_PullBlock` | SAF1 | defense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `13` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 90 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 91 | START | 91 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `10` | `9` | 94 | START | 94 | 133 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `12` | `11` | 94 | START | 107 | 187 |
| ✅ EXACT | `Action_DownBlock` | LT | `7` | `6` | 94 | START | 94 | 187 |
| ✅ EXACT | `Action_PullBlock` | SAF1 | `4` | `3` | 94 | START | 94 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `13` | `12` | 94 | START | 94 | 169 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 106 | END | 91 | 106 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `7` | 118 | START | 118 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `1` | `0` | 136 | START | 136 | 213 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 187 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_SnapReceive` | 91 | 106 | 16 | inferred_complete_timeline |
| `Action_None` | 107 | 117 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 118 | 135 | 18 | inferred_complete_timeline |
| `Action_None` | 136 | 192 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 135 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 136 | 213 | 78 | inferred_complete_timeline |
| `Action_BallCarry` | 215 | 218 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 223 | 242 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 211 | 121 | inferred_complete_timeline |
| `Action_None` | 272 | 299 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_DownBlock` | 94 | 187 | 94 | inferred_complete_timeline |
| `Action_None` | 188 | 299 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_DownBlock` | 94 | 133 | 40 | inferred_complete_timeline |
| `Action_DownBlock` | 139 | 187 | 49 | inferred_complete_timeline |
| `Action_None` | 188 | 228 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_BallSnap` | 91 | 106 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 107 | 187 | 81 | inferred_complete_timeline |
| `Action_None` | 188 | 299 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 122 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 94 | 169 | 76 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 171 | 187 | 17 | inferred_complete_timeline |
| `Action_None` | 188 | 284 | 97 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 143 | 53 | inferred_complete_timeline |
| `Action_None` | 156 | 164 | 9 | inferred_complete_timeline |
| `Action_None` | 166 | 221 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 124 | 34 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 129 | 138 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 115 | 25 | inferred_complete_timeline |
| `Action_None` | 122 | 134 | 13 | inferred_complete_timeline |
| `Action_None` | 136 | 158 | 23 | inferred_complete_timeline |
| `Action_None` | 183 | 188 | 6 | inferred_complete_timeline |
| `Action_None` | 190 | 234 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 58 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 81 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 90 | 7 | inferred_complete_timeline |
| `Action_None` | 91 | 94 | 4 | inferred_complete_timeline |
| `Action_None` | 106 | 134 | 29 | inferred_complete_timeline |
| `Action_None` | 137 | 146 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 93 | 22 | inferred_complete_timeline |
| `Action_PullBlock` | 94 | 119 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 163 | 73 | inferred_complete_timeline |
| `Action_None` | 167 | 192 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 110–187 | 62 | 5 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 125–299 | 170 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 156–287 | 121 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 161–282 | 109 | 4 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 167–299 | 133 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 170–299 | 126 | 4 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 195–199 | 5 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 235–299 | 65 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 240–253 | 11 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 254–292 | 29 | 3 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 262–299 | 38 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 284–287 | 4 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 296–299 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (2 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `12` (C): Annotated start 94 != Inferred start 107
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '6' (LT) duration 94 frames exceeds threshold 90 frames [start=94, end=187].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '9' (LG) duration 94 frames exceeds threshold 90 frames [start=94, end=187].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '11' (C) duration 94 frames exceeds threshold 90 frames [start=94, end=187].
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [91–106], lower_priority='Action_DownBlock' annotated_start=94, effective_Action_DownBlock_start=107.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [136-213] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [215-218] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [223-242] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-163] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-192] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-211] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-70] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [94-119] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-115] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-134] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-158] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-188] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-234] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-143] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-164] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-221] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-192] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-58] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-81] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-134] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-146] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [94-133] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [139-187] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-228] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-122] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [94-169] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-284] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-124] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-138] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-117] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-128] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-146] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-187] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-141] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-242] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-264] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-279] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-287] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-185] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-282] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-221] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-233] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-253] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-266] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-287] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-287] for track '25' has 1 frames without a visible bounding box.
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

</details>