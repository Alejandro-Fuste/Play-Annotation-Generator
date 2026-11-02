# Play-Annotation-Generator Annotation Review — JetSweep_124

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_124`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `6` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `19` | `18` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Toss` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `2` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `5` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 45 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 44 | START | 44 | 56 |
| ✅ EXACT | `Action_LeadBlock` | RB | `3` | `2` | 46 | START | 46 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `1` | `0` | 46 | START | 46 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `11` | 46 | START | 57 | 146 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `16` | `15` | 46 | START | 46 | 148 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `6` | `5` | 46 | START | 46 | 169 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `6` | 46 | START | 46 | 71 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `19` | `18` | 47 | START | 47 | 70 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 56 | END | 44 | 56 |
| ✅ EXACT | `Action_Toss` | QB | `15` | `14` | 62 | START | 62 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `19` | `18` | 71 | START | 71 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | `7` | `6` | 72 | START | 72 | 152 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 169 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_SnapReceive` | 44 | 56 | 13 | inferred_complete_timeline |
| `Action_None` | 57 | 61 | 5 | inferred_complete_timeline |
| `Action_Toss` | 62 | 70 | 9 | inferred_complete_timeline |
| `Action_None` | 71 | 122 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_LeadBlock` | 46 | 169 | 124 | inferred_complete_timeline |
| `Action_None` | 170 | 239 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 239 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 137 | 94 | inferred_complete_timeline |
| `Action_None` | 156 | 239 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 75 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 101 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 156 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 71 | 26 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 72 | 152 | 81 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 154 | 169 | 16 | inferred_complete_timeline |
| `Action_None` | 170 | 226 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_BallSnap` | 44 | 56 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 146 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 151 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 169 | 6 | inferred_complete_timeline |
| `Action_None` | 170 | 239 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 169 | 124 | inferred_complete_timeline |
| `Action_None` | 170 | 239 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 148 | 103 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 98 | 55 | inferred_complete_timeline |
| `Action_None` | 100 | 137 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 78 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 71 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 68 | 25 | inferred_complete_timeline |
| `Action_None` | 85 | 88 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 239 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 97 | 54 | inferred_complete_timeline |
| `Action_None` | 99 | 186 | 88 | inferred_complete_timeline |
| `Action_None` | 188 | 198 | 11 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_None` | 213 | 239 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 239 | 196 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 23–29 | 7 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 45–47 | 3 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 47–212 | 161 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 75–113 | 37 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 93–188 | 90 | 4 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 108–120 | 13 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 110–239 | 130 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 113–238 | 113 | 4 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 123–194 | 67 | 3 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 125–139 | 6 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 127–239 | 113 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 127–239 | 113 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 136–200 | 65 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 155–239 | 85 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 166–184 | 5 | 2 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 200–239 | 40 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 208–239 | 29 | 2 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 221–230 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '0' (LT) duration 111 frames exceeds threshold 90 frames [start=46, end=156].
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '2' (RB) duration 124 frames exceeds threshold 90 frames [start=46, end=169].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (RG) duration 124 frames exceeds threshold 90 frames [start=46, end=169].
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '6' (LG) duration 98 frames exceeds threshold 90 frames [start=72, end=169].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (C) duration 124 frames exceeds threshold 90 frames [start=46, end=169].
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [44–56], lower_priority='Action_ZoneBlock' annotated_start=46, effective_Action_ZoneBlock_start=57.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (RT) duration 103 frames exceeds threshold 90 frames [start=46, end=148].
- ⚠️ Action 'Action_ZoneBlock' range [46-75] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-101] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [107-156] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-71] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-137] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-239] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [72-152] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-226] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-98] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-137] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-78] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [57-146] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [148-151] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-97] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-186] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-198] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-68] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-88] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-122] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [46-148] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-29] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-47] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [71-165] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [171-212] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-113] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-172] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-188] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-120] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-160] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-232] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-152] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-181] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-194] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-239] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-200] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-212] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-239] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-225] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '33' has 1 frames without a visible bounding box.
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

</details>