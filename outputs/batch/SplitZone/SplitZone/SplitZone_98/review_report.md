# Play-Annotation-Generator Annotation Review — SplitZone_98

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_98`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 31
- **Ball Tracks:** 1
- **Action Segments:** 84
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `11` | `11` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `14` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 21 | START | 22 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 21 | START | 22 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 21 | START | 22 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 21 | START | 22 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `16` | `Group` | 21 | START | 22 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 21 | START | 22 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 21 | START | 22 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 21 | START | 22 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `9` | `Group` | 21 | START | 22 | 108 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `5` | 109 | START | 109 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | `16` | `16` | 111 | START | 111 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `1` | `1` | 112 | START | 112 | 127 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `11` | `11` | 112 | START | 112 | 230 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `5` | `5` | 112 | START | 123 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `6` | `6` | 112 | START | 112 | 145 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `7` | `7` | 112 | START | 112 | 230 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 122 | END | 109 | 122 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `12` | 126 | START | 126 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `5` | `5` | 128 | START | 128 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `14` | `14` | 133 | START | 133 | 310 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 230 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 22–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 108 | 87 | inferred_complete_timeline |
| `Action_SnapReceive` | 109 | 122 | 14 | inferred_complete_timeline |
| `Action_None` | 123 | 125 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 126 | 132 | 7 | inferred_complete_timeline |
| `Action_None` | 133 | 329 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 22–318
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 30 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 132 | 85 | inferred_complete_timeline |
| `Action_BallCarry` | 133 | 310 | 178 | inferred_complete_timeline |
| `Action_BallCarry` | 317 | 318 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 22–169
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 110 | 89 | inferred_complete_timeline |
| `Action_SplitBlock` | 111 | 128 | 18 | inferred_complete_timeline |
| `Action_SplitBlock` | 130 | 136 | 7 | inferred_complete_timeline |
| `Action_SplitBlock` | 138 | 169 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 22–329
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 108 | 87 | inferred_complete_timeline |
| `Action_None` | 109 | 129 | 21 | inferred_complete_timeline |
| `Action_None` | 141 | 170 | 30 | inferred_complete_timeline |
| `Action_None` | 173 | 176 | 4 | inferred_complete_timeline |
| `Action_None` | 192 | 329 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 22–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 111 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 230 | 119 | inferred_complete_timeline |
| `Action_None` | 231 | 329 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 22–329
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 111 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 145 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 163 | 230 | 68 | inferred_complete_timeline |
| `Action_None` | 231 | 329 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 22–166
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 108 | 87 | inferred_complete_timeline |
| `Action_BallSnap` | 109 | 122 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 127 | 5 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 128 | 130 | 3 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 132 | 135 | 4 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 138 | 166 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 22–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 111 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 230 | 119 | inferred_complete_timeline |
| `Action_None` | 231 | 329 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 22–329
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 111 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 127 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 230 | 94 | inferred_complete_timeline |
| `Action_None` | 231 | 329 | 99 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 22–167
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 108 | 87 | inferred_complete_timeline |
| `Action_None` | 109 | 167 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 22–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 108 | 87 | inferred_complete_timeline |
| `Action_None` | 109 | 329 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 22–329
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 108 | 87 | inferred_complete_timeline |
| `Action_None` | 109 | 194 | 86 | inferred_complete_timeline |
| `Action_None` | 197 | 198 | 2 | inferred_complete_timeline |
| `Action_None` | 200 | 203 | 4 | inferred_complete_timeline |
| `Action_None` | 210 | 329 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 22–233
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 108 | 87 | inferred_complete_timeline |
| `Action_None` | 109 | 161 | 53 | inferred_complete_timeline |
| `Action_None` | 168 | 191 | 24 | inferred_complete_timeline |
| `Action_None` | 193 | 199 | 7 | inferred_complete_timeline |
| `Action_None` | 203 | 205 | 3 | inferred_complete_timeline |
| `Action_None` | 207 | 233 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 22–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 108 | 87 | inferred_complete_timeline |
| `Action_None` | 109 | 329 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 22–165
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 108 | 87 | inferred_complete_timeline |
| `Action_None` | 109 | 165 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 22–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 108 | 87 | inferred_complete_timeline |
| `Action_None` | 109 | 329 | 221 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 117–147 | 27 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 139–329 | 191 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 140–329 | 187 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 173–329 | 147 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 176–329 | 154 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 186–329 | 144 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 189–329 | 141 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 209–329 | 101 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 217–329 | 113 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 219–329 | 111 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 223–329 | 99 | 4 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 232–233 | 2 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 242–329 | 88 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 299–311 | 13 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 327–329 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | 22 | 110 | 89 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `5` (C): Annotated start 112 != Inferred start 123
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 45 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (RT) duration 119 frames exceeds threshold 90 frames [start=112, end=230].
- ⚠️ Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [109–122], lower_priority='Action_ZoneBlock' annotated_start=112, effective_Action_ZoneBlock_start=123.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (LG) duration 119 frames exceeds threshold 90 frames [start=112, end=230].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (RG) duration 119 frames exceeds threshold 90 frames [start=112, end=230].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (LT) duration 119 frames exceeds threshold 90 frames [start=112, end=230].
- ⚠️ Action 'Action_None' range [109-165] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-127] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-329] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-194] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [128-130] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [132-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [138-166] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-145] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [163-230] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-230] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-129] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-170] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-167] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-230] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-161] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-191] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-199] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-233] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-30] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [133-310] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [317-318] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [111-128] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [130-136] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [138-169] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-126] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-147] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-234] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-199] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-320] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-245] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-308] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-254] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-311] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '31' has 1 frames without a visible bounding box.
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

</details>