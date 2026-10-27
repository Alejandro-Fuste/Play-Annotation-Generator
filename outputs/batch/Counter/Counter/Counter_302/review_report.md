# Play-Annotation-Generator Annotation Review — Counter_302

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_302`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 110
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `7` | `6` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `13` | `12` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `13` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 3 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 3 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 3 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 3 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 3 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 3 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 3 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 3 | START | 0 | 56 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `8` | 57 | START | 57 | 68 |
| ✅ EXACT | `Action_DownBlock` | LG | `5` | `4` | 60 | START | 60 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `7` | `6` | 60 | START | 60 | 93 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `9` | `8` | 60 | START | 71 | 144 |
| ✅ EXACT | `Action_PullBlock` | RG | `13` | `12` | 60 | START | 60 | 144 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `11` | `10` | 60 | START | 60 | 144 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 68 | END | 57 | 68 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `13` | 77 | START | 77 | 101 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `1` | `0` | 102 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 144 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_SnapReceive` | 57 | 68 | 12 | inferred_complete_timeline |
| `Action_None` | 69 | 76 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 77 | 101 | 25 | inferred_complete_timeline |
| `Action_None` | 102 | 156 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 245 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_DownBlock` | 60 | 93 | 34 | inferred_complete_timeline |
| `Action_DownBlock` | 95 | 130 | 36 | inferred_complete_timeline |
| `Action_DownBlock` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 144 | 144 | 1 | inferred_complete_timeline |
| `Action_None` | 145 | 299 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_DownBlock` | 60 | 144 | 85 | inferred_complete_timeline |
| `Action_None` | 145 | 299 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_BallSnap` | 57 | 68 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 71 | 144 | 74 | inferred_complete_timeline |
| `Action_None` | 145 | 190 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PullBlock` | 60 | 144 | 85 | inferred_complete_timeline |
| `Action_None` | 145 | 218 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–261
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 60 | 144 | 85 | inferred_complete_timeline |
| `Action_None` | 145 | 261 | 117 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 96 | 40 | inferred_complete_timeline |
| `Action_None` | 107 | 294 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 78 | 22 | inferred_complete_timeline |
| `Action_None` | 96 | 103 | 8 | inferred_complete_timeline |
| `Action_None` | 105 | 198 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 75 | 19 | inferred_complete_timeline |
| `Action_None` | 79 | 106 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 60 | 4 | inferred_complete_timeline |
| `Action_None` | 62 | 75 | 14 | inferred_complete_timeline |
| `Action_None` | 77 | 85 | 9 | inferred_complete_timeline |
| `Action_None` | 105 | 113 | 9 | inferred_complete_timeline |
| `Action_None` | 116 | 125 | 10 | inferred_complete_timeline |
| `Action_None` | 127 | 142 | 16 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_None` | 148 | 150 | 3 | inferred_complete_timeline |
| `Action_None` | 153 | 299 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 134 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 123 | 67 | inferred_complete_timeline |
| `Action_None` | 125 | 299 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 267 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 93 | 37 | inferred_complete_timeline |
| `Action_None` | 95 | 97 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `19` | Position_Unknown | Team_Unknown | 41–177 | 137 | 2 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 99–299 | 198 | 3 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 105–299 | 186 | 5 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 149–181 | 32 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 152–153 | 2 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 158–299 | 138 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 164–299 | 134 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 169–281 | 113 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 169–299 | 131 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 175–293 | 117 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 204–212 | 8 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 208–299 | 90 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 208–233 | 26 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 243–259 | 15 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 247–249 | 3 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 275–278 | 4 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 287–299 | 13 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 289–292 | 4 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 289–294 | 4 | 2 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 291–292 | 2 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 299–299 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (4 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `9` (C): Annotated start 60 != Inferred start 71
- ❌ Missing segment for action `Action_BallCarry` on target `1` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '0' has invalid range: start=102, end=94. Clamping end to start.
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [57–68], lower_priority='Action_DownBlock' annotated_start=60, effective_Action_DownBlock_start=69.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-134] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-123] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-299] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-96] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-294] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-245] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [60-93] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [95-130] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [141-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-299] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-267] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [57-68] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [71-144] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-78] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-103] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-198] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [60-144] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-261] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-75] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-106] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [60-144] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-218] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-156] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-60] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-75] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-125] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-142] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-93] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-154] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-202] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-222] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-261] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-160] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-181] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-171] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-271] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-281] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-204] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-293] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-209] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-218] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-271] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-233] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-255] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-278] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-292] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '35' has 1 frames without a visible bounding box.
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

</details>