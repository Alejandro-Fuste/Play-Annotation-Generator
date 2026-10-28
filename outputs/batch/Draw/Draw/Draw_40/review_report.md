# Play-Annotation-Generator Annotation Review — Draw_40

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_40`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 29
- **Ball Tracks:** 1
- **Action Segments:** 108
- **Validation Warnings:** 120
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `4` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `1` | `0` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_Handoff` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 72 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `4` | 70 | START | 70 | 84 |
| ✅ EXACT | `Action_PassBlock` | RT | `1` | `0` | 73 | START | 73 | 119 |
| ✅ EXACT | `Action_PassBlock` | LG | `12` | `11` | 73 | START | 73 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `4` | `3` | 73 | START | 73 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `5` | `4` | 73 | START | 85 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `9` | `8` | 73 | START | 73 | 103 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 84 | END | 70 | 84 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `11` | `10` | 86 | START | 86 | 97 |
| ❌ MISSING SEGMENT | `Action_Handoff` | QB | `11` | `10` | 101 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `14` | `13` | 113 | START | 113 | 121 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 158 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_SnapReceive` | 70 | 84 | 15 | inferred_complete_timeline |
| `Action_None` | 85 | 85 | 1 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 86 | 97 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–278
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 89 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 100 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 112 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 113 | 121 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 123 | 152 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 154 | 278 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 103 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 123 | 129 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 133 | 149 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 92 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_BallSnap` | 70 | 84 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 88 | 103 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 105 | 127 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 131 | 158 | 28 | inferred_complete_timeline |
| `Action_None` | 159 | 201 | 43 | inferred_complete_timeline |
| `Action_None` | 204 | 296 | 93 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 152 | 80 | inferred_complete_timeline |
| `Action_PassBlock` | 154 | 158 | 5 | inferred_complete_timeline |
| `Action_None` | 159 | 163 | 5 | inferred_complete_timeline |
| `Action_None` | 169 | 171 | 3 | inferred_complete_timeline |
| `Action_None` | 211 | 224 | 14 | inferred_complete_timeline |
| `Action_None` | 226 | 227 | 2 | inferred_complete_timeline |
| `Action_None` | 229 | 240 | 12 | inferred_complete_timeline |
| `Action_None` | 242 | 244 | 3 | inferred_complete_timeline |
| `Action_None` | 246 | 299 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 119 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 152 | 83 | inferred_complete_timeline |
| `Action_None` | 154 | 299 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 144 | 75 | inferred_complete_timeline |
| `Action_None` | 148 | 152 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 96 | 27 | inferred_complete_timeline |
| `Action_None` | 99 | 103 | 5 | inferred_complete_timeline |
| `Action_None` | 108 | 126 | 19 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_None` | 137 | 152 | 16 | inferred_complete_timeline |
| `Action_None` | 160 | 166 | 7 | inferred_complete_timeline |
| `Action_None` | 170 | 175 | 6 | inferred_complete_timeline |
| `Action_None` | 192 | 195 | 4 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_None` | 201 | 295 | 95 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 131 | 62 | inferred_complete_timeline |
| `Action_None` | 133 | 185 | 53 | inferred_complete_timeline |
| `Action_None` | 187 | 225 | 39 | inferred_complete_timeline |
| `Action_None` | 227 | 250 | 24 | inferred_complete_timeline |
| `Action_None` | 252 | 268 | 17 | inferred_complete_timeline |
| `Action_None` | 270 | 285 | 16 | inferred_complete_timeline |
| `Action_None` | 294 | 299 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 299 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 237 | 168 | inferred_complete_timeline |
| `Action_None` | 242 | 299 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–94 | 95 | 2 | Undefined position; Undefined team |
| `14` | `18` | Position_Unknown | Team_Unknown | 116–175 | 60 | 1 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 116–299 | 173 | 5 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 161–299 | 88 | 6 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 163–299 | 137 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 184–299 | 112 | 3 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 188–189 | 2 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 190–299 | 79 | 7 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 237–298 | 61 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 243–291 | 48 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 263–299 | 37 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 265–293 | 24 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 275–277 | 3 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 289–296 | 8 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 294–299 | 6 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 299–299 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `24` | 180 | 180 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (5 segments found)
- ❌ Missing segment for action `Action_Handoff` on target `11` (QB)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (3 segments found)

### Track Identity Issues

- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 84 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '15' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [70–84], lower_priority='Action_PassBlock' annotated_start=73, effective_Action_PassBlock_start=85.
- ⚠️ Segment 'Action_Handoff' for track '10' has invalid range: start=101, end=97. Clamping end to start.
- ⚠️ Action 'Action_PassBlock' range [73-119] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-237] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-144] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-152] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [154-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-163] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-224] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-240] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-299] for track '3' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [85-86] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [88-103] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [105-127] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [131-158] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-201] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-296] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-299] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-131] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-185] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-225] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-250] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-268] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-285] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-299] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-152] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-103] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [111-112] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [115-118] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [123-129] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [133-149] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-96] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-103] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-126] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-152] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-166] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-295] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakePassDroptoHandoff' range [86-97] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-92] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-94] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-70] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-89] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-112] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [113-121] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [123-152] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [154-278] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-175] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-127] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-152] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-177] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-185] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-231] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-291] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-299] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-240] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-299] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-201] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-231] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-248] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-258] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-283] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-299] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-258] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-298] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-248] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-291] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-285] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-296] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>