# Play-Annotation-Generator Annotation Review — Counter_244

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_244`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 69
- **Validation Warnings:** 79
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `1` | `0` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `16` | `15` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `7` | `6` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `17` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 6 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `16` | `15` | 7 | START | 7 | 8 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `1` | `0` | 9 | START | 9 | 54 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `16` | `15` | 9 | START | 9 | 29 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | Position_Unknown | `7` | `6` | 9 | START | N/A | N/A |
| ✅ EXACT | `Action_PullBlock` | LG | `6` | `5` | 9 | START | 9 | 93 |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | `7` | `6` | 9 | START | 9 | 65 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 22 | END | 7 | 22 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `7` | 33 | START | 33 | 59 |
| ✅ EXACT | `Action_BallCarry` | RB | `10` | `9` | 60 | START | 60 | 70 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 93 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_SnapReceive` | 7 | 22 | 16 | inferred_complete_timeline |
| `Action_None` | 23 | 32 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 33 | 59 | 27 | inferred_complete_timeline |
| `Action_None` | 60 | 80 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 59 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 60 | 70 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–24
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 20 | 14 | inferred_complete_timeline |
| `Action_None` | 22 | 24 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–33
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 33 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PullBlock` | 9 | 93 | 85 | inferred_complete_timeline |
| `Action_None` | 94 | 114 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 9 | 54 | 46 | inferred_complete_timeline |
| `Action_DownBlock` | 63 | 93 | 31 | inferred_complete_timeline |
| `Action_None` | 94 | 143 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 18–129
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 18 | 90 | 73 | inferred_complete_timeline |
| `Action_None` | 96 | 129 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 257 | 251 | inferred_complete_timeline |
| `Action_None` | 263 | 269 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 111 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 87 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 102 | 96 | inferred_complete_timeline |
| `Action_None` | 107 | 124 | 18 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 60 | 54 | inferred_complete_timeline |
| `Action_None` | 64 | 99 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 117 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 269 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 269 | 263 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–65 | 66 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–29 | 30 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 43–203 | 157 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 52–138 | 87 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 72–133 | 62 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 78–269 | 180 | 4 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 83–269 | 187 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 84–108 | 25 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 86–245 | 150 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 91–130 | 38 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 94–199 | 106 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 99–258 | 160 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 133–269 | 137 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 134–149 | 9 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 138–247 | 105 | 2 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 266–268 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `1` (2 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `7` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 490: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Overlapping action conflict at frame 9 for track '6': 'Action_DownBlock' vs 'Action_PullLeadBlock'. Overriding with 'Action_PullLeadBlock'.
- ⚠️ Action 'Action_DownBlock' range [9-54] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [63-93] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-143] for track '0' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-117] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-60] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-99] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-33] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-257] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-114] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [9-65] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-80] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [60-70] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-111] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-269] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-102] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-124] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-87] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-20] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-24] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [9-29] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-90] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-129] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-196] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-138] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-245] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-256] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-108] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-245] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-130] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-199] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-258] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-149] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-232] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-247] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>