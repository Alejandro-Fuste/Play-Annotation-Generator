# Play-Annotation-Generator Annotation Review — JetSweep_49

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_49`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 114
- **Validation Warnings:** 146
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 93
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | TE | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Toss` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `17` | `16` | 67 | START | 67 | 98 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 72 | START | 72 | 83 |
| ✅ EXACT | `Action_LeadBlock` | RB | `5` | `4` | 74 | START | 74 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | TE | `4` | `3` | 74 | START | 74 | 208 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `11` | 74 | START | 84 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `2` | `1` | 74 | START | 74 | 103 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `2` | 74 | START | 74 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `6` | `5` | 74 | START | 74 | 97 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 83 | END | 72 | 83 |
| ✅ EXACT | `Action_Toss` | QB | `9` | `8` | 91 | START | 91 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `17` | `16` | 101 | START | 101 | 193 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 124 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_SnapReceive` | 72 | 83 | 12 | inferred_complete_timeline |
| `Action_None` | 84 | 90 | 7 | inferred_complete_timeline |
| `Action_Toss` | 91 | 100 | 10 | inferred_complete_timeline |
| `Action_None` | 101 | 134 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_LeadBlock` | 74 | 113 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_SealBlock` | 74 | 208 | 135 | inferred_complete_timeline |
| `Action_SealBlock` | 231 | 238 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 122 | 49 | inferred_complete_timeline |
| `Action_None` | 130 | 133 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 103 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 124 | 19 | inferred_complete_timeline |
| `Action_None` | 125 | 148 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–361
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_BallSnap` | 72 | 83 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 92 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 124 | 30 | inferred_complete_timeline |
| `Action_None` | 125 | 154 | 30 | inferred_complete_timeline |
| `Action_None` | 184 | 361 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 97 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 105 | 106 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 114 | 43 | inferred_complete_timeline |
| `Action_None` | 120 | 131 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–284
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 80 | 9 | inferred_complete_timeline |
| `Action_None` | 90 | 259 | 170 | inferred_complete_timeline |
| `Action_None` | 268 | 284 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 75 | 4 | inferred_complete_timeline |
| `Action_None` | 108 | 109 | 2 | inferred_complete_timeline |
| `Action_None` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_None` | 123 | 125 | 3 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 87 | 16 | inferred_complete_timeline |
| `Action_None` | 89 | 94 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 199 | 128 | inferred_complete_timeline |
| `Action_None` | 210 | 307 | 98 | inferred_complete_timeline |
| `Action_None` | 312 | 389 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 126 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 190 | 119 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–135 | 127 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–5 | 6 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 67–389 | 247 | 12 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 112–389 | 206 | 4 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 126–138 | 13 | 1 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 127–135 | 9 | 1 | Undefined position; Undefined team |
| `20` | `29` | Position_Unknown | Team_Unknown | 132–281 | 147 | 2 | Undefined position; Undefined team |
| `21` | `34` | Position_Unknown | Team_Unknown | 143–169 | 27 | 1 | Undefined position; Undefined team |
| `22` | `35` | Position_Unknown | Team_Unknown | 156–389 | 233 | 2 | Undefined position; Undefined team |
| `23` | `36` | Position_Unknown | Team_Unknown | 159–250 | 73 | 2 | Undefined position; Undefined team |
| `24` | `37` | Position_Unknown | Team_Unknown | 177–237 | 55 | 2 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 190–299 | 110 | 1 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 205–240 | 36 | 1 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 210–389 | 140 | 5 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 219–306 | 67 | 4 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 222–282 | 61 | 1 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 230–389 | 160 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 233–259 | 24 | 2 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 243–384 | 142 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 273–349 | 77 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 273–389 | 117 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 290–389 | 100 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 294–296 | 3 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 335–339 | 5 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 338–389 | 52 | 1 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 342–389 | 38 | 5 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 343–389 | 47 | 1 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 361–389 | 29 | 1 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 362–389 | 26 | 2 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 389–389 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SealBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (10 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 82 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 100: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 100: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [72–83], lower_priority='Action_ZoneBlock' annotated_start=74, effective_Action_ZoneBlock_start=84.
- ⚠️ Action 'Action_None' range [72-107] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-135] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-103] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-148] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-122] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [74-208] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [231-238] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [74-113] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-97] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [105-106] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-126] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-199] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-307] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-134] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-87] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-94] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-114] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-131] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-85] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-92] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-124] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-154] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-361] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-190] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-75] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-80] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-259] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-284] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [67-98] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [101-193] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [208-239] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [256-257] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [260-263] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [281-282] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [286-287] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [289-293] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [298-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [309-310] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-143] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-356] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-375] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-389] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-138] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-178] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-281] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-169] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-238] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-229] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-208] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-237] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-299] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-240] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-222] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-307] for track '27' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-380] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-389] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-242] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-285] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-301] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-306] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-282] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-389] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-247] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-259] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-384] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-349] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-339] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-347] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-354] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-372] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-369] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>